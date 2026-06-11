# Git Commands: A Practical Cheat Sheet For QA

Source: user-provided article "A Cheat Sheet for Git Commands", updated with official Git documentation
Date added: 2026-06-11
Related plan item: Automation
Tags: QA, automation, Git, version control, branches, commits
Language: English
Translation pair: quality-assurance/overview/07-automation/git-command-cheat-sheet.md

## Summary

Git is a distributed version control system. QA engineers use it to store automated tests, test data, configuration, CI/CD files, and technical documentation.

It is useful to understand four locations:

```text
Working tree -> Staging area (index) -> Local repository -> Remote repository
```

A common workflow:

```bash
git status
git switch -c test/login-validation
# edit files
git diff
git add tests/test_login.py
git diff --staged
git commit -m "Add login validation tests"
git push -u origin test/login-validation
```

## Key Points

- Run `git status` before a command that changes repository state.
- `git diff` shows unstaged changes; `git diff --staged` shows changes prepared for commit.
- `git add` does not save history. It copies selected content into the staging area.
- `git commit` creates a local snapshot; `git push` sends commits to a remote.
- `git fetch` downloads remote information without changing the current branch.
- Prefer `git switch` for branches and `git restore` for restoring files.
- `git pull` combines fetch with merge or rebase, depending on configuration.
- `git reset --hard`, `git clean`, force push, and forced branch deletion can destroy work.
- `git revert` is usually safer than rewriting published shared history.
- Review the staged diff before every commit.

## Terms

| Term | Meaning |
| --- | --- |
| Repository | Project history, commits, branches, and tags |
| Working tree | Files currently checked out on disk |
| Staging area / index | Content prepared for the next commit |
| Commit | A recorded snapshot with author, time, and message |
| Branch | A movable reference to a sequence of commits |
| `HEAD` | A reference to the current branch or selected commit |
| Remote | A configured external repository |
| `origin` | A conventional, not mandatory, remote name after clone |
| Upstream branch | The remote branch tracked by a local branch |
| Merge | Combining branch histories |
| Rebase | Replaying commits onto another base with new hashes |
| Detached HEAD | A state where a commit, rather than a branch, is checked out |
| Stash | Temporary storage for unfinished changes |
| Tag | A stable label that points to a commit |

