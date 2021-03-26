from sys import platform


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite://///Users/ilarudy/PycharmProjects/flaskProject1/pypet.db'

    if platform == "linux" or platform == "linux2":
       SQLALCHEMY_DATABASE_URI = 'sqlite://///Users/ilarudy/PycharmProjects/flaskProject1/pypet.db'
    elif platform == "win32":
       SQLALCHEMY_DATABASE_URI = r'sqlite:///D:\git_source\meet-factory\pypet.db'

    SECRET_KEY = 'secret 12345'
    SECURITY_PASSWORD_SALT = 'kek'
    SECURITY_PASSWORD_HASH = 'sha256_crypt'

    UPLOADED_PHOTOS_DEST = 'static/image'
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    MAX_CONTENT_LENGTH = '16 * 1024 * 1024'
