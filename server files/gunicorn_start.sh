#!/bin/sh

NAME='wey'
DJANGODIR=/webapps/wey/wey_backend
SOCKFILE=/webapps/wey/run/gunicorn.sock
USER=weyuser
GROUP=webapps
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=wey_backend.settingsprod
DJANGO_WSGI_MODULE=wey_backend.wsgi
TIMEOUT=120

cd $DJANGODIR
source ../env/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec ../env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--timeout $TIMEOUT \
--user=$USER --group=$GROUP \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=-