## Setup And Configuration

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list --show-origin
git config --global init.defaultBranch main
git help switch
git switch --help
```

Do not put access tokens or passwords into repository configuration or commands that may remain in shell history. Use an approved credential manager, SSH key, or team authentication mechanism.

## Create Or Obtain A Repository

```bash
git init
git clone https://example.com/team/project.git
git clone https://example.com/team/project.git qa-tests
git remote -v
git remote add origin https://example.com/team/project.git
git remote set-url origin https://example.com/team/new-project.git
git remote remove origin
```

`git remote remove` removes the local remote configuration. It does not delete the external repository.

## Inspect State

```bash
git status
git status --short
git diff
git diff -- tests/test_login.py
git diff --staged
git ls-files
git check-ignore -v reports/result.xml
```

A useful pre-commit habit:

```bash
git status
git diff
git diff --staged
```

## Staging And Files

```bash
git add tests/test_login.py
git add tests/ fixtures/
git add .
git add -p
git restore --staged tests/test_login.py
git rm obsolete_test.py
git rm --cached local.env
git mv old_name.py new_name.py
```

`git add .` includes new, modified, and deleted files under the given pathspec. Check `git status` first to avoid staging reports, secrets, or temporary files.

## Commits

```bash
git commit -m "Add API smoke tests"
git commit
git commit -am "Update login assertions"
git commit --amend
git show
git show <commit-hash>
```

`git commit -am` does not include new untracked files. `--amend` rewrites the latest commit and should be used carefully after publication.

Useful commit messages describe the change:

```text
Add checkout API regression tests
Fix flaky wait in payment test
Update CI browser matrix
```

## History And Search

```bash
git log
git log --oneline
git log --oneline --graph --decorate --all
git log --follow -- tests/test_login.py
git log -p
git blame tests/test_login.py
git grep "checkout"
```

`git blame` identifies the latest commit for each line, but does not explain why it changed. Inspect the commit and related pull request or issue for context.

## Branches

```bash
git branch
git branch -a
git switch -c test/payment-errors
git switch main
git switch -
git branch -m new-name
git branch -d old-branch
git branch -D old-branch
```

`git switch` separates branch operations from file restoration. The older `git checkout` syntax is still available, but performs several unrelated jobs and is easier to misuse.

## Remote, Fetch, Pull, And Push

```bash
git fetch origin
git fetch --prune origin
git log --oneline --left-right HEAD...origin/main
git pull
git pull --rebase
git push -u origin test/payment-errors
git push
git push origin --delete old-branch
```

`git fetch` is useful before review because it updates remote-tracking references without changing current files. `git pull` changes local history, so confirm the branch, status, and team workflow first.

## Merge And Rebase

```bash
git merge feature/login-tests
git merge --abort
git rebase main
git add <resolved-files>
git rebase --continue
git rebase --abort
```

When resolving a conflict:

1. Run `git status`.
2. Find conflict markers.
3. Choose the correct final content.
4. Remove the markers.
5. Stage resolved files with `git add`.
6. Continue the merge or rebase.
7. Run the tests.

Rebase changes commit hashes. Do not rewrite shared commits that other contributors already use without coordination.

## Stash

```bash
git stash push -m "WIP login tests"
git stash push -u -m "WIP login tests"
git stash list
git stash show -p stash@{0}
git stash apply stash@{0}
git stash pop
git stash drop stash@{0}
```

Stash is temporary storage, not a durable archive. For important unfinished work, a branch and commit are usually safer.

## Undo Changes Safely

```bash
git restore --staged tests/test_login.py
git restore tests/test_login.py
git restore --source=<commit-hash> -- tests/test_login.py
git revert <commit-hash>
git reset --mixed HEAD~1
git reflog
```

`git restore <file>` discards unstaged changes in that file. Inspect the diff first.

For shared history, prefer `git revert`: it records a new inverse commit instead of deleting the original commit.

## Dangerous Commands

```bash
git reset --hard <commit>
git clean -fd
git branch -D <branch>
git push --force
git switch --discard-changes <branch>
```

Risks:

- `reset --hard` replaces the index and working tree;
- `clean -fd` deletes untracked files and directories;
- `branch -D` deletes a branch even when it is not merged;
- `push --force` can overwrite remote history;
- `switch --discard-changes` discards conflicting local changes.

When rewriting your own remote branch is truly necessary, `git push --force-with-lease` is safer than `--force` because it checks the expected remote state. It still requires care and team agreement.

## Tags

```bash
git tag
git tag -a v1.2.0 -m "Release v1.2.0"
git push origin v1.2.0
git push origin --tags
```

Tags are commonly used for releases or stable versions of a test framework.

## Practical QA Workflow

```bash
git fetch --prune origin
git switch main
git pull --ff-only
git switch -c test/refund-api

# edit and test
git status
git diff
git add tests/api/test_refund.py fixtures/refund.json
git diff --staged
git commit -m "Add refund API tests"
git push -u origin test/refund-api
```

The usual next steps are creating a Pull Request, running CI checks, and completing code review.

## Questions

### 1. How does the working tree differ from the staging area?

The working tree contains current files on disk. The staging area contains the exact file versions selected for the next commit.

### 2. How does `git fetch` differ from `git pull`?

`fetch` downloads data and updates remote-tracking references without changing the current branch. `pull` follows fetching with merge or rebase.

### 3. What do `git diff` and `git diff --staged` show?

The first shows unstaged changes. The second shows content prepared for the next commit.

### 4. Why can `git commit -am` miss a file?

The `-a` option stages changes to tracked files, but does not include new untracked files.

### 5. When should `git revert` be used?

Use it to safely undo a published commit without rewriting shared history.

### 6. Why is `git reflog` useful?

It records recent positions of `HEAD` and branches and may help locate commits after an accidental reset or rebase.

### 7. Why is force push dangerous?

It can replace remote history and remove commits used by other contributors.

### 8. What should be checked before a commit?

The current branch, status, unstaged diff, staged diff, absence of secrets, and relevant test results.

## What To Review Later

- merge conflicts;
- interactive rebase;
- commit signing;
- Git hooks;
- `.gitignore` patterns;
- submodules and worktrees;
- branch protection and Pull Request workflow;
- the Git workflow used by your team.

## Sources

- User-provided article: "A Cheat Sheet for Git Commands"
- [Git documentation: switch](https://git-scm.com/docs/git-switch)
- [Git documentation: restore](https://git-scm.com/docs/git-restore)
- [Git documentation: add](https://git-scm.com/docs/git-add)
- [Git documentation: reset](https://git-scm.com/docs/git-reset)
- [Git documentation: push](https://git-scm.com/docs/git-push)
