# Learning Materials

Учебный портал с материалами по разным направлениям. Сейчас внутри есть два больших раздела:

- `CCNA` - сетевые технологии, статьи, лабораторные заметки и план подготовки.
- `Englishe` - английские времена и грамматические конструкции.

Проект хранит исходники в Markdown и собирает их в статический сайт на MkDocs Material, чтобы удобно читать материалы с телефона, планшета или компьютера в локальной сети.

## Что внутри

- [STUDY_PLAN.md](STUDY_PLAN.md) - общий план подготовки по CCNA.
- `articles/` - CCNA-статьи по календарю: `YYYY-MM/week-XX/NN-topic.md`.
- `articles-en/` - английские версии CCNA-статей с зеркальной структурой.
- `quality-assurance-en/` - английские версии QA-статей для будущей локализации.
- `englishe/` - материалы по английскому.
- `notes/` - будущие конспекты по темам и урокам.
- `labs/` - разборы лабораторных работ.
- `packet-tracer/` - заметки по топологиям Packet Tracer.
- `cheatsheets/` - короткие шпаргалки.
- `quizzes/` - вопросы, ответы и разбор ошибок.
- `flashcards/` - карточки для повторения.
- `configs/` - фрагменты конфигураций Cisco IOS.
- `resources/` - ссылки и внешние материалы.
- `review/` - еженедельные итоги и повторение.
- `templates/` - шаблоны Markdown-файлов.

## Организация сайта

Верхний уровень навигации разделен по направлениям:

```text
Learning Materials
├─ CCNA
└─ Englishe
```

Новые направления можно добавлять отдельными папками и подключать их в `scripts/sync_docs.py` и `mkdocs.yml`.

## Формат CCNA-статей

Статьи хранятся в `articles/YYYY-MM/week-XX/` и нумеруются внутри недели:

```text
01-what-is-a-network.md
02-what-is-a-switch.md
03-what-is-a-router.md
```

Каждая статья приводится к единому учебному формату:

- summary;
- key points;
- структурированный конспект;
- термины и команды;
- вопросы с ответами;
- блок для повторения.

Базовый шаблон: [templates/article-note.md](templates/article-note.md).

Подробные правила написания, перевода и хранения двух языковых версий описаны в [ARTICLE_GUIDE.md](ARTICLE_GUIDE.md).

## Статический сайт

Источники остаются в `articles/`, `englishe/` и `STUDY_PLAN.md`, а `scripts/sync_docs.py` готовит копии для сайта в `docs/`.

Локальная синхронизация:

```powershell
python scripts/sync_docs.py
```

Локальная сборка:

```powershell
pip install -r requirements.txt
mkdocs build --strict
```

Dev-сервер:

```powershell
mkdocs serve
```

## Docker

Production-вариант собирает сайт и отдает его через nginx:

```bash
docker compose up -d --build ccna-site
```

По умолчанию сайт доступен на порту `8080`:

```text
http://<host-ip>:8080
```

Для локального HTTPS есть отдельный override:

```bash
docker compose -f docker-compose.yml -f docker-compose.https.yml up -d --build ccna-site
```

Сертификаты создаются локально и не хранятся в git. Подробности деплоя: [DEPLOY.md](DEPLOY.md).

## Что не хранится в git

В репозиторий не должны попадать локальные окружения, собранный сайт и сгенерированные копии документов:

- `.venv/`
- `.vendor/`
- `site/`
- `docs/articles/`
- `docs/study-plan.md`
- `docs/ccna/articles/`
- `docs/ccna/study-plan.md`
- `docs/englishe/`
- временные файлы и логи
- локальные TLS-сертификаты и приватные ключи

PDF-оригиналы и приватные учетные данные также не добавляются в репозиторий.
