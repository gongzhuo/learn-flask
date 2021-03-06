import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.exmail.qq.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'true')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <zhuo.gong@lixinchuxing.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_POSTS_PER_PAGE = 20


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gongzhuo@localhost:3306/gongzhuo?charset=utf8mb4'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gongzhuo@localhost:3306/gongzhuo?charset=utf8mb4'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gongzhuo@localhost:3306/gongzhuo?charset=utf8mb4'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
