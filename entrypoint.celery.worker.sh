#!/bin/sh

celery -A Core worker -l info
