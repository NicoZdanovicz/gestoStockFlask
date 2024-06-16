class Config:
    SECRET_KEY = 'B!x8dddd'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQ_PASSWORD = ''
    MYSQL_DB = 'gestorstock'

config={
    'development': DevelopmentConfig
}