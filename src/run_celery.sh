#!/bin/sh

su -m celery_user -c "celery worker -A celeryworker:celery_app"