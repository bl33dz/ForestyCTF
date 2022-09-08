FROM mysql:8-oracle

RUN microdnf install cronie

# Copy needed files
COPY run.sh /run.sh
COPY start.sh /start.sh
COPY conf/custom.cnf /etc/mysql/conf.d/custom.cnf
COPY db.sql /docker-entrypoint-initdb.d/1-db.sql

RUN chmod +x /run.sh /start.sh

RUN echo '*/5 * * * * root /run.sh' >> /etc/crontab

CMD sh -c '/start.sh'
