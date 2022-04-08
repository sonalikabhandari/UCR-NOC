#!/bin/bash

set -ex

exec celery -A audit_processes worker -l INFO & python manage.py runserver


