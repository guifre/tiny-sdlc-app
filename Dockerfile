FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000 \
    DB_CONNECT_RETRIES=20 \
    DB_CONNECT_DELAY=2

WORKDIR /app

RUN adduser --disabled-password --gecos "" appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x /app/start.sh && chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["/app/start.sh"]
