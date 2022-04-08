#!/bin/bash

set -ex

WORKERS=${GUNICORN_WORKERS:-4}
exec gunicorn --certfile=/etc/ssl/certs/_.netops.charter.com.crt \
     --keyfile=/etc/ssl/certs/_.netops.charter.com.key \
     --access-logfile /dbAudited/log/intake-access.log \
     --error-logfile /dbAudited/log/intake-error.log \
     --pid /dbAudited/log/intake.pid \
     --timeout 60 \
     --workers $WORKERS \
     --bind 0.0.0.0:8000 \
     dbAudited.wsgi.application

