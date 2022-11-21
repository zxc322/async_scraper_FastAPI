from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")

RABBITMQ_DEFAULT_USER = config("RABBITMQ_DEFAULT_USER", cast=str, default="")
RABBITMQ_DEFAULT_PASS = config("RABBITMQ_DEFAULT_PASS", cast=str, default="")