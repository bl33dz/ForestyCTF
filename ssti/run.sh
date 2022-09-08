#!/bin/sh
su -c 'cd app; python app.py' app &
su -c 'cd app2; python app.py' app2 &

wait -n

exit $?
