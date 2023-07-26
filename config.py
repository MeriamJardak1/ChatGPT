
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
