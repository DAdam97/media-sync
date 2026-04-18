import os
from dataclasses import dataclass, field


@dataclass
class Settings:
    media_path: str = field(default_factory=lambda: os.environ.get("MEDIA_PATH", "/mnt/media"))
    database_path: str = field(
        default_factory=lambda: os.environ.get("DATABASE_PATH", "/mnt/media/metadata.db")
    )
    api_key: str = field(default_factory=lambda: os.environ.get("API_KEY", ""))
    models_path: str = field(default_factory=lambda: os.environ.get("MODELS_PATH", "/app/models"))


settings = Settings()
