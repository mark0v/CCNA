# Git Commands: практическая шпаргалка для QA

Source: user-provided article "A Cheat Sheet for Git Commands", updated with official Git documentation
Date added: 2026-06-11
Related plan item: Automation
Tags: QA, automation, Git, version control, branches, commits
Language: Russian
Translation pair: quality-assurance-en/overview/07-automation/git-command-cheat-sheet.md

## Summary

Git — распределённая система контроля версий. В QA она используется для хранения автотестов, test data, конфигураций, CI/CD-файлов и технической документации.

Полезно понимать три состояния файла:

```text
Working tree -> Staging area (index) -> Local repository -> Remote repository
```

Обычный рабочий цикл:

```bash
git status
git switch -c test/login-validation
# изменить файлы
git diff
git add tests/test_login.py
git diff --staged
git commit -m "Add login validation tests"
git push -u origin test/login-validation
```

## Key Points

- Перед изменяющей командой полезно запускать `git status`.
- `git diff` показывает незастейдженные изменения, а `git diff --staged` — подготовленные к коммиту.
- `git add` не сохраняет историю: он только помещает выбранную версию файла в staging area.
- `git commit` создаёт локальный snapshot; `git push` отправляет commits в remote repository.
- `git fetch` безопасно загружает информацию с remote без изменения текущей ветки.
- Для работы с ветками понятнее использовать `git switch`, а для восстановления файлов — `git restore`.
- `git pull` объединяет `fetch` и последующее merge или rebase в зависимости от настройки.
- `git reset --hard`, `git clean`, force push и удаление веток могут уничтожить работу.
- Для общей ветки обычно безопаснее `git revert`, чем переписывание опубликованной истории.
- Перед коммитом нужно проверить не только `status`, но и содержимое staged diff.

## Основные термины

| Термин | Значение |
| --- | --- |
| Repository | История проекта, commits, branches и tags |
| Working tree | Файлы, с которыми пользователь работает сейчас |
| Staging area / index | Содержимое, подготовленное для следующего commit |
| Commit | Сохранённый snapshot с автором, временем и сообщением |
| Branch | Перемещаемая ссылка на последовательность commits |
| `HEAD` | Ссылка на текущую ветку или выбранный commit |
| Remote | Связанный внешний repository |
| `origin` | Обычное, но не обязательное имя remote после clone |
| Upstream branch | Remote branch, с которой связана локальная ветка |
| Merge | Объединение историй веток |
| Rebase | Перенос commits на другую базу с переписыванием их hash |
| Detached HEAD | Состояние, когда выбран commit, а не branch |
| Stash | Временное хранилище незавершённых изменений |
| Tag | Постоянная метка на определённом commit |

## Установка и конфигурация

```bash
# Версия Git
git --version

# Имя и email для новых commits
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Посмотреть настройки и их источник
git config --list --show-origin

# Установить main как имя начальной ветки
git config --global init.defaultBranch main

# Открыть справку
git help switch
git switch --help
```

Не добавляйте access token или пароль в repository config и команды, которые попадут в shell history. Используйте credential manager, SSH key или другой одобренный командой механизм.

## Создание и получение repository

```bash
# Создать Git repository в текущей папке
git init

# Клонировать repository
git clone https://example.com/team/project.git

# Клонировать под другим именем папки
git clone https://example.com/team/project.git qa-tests

# Показать remotes
git remote -v

# Добавить remote
git remote add origin https://example.com/team/project.git

# Изменить URL remote
git remote set-url origin https://example.com/team/new-project.git

# Удалить только связь с remote
git remote remove origin
```

`git remote remove` не удаляет внешний repository. Команда удаляет его описание из локального repository.

## Проверка состояния

```bash
# Полный статус
git status

# Компактный статус
git status --short

# Незастейдженные изменения
git diff

# Изменения в конкретном файле
git diff -- tests/test_login.py

# Изменения, подготовленные к commit
git diff --staged

# Список tracked-файлов
git ls-files

# Почему файл игнорируется
git check-ignore -v reports/result.xml
```

Хорошая привычка перед commit:

```bash
git status
git diff
git diff --staged
```

## Staging area и файлы

