from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PC Forge Store API"
    api_prefix: str = "/api"
    db_host: str = "db"
    db_port: int = 3306
    db_user: str = "ecom_user"
    db_password: str = "ecom_pass"
    db_name: str = "ecommerce"
    secret_key: str = "supersecretkey"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24
    cors_origins: str = "http://localhost:5173,http://localhost:8080"

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()


def build_database_url() -> str:
    return (
        f"mysql+pymysql://{settings.db_user}:{settings.db_password}"
        f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
    )
