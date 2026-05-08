# CCNA Study Project

Учебный репозиторий для подготовки к CCNA. Здесь собираются Markdown-конспекты, статьи, вопросы для самопроверки, лабораторные заметки и статический сайт для удобного чтения с телефона или компьютера.

## Что внутри

- [STUDY_PLAN.md](STUDY_PLAN.md) - общий план подготовки.
- `articles/` - обработанные статьи по календарю: `YYYY-MM/week-XX/NN-topic.md`.
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

## Формат статей

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

## Статический сайт

Проект собирается в статический сайт на MkDocs Material. Источники остаются в `articles/` и `STUDY_PLAN.md`, а `scripts/sync_docs.py` готовит копии для сайта в `docs/`.

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

Подробности деплоя: [DEPLOY.md](DEPLOY.md).

## Что не хранится в git

В репозиторий не должны попадать локальные окружения, собранный сайт и сгенерированные копии документов:

- `.venv/`
- `.vendor/`
- `site/`
- `docs/articles/`
- `docs/study-plan.md`
- временные файлы и логи

PDF-оригиналы и приватные учетные данные также не добавляются в репозиторий.

## Назначение

Это личный учебный проект: цель - постепенно превратить материалы CCNA в удобную базу знаний и сайт для повторения до конца лета.
