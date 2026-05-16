# TODO

## Site

- Add proper multilingual support with `mkdocs-static-i18n`.
  - Use Russian as the default locale.
  - Add English as an additional locale.
  - Generate localized site paths like `/ru/...` and `/en/...`.
  - Keep `CCNA`, `Englishe`, and future learning sections inside the localized structure.
  - Update `scripts/sync_docs.py` so it can generate localized `docs/` content.
  - Use `articles/` as the Russian CCNA source and `articles-en/` as the English CCNA source.
  - Keep Russian and English article filenames mirrored.
  - Follow `ARTICLE_GUIDE.md` for new articles and translations.

## Home Network Monitoring

- Continue LibreNMS and ntopng setup on VM `trafic` later.
  - LibreNMS is installed at `http://192.168.50.165:8000`.
  - ntopng is installed at `http://192.168.50.165:3000`.
  - MikroTik RB260GS / CSS106-5G-1S switch is reachable via SwOS at `http://192.168.50.250`.
  - `Port1` is renamed to `ntopng-mirror` and is used as the mirror destination port.
  - LibreNMS monitors the switch, switch ports, and mirror-port availability.
  - After adding/confirming the dedicated capture NIC, finish ntopng traffic visibility checks.
  - Keep management traffic and mirrored capture traffic on separate interfaces if possible.
