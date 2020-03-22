from app import app_flsk
from app import app_flsk, db
from app.models import User, Post

@app_flsk.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}