
from myapp.app import create_app
from myapp.extensions import celery as worker

flask_app = create_app()

celery_app = worker
