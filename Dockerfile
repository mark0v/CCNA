FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python scripts/sync_docs.py
RUN mkdocs build --strict

FROM nginx:1.27-alpine

COPY --from=builder /app/site /usr/share/nginx/html

EXPOSE 80
