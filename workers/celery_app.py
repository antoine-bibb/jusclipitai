from celery import Celery

app = Celery('jusclipit', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')
app.conf.task_routes = {'workers.tasks.*': {'queue': 'video'}}
