import os
from dotenv import load_dotenv

load_dotenv(os.path.abspath(".env"))


class BaseConfig:
    """
    BaseConfig class contains basic configuration
    required for the application
    """

    FLASK_ENV = "development"
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")


class DevConfig(BaseConfig):
    """
    DevConfig class contains configuration
    required for the application in development
    phase
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DB_URI")


class ProdConfig(BaseConfig):
    """
    ProdConfig class contains configuration
    required for the application in production
    phase
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DB_URI")
