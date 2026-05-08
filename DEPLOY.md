# Deploy CCNA Site

Проект собирается как статический сайт на MkDocs Material и отдается через nginx в Docker.

## Локальная проверка

Синхронизировать Markdown-источники в `docs/`:

```powershell
python scripts/sync_docs.py
```

Запустить dev-сервер через Docker:

```powershell
docker compose --profile dev up ccna-site-dev
```

Открыть:

```text
http://localhost:8000
```

## Production на Linux VM

На VM с Docker:

```bash
git clone <repo-url> ccna
cd ccna
docker compose up -d --build ccna-site
```

Открыть с телефона в той же сети:

```text
http://<vm-ip>:8080
```

## HTTPS в локальной сети

Обычный самоподписанный сертификат не убирает предупреждение браузера. Чтобы браузер доверял сайту, нужно:

1. Создать локальный CA.
2. Подписать им сертификат сайта с `subjectAltName` для IP VM.
3. Установить CA-сертификат как доверенный на телефон/ПК.
4. Запустить сайт с HTTPS override.

Сгенерировать сертификаты локально:

```powershell
.\scripts\new-local-ca-cert.ps1 -SiteIp 192.168.50.206 -SiteDns ccna.local
```

После этого появится папка `certs/`. В git она не добавляется, потому что содержит приватные ключи.

На VM папка `certs/` должна лежать рядом с `docker-compose.yml`, а внутри должны быть:

```text
certs/ccna-site.crt
certs/ccna-site.key
```

Запуск HTTPS-варианта:

```bash
docker compose -f docker-compose.yml -f docker-compose.https.yml up -d --build ccna-site
```

Открыть:

```text
https://<vm-ip>:8443
```

Чтобы браузер не ругался, установи `certs/ccna-local-ca.crt` в доверенные корневые центры сертификации на каждом устройстве, с которого читаешь сайт.

## Обновление после новых статей

Для HTTP-варианта:

```bash
git pull
docker compose up -d --build ccna-site
```

Для HTTPS-варианта:

```bash
git pull
docker compose -f docker-compose.yml -f docker-compose.https.yml up -d --build ccna-site
```

## Как это работает

```text
articles/ + STUDY_PLAN.md
-> scripts/sync_docs.py
-> docs/
-> mkdocs build
-> nginx container
```

`articles/` остается главным источником статей. Папка `docs/articles/` генерируется перед сборкой и не хранится в git.