```bash
# Добавить один файл
git add tests/test_login.py

# Добавить несколько путей
git add tests/ fixtures/

# Добавить все изменения внутри текущей папки
git add .

# Добавить изменения интерактивно, по фрагментам
git add -p

# Убрать файл из staging, сохранив рабочие изменения
git restore --staged tests/test_login.py

# Удалить tracked-файл
git rm obsolete_test.py

# Перестать отслеживать файл, оставив его на диске
git rm --cached local.env

# Переместить или переименовать файл
git mv old_name.py new_name.py
```

`git add .` включает новые, изменённые и удалённые файлы в пределах указанного pathspec. Перед использованием проверьте `git status`, чтобы случайно не добавить отчёты, secrets или временные файлы.

## Commits

```bash
# Создать commit из staged content
git commit -m "Add API smoke tests"

# Открыть editor для подробного сообщения
git commit

# Добавить tracked-изменения и создать commit
git commit -am "Update login assertions"

# Исправить последний локальный commit
git commit --amend

# Показать последний commit
git show

# Показать конкретный commit
git show <commit-hash>
```

`git commit -am` не добавляет новые untracked-файлы. `--amend` переписывает последний commit, поэтому после публикации его следует применять только при понимании последствий.

Хорошее сообщение отвечает на вопрос, что изменилось:

```text
Add checkout API regression tests
Fix flaky wait in payment test
Update CI browser matrix
```

## Просмотр истории

```bash
# История commits
git log

# Компактная история
git log --oneline

# Граф веток
git log --oneline --graph --decorate --all

# История конкретного файла
git log --follow -- tests/test_login.py

# История с patches
git log -p

# Кто последним изменял строки
git blame tests/test_login.py

# Поиск текста в tracked-файлах
git grep "checkout"
```

`git blame` показывает последний commit для строки, но сам по себе не объясняет причину изменения. Для контекста изучайте commit и связанные PR или issue.

## Ветки

```bash
# Локальные ветки
git branch

# Все локальные и remote-tracking branches
git branch -a

# Создать ветку и переключиться на неё
git switch -c test/payment-errors

# Переключиться на существующую ветку
git switch main

# Вернуться на предыдущую ветку
git switch -

# Переименовать текущую ветку
git branch -m new-name

# Удалить уже объединённую локальную ветку
git branch -d old-branch

# Принудительно удалить локальную ветку
git branch -D old-branch
```

`git switch` отделяет работу с ветками от восстановления файлов. Старый синтаксис `git checkout` остаётся доступным, но выполняет несколько разных задач и поэтому легче приводит к ошибке.

## Remote, fetch, pull и push

```bash
# Загрузить refs и объекты без изменения working tree
git fetch origin

# Обновить данные и удалить устаревшие remote-tracking refs
git fetch --prune origin

# Показать расхождение с remote branch
git log --oneline --left-right HEAD...origin/main

# Получить изменения и объединить их
git pull

# Получить изменения с rebase локальных commits
git pull --rebase

# Отправить текущую ветку и назначить upstream
git push -u origin test/payment-errors

# Последующие отправки связанной ветки
git push

# Удалить remote branch
git push origin --delete old-branch
```

`git fetch` удобен перед review: он обновляет представление о remote и не меняет текущие файлы. `git pull` меняет локальную историю, поэтому перед ним проверьте branch, status и правила команды.

## Merge и rebase

```bash
# Объединить указанную ветку с текущей
git merge feature/login-tests

# Прервать конфликтный merge
git merge --abort

# Перенести локальные commits на актуальный main
git rebase main

# После решения конфликтов продолжить rebase
git add <resolved-files>
git rebase --continue

# Отменить rebase
git rebase --abort
```

При конфликте:

1. Выполнить `git status`.
2. Найти conflict markers в файлах.
3. Выбрать правильное итоговое содержимое.
4. Удалить markers.
5. Добавить решённые файлы через `git add`.
6. Продолжить merge или rebase.
7. Запустить tests.

Rebase меняет commit hashes. Не переписывайте без согласования commits общей ветки, на которые уже опираются другие разработчики.

## Stash

```bash
# Сохранить tracked-изменения
git stash push -m "WIP login tests"

# Сохранить также untracked-файлы
git stash push -u -m "WIP login tests"

# Список stash entries
git stash list

# Просмотреть содержимое
git stash show -p stash@{0}

# Применить, не удаляя entry
git stash apply stash@{0}

# Применить и удалить entry при успехе
git stash pop

# Удалить entry
git stash drop stash@{0}
```

