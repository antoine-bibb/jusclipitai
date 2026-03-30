from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    app_env: str = 'development'
    secret_key: str = 'change_me'
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 30

    database_url: str
    redis_url: str

    upload_dir: str = './uploads'
    clips_dir: str = './clips'

    ffmpeg_bin: str = 'ffmpeg'
    ffprobe_bin: str = 'ffprobe'

    stripe_secret_key: str = ''
    stripe_webhook_secret: str = ''
    stripe_price_pro: str = ''
    stripe_price_business: str = ''
    frontend_url: str = 'http://localhost:3000'


settings = Settings()  # type: ignore[call-arg]
