# celery code to init workers inside cpu.
import time
import random

from celery import Celery
from celery.utils.log import get_task_logger
# define cluster and corresponding redis.
celery = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

celery_log = get_task_logger(__name__)
# receives str message from FastAPI
# worker task: send email.
# logs into redis
# def send_email() returns dest.
@celery.task
def send_email(email: str):
    #delay sending time to stabilize db
    time.sleep(random.randint(1, 4)) 
    celery_log.info("Email has been sent")
    return {
        "msg": f"Email has been sent to {email}",
        "details": {
            "destination": email,
        },
    }


