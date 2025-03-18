from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    DB_HOST: str = 'http://localhost:8529'
    DB_USERNAME: str = 'root'
    DB_PASSWORD: str = 'root_passwd'
    DB_DATABASE: str = 'tuw'

    model_config = SettingsConfigDict(env_file='.env')


config = Config()
