# services/users/project/config.py

import os

class BaseConfig:
    """Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('DATABASE_URL')

class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('DATABASE_TEST_URL')

class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('DATABASE_URL')
