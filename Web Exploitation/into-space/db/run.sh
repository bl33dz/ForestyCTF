#!/bin/sh

find /var/www/html/space ! -name 'space.gif' -type f -exec rm -f {} +
mysql -u root -pjustdummypass1337 into_space < /docker-entrypoint-initdb.d/1-db.sql
