import os 
from dataclasses import dataclass 
from collections.abc import Callable 


VALID_LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")

@dataclass(frozen=True)
class Settings:
    app_name : str = "booking-data-pipeline"
    environment : str = "local"
    log_level : str = "INFO"

    def __post_init__(self) -> None:
        if self.log_level not in VALID_LOG_LEVELS:
            raise ValueError(
                f"Invalid log_level: {self.log_level!r}. "
                f"Expected one of: {', '.join(VALID_LOG_LEVELS)}"
            )
def get_env(key: str, transform: Callable[[str], str] | None = None) -> str | None:
    """Đọc một biến môi trường và làm sạch.

    Trả về None nếu biến không được đặt hoặc chỉ chứa khoảng trắng,
    để Settings dùng giá trị mặc định của nó.
    """
    val= os.getenv(key)
    if val is None: 
        return None 

    val= val.strip()
    if not val : 
        return None 

    return transform(val) if transform else val

def load_settings()-> Settings:
    overrides : dict [str, str] ={}

    log_level = get_env("BOOKING_LOG_LEVEL",str.upper)
    if log_level is not None:
        overrides["log_level"] = log_level

    environment = get_env("BOOKING_ENVIRONMENT", str.lower)
    if environment is not None:
        overrides["environment"] = environment

    return Settings(**overrides)


settings = load_settings()



