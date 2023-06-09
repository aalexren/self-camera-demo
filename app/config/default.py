from os import environ

from pydantic import BaseSettings

class DefaultSettings(BaseSettings):
    
    ENV: str = environ.get("ENV", "local")
    PATH_PREFIX: str = environ.get("PATH_PREFIX", "/api/v1")
    APP_HOST: str = environ.get("APP_HOST", "http://127.0.0.1")
    APP_PORT: int = int(environ.get("APP_PORT", 9752))

    POSTGRES_DB: str = environ.get("POSTGRES_DB", "camera_service_db")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: int = int(environ.get("POSTGRES_PORT", 5432))
    POSTGRES_USER: str = environ.get("POSTGRES_USER", "admin")
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "admin")

    ZITADEL_HOST: str = environ.get("ZITADEL_HOST", "localhost")
    CLIENT_ISSUER: str = environ.get("CLIENT_ISSUER", f"http://{ZITADEL_HOST}:8080")
    CLIENT_ID: str = environ.get("CLIENT_ID", "217787792292380677@camera")
    CLIENT_SECRET: str = environ.get("CLIENT_SECRET", "wvCrKsc5H0TqA7ktOuoWk4CdhVzp77PfqmQ8emGYbLcTiyUD7X2DAjUUg85QbvGN")
    
    @property
    def database_settings(self) -> dict:
        return {
            "database": self.POSTGRES_DB,
            "host": self.POSTGRES_HOST,
            "port": self.POSTGRES_PORT,
            "user": self.POSTGRES_USER,
            "password": self.POSTGRES_PASSWORD,
        }
    
    @property
    def database_uri(self) -> str:
        return \
            "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}" \
            .format(**self.database_settings)
    
    @property
    def database_uri_sync(self) -> str:
        return \
            "postgresql://{user}:{password}@{host}:{port}/{database}" \
            .format(**self.database_settings)
    

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"