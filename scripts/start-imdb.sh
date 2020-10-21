#!/bin/bash

NAME="fynd-imdb"
PROJECT_SRC="/opt/projects/fynd-imdb/apps/fynd-imdb/src"
LOGFILE="/opt/projects/fynd-imdb/data/logs/gunicorn/gunicorn.log"

USER=$(whoami)
GROUP=$(id -g -n)
if [[ "$OSTYPE" == "linux-gnu" ]]; then
  NUM_WORKERS=$((2 * $(cat /proc/cpuinfo | grep 'core id' | wc -l) + 1))
elif [[ "$OSTYPE" == "darwin"* ]]; then
  NUM_WORKERS=3
fi

NUM_THREADS=$((2 * $NUM_WORKERS))

WSGI_MODULE=config.wsgi

cd $PROJECT_SRC || exit

source /opt/projects/fynd-imdb/runtime-environments/fynd/bin/activate
export PYTHONPATH="$PYTHONPATH:$PROJECT_SRC"

source /opt/projects/fynd-imdb/apps/fynd-imdb/.env

echo "Starting $NAME with $NUM_WORKERS workers and $NUM_THREADS threads!"

exec gunicorn ${WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=0.0.0.0:9000 \
  --log-level=info \
  --reload \
  --timeout 300 \
  --log-file=$LOGFILE \
  --threads=$NUM_THREADS \
  --worker-class=gthread

