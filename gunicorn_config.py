from distutils.log import debug

bind = "0.0.0.0:8080"
workers = 1

accesslog = "-"
errorlog = "-"

capture_output = True
loglevel = "info"

timeout = 300



"""

gunicorn --worker-tmp-dir /dev/shm --config gunicorn_config.py app:app

"""