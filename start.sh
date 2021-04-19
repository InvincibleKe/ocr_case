#!/bin/bash
exec gunicorn -w 4 -b 0.0.0.0:8080 --worker-class=gevent --worker-connections=200 app:app