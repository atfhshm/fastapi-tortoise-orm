from pydantic_settings import BaseSettings
from os import urandom


class Settings(BaseSettings):
    db_schema: str = "postgresql"
    db_user: str = "postgres"
    db_password: str = "123456789"
    db_host: str = "127.0.0.1"
    db_port: int = 5432
    db_name: str = "postgres"
    secret_key: str = urandom(40).hex()
    hashing_algorithm: str = "HS256"
    access_token_expiry_minutes: int = 15
    refresh_token_expiry_minutes: int = 30 * 24 * 60


settings = Settings()
