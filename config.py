class Config:
    SECRET_KEY = 'B!x8dddd'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD  = ''
    MYSQL_DB = 'gestorstock'

class ProductionConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'zdano.mysql.pythonanywhere-services.com'
    MYSQL_USER = ''
    MYSQL_PASSWORD  = ''
    MYSQL_DB = '$default'
    
config={
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
