
import time

from .extensions import celery



@celery.task(bind=True)
def add(self, a, b):
    x = 5

    self.update_state(state="Processing", meta="Waiting for loop")
    while x > 0:
        x = x - 1
        time.sleep(2)

    return a+b