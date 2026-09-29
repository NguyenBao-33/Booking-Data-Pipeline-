from dataclasses import dataclass 
VALID_LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")

@dataclass(frozen=True)
class Settings:
    app_name: str = "booking-data-pipeline"
    environment: str = "local"
    log_level: str = "INFO"

    def __post_init__(self) -> None:
        if self.log_level not in VALID_LOG_LEVELS:
            raise ValueError(
                f"Invalid log_level: {self.log_level!r}. "
                f"Expected one of: {', '.join(VALID_LOG_LEVELS)}"
            )


settings = Settings()