Stash — временный инструмент, а не надёжный архив. Для важной незавершённой работы обычно лучше создать отдельную ветку и commit.

## Безопасная отмена изменений

```bash
# Убрать файл из staging, сохранив изменения
git restore --staged tests/test_login.py

# Отменить незастейдженные изменения файла
git restore tests/test_login.py

# Восстановить файл из конкретного commit
git restore --source=<commit-hash> -- tests/test_login.py

# Создать новый commit, отменяющий опубликованный commit
git revert <commit-hash>

# Переместить текущую локальную ветку на предыдущий commit,
# сохранив изменения в working tree
git reset --mixed HEAD~1

# Найти прежние положения HEAD
git reflog
```

`git restore <file>` удаляет незастейдженные изменения указанного файла. Сначала проверьте diff.

Для shared history обычно используйте `git revert`: он не удаляет старый commit, а добавляет новый обратный commit.

## Опасные команды

```bash
git reset --hard <commit>
git clean -fd
git branch -D <branch>
git push --force
git switch --discard-changes <branch>
```

Риски:

- `reset --hard` заменяет index и working tree;
- `clean -fd` удаляет untracked-файлы и папки;
- `branch -D` удаляет branch даже без merge;
- `push --force` может перезаписать remote history;
- `switch --discard-changes` выбрасывает конфликтующие локальные изменения.

Если переписывание собственной remote branch действительно необходимо, `git push --force-with-lease` безопаснее обычного `--force`, потому что проверяет ожидаемое состояние remote. Но это всё равно операция, которую нужно согласовать.

## Tags

```bash
# Список tags
git tag

# Создать annotated tag
git tag -a v1.2.0 -m "Release v1.2.0"

# Отправить один tag
git push origin v1.2.0

# Отправить все локальные tags
git push origin --tags
```

Tag часто используется для release или стабильной версии test framework.

## Практический QA-сценарий

```bash
# 1. Обновить представление о remote
git fetch --prune origin

# 2. Переключиться на main и получить изменения
git switch main
git pull --ff-only

# 3. Создать рабочую ветку
git switch -c test/refund-api

# 4. После изменений проверить и подготовить файлы
git status
git diff
git add tests/api/test_refund.py fixtures/refund.json
git diff --staged

# 5. Зафиксировать и отправить ветку
git commit -m "Add refund API tests"
git push -u origin test/refund-api
```

Далее создаётся Pull Request, запускаются CI checks и выполняется code review.

## Questions

### 1. Чем working tree отличается от staging area?

Working tree содержит текущие файлы на диске. Staging area содержит именно те версии файлов, которые попадут в следующий commit.

### 2. Чем `git fetch` отличается от `git pull`?

`fetch` загружает данные и обновляет remote-tracking refs, не изменяя текущую ветку. `pull` после получения данных выполняет merge или rebase.

### 3. Что показывают `git diff` и `git diff --staged`?

Первая команда показывает незастейдженные изменения. Вторая показывает содержимое, подготовленное к следующему commit.

### 4. Почему `git commit -am` может пропустить файл?

Опция `-a` автоматически добавляет изменения tracked-файлов, но не включает новые untracked-файлы.

### 5. Когда использовать `git revert`?

Когда нужно безопасно отменить опубликованный commit без переписывания общей истории.

### 6. Зачем нужен `git reflog`?

Он показывает недавние положения `HEAD` и branches и может помочь найти commit после ошибочного reset или rebase.

### 7. Почему force push опасен?

Он может заменить remote history и удалить commits, которые уже используют другие участники.

### 8. Что проверить перед commit?

Текущую ветку, `git status`, незастейдженный diff, staged diff, отсутствие secrets и результаты нужных tests.

## What To Review Later

- merge conflicts;
- interactive rebase;
- commit signing;
- Git hooks;
- `.gitignore` patterns;
- submodules and worktrees;
- branch protection and Pull Request workflow;
- правила Git workflow конкретной команды.

## Sources

- User-provided article: "A Cheat Sheet for Git Commands"
- [Git documentation: switch](https://git-scm.com/docs/git-switch)
- [Git documentation: restore](https://git-scm.com/docs/git-restore)
- [Git documentation: add](https://git-scm.com/docs/git-add)
- [Git documentation: reset](https://git-scm.com/docs/git-reset)
- [Git documentation: push](https://git-scm.com/docs/git-push)
