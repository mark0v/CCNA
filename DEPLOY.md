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

## Обновление после новых статей

```bash
git pull
docker compose up -d --build ccna-site
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
