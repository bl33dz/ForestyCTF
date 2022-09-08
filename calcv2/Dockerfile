FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache bash socat

COPY app.py flag.txt /app/

RUN chmod 0644 /app/flag.txt && \
    mkdir /secret && \
    echo "somewhere in this diretory, goodluck!" > /secret/a-notes.txt && \
    mv /app/flag.txt /secret/ä-flag.txt

EXPOSE 3000

USER nobody

CMD socat TCP-LISTEN:3000,reuseaddr,fork EXEC:"python app.py",su=nobody,stderr
