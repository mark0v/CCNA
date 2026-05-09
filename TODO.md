# TODO

## Site

- Add proper multilingual support with `mkdocs-static-i18n`.
  - Use Russian as the default locale.
  - Add English as an additional locale.
  - Generate localized site paths like `/ru/...` and `/en/...`.
  - Keep `CCNA`, `Englishe`, and future learning sections inside the localized structure.
  - Update `scripts/sync_docs.py` so it can generate localized `docs/` content.
  - Migrate current materials into the Russian locale first, then add English versions gradually.
