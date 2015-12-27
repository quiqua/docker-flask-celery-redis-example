
from flask import Blueprint, jsonify

from .extensions import celery
from .tasks import add


api = Blueprint("api", __name__)


@api.route("/")
def index():
    return jsonify(message="Hello World")


@api.route("/mytask")
def mytask():
    task = add.delay(4,4)
    return jsonify(id=task.id, state=task.state)


@api.route("/state/<task_id>")
def state(task_id):
    task_result = celery.AsyncResult(task_id)
    return jsonify(id=task_result.id, state=task_result.state, info=task_result.info)