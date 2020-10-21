PROJECT_SRC="/opt/projects/fynd-imdb/apps/fynd-imdb/src"
NODE_SAAS_CHOKIDAR_BINARY="/opt/projects/fynd-imdb/apps/fynd-imdb/node_modules/.bin/node-sass-chokidar"

source /opt/projects/fynd-imdb/runtime-environments/fynd/bin/activate

export PYTHONPATH="$PYTHONPATH:$PROJECT_SRC"

rm -rf /opt/projects/fynd-imdb/apps/fynd-imdb/public

$NODE_SAAS_CHOKIDAR_BINARY $PROJECT_SRC/static/assets/custom/assets/sass -o $PROJECT_SRC/static/assets/custom/assets/css

cd $PROJECT_SRC || exit

python manage.py collectstatic --no-input
