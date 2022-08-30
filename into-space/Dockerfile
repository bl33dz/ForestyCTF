FROM alpine:3.16

WORKDIR /var/www/html

RUN apk add --no-cache \
  curl \
  nginx \
  php81 \
  php81-ctype \
  php81-curl \
  php81-dom \
  php81-fpm \
  php81-gd \
  php81-intl \
  php81-mbstring \
  php81-mysqli \
  php81-opcache \
  php81-openssl \
  php81-phar \
  php81-session \
  php81-xml \
  php81-xmlreader \
  php81-zlib \
  supervisor

# Create symlink so programs depending on `php` still function
RUN ln -s /usr/bin/php81 /usr/bin/php

# Configure nginx
COPY conf/nginx.conf /etc/nginx/nginx.conf

# Configure PHP-FPM
COPY conf/fpm-pool.conf /etc/php81/php-fpm.d/www.conf
COPY conf/php.ini /etc/php81/conf.d/custom.ini

# Configure supervisord
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY flag.txt /flag.txt

COPY src/ /var/www/html/

RUN addgroup nobody ping

RUN chown -R nobody.nobody /run /var/lib/nginx /var/log/nginx

RUN mkdir /var/www/html/space && \
    chmod -R 777 /var/www/html/space && \
    mv /var/www/html/space.gif /var/www/html/space/space.gif && \
    mv /flag.txt /flag-$(cat /proc/sys/kernel/random/uuid).txt

USER nobody

EXPOSE 8080

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
