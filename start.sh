#!/bin/bash
export COMPRESS=$1
exec gunicorn -w 4 -b 0.0.0.0:5000 --worker-class=gevent --worker-connections=200 app:app