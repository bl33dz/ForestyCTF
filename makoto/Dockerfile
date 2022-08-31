FROM python:3.9-alpine

RUN pip install python-telegram-bot Mako --no-cache-dir
RUN addgroup -S app
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app" \
    --ingroup "app" \
    --uid "1337" app
RUN chown -R root:root /app

WORKDIR /app
COPY bot.py ./bot.py
COPY flag.txt /galf.txt

USER app

CMD ["python", "bot.py"]
