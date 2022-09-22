FROM python:3.9-alpine

RUN pip install Flask --no-cache-dir
RUN addgroup -S app
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app" \
    --ingroup "app" \
    --uid "1337" app

RUN addgroup -S app2
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app2" \
    --ingroup "app2" \
    --uid "1338" app2

COPY run.sh /run.sh

WORKDIR /app

COPY app/app.py app/flag.txt ./

RUN chown root:app app.py flag.txt && \
    chmod 0640 app.py flag.txt

EXPOSE 5001

WORKDIR /app2

COPY app2/app.py ./

RUN chown root:app2 app.py && \
    chmod 0640 app.py

EXPOSE 5000

WORKDIR /

CMD ./run.sh
