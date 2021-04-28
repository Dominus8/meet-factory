from app import app
from app import db

from posts.blueprint import posts
from lending.blueprint import lending


import view


app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(lending, url_prefix='/lending')

if __name__ == '__main__':
    app.run()
