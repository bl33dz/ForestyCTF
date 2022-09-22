FROM python:3.9-alpine

WORKDIR /app

RUN apk add --no-cache bash socat

COPY app.py flag.txt /app/

RUN chmod 0644 /app/flag.txt && \
    mv /app/flag.txt /flag-$(cat /proc/sys/kernel/random/uuid)

EXPOSE 3000

CMD socat TCP-LISTEN:3000,reuseaddr,fork EXEC:"python app.py",su=nobody,stderr
