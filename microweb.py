import os
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
