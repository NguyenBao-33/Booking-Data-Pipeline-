from dataclasses import dataclass 

@dataclass(frozen=True) #sau khi tạo object thì mọi thứ ko đc sửa từ bên ngoài
# nếu đề frozen=FALSE thì khi 1 component thay đổi thì mọi logic trong các component khác của pipeline cung bị đổi
class Settings:
    app_name: str = "booking-data-pipeline"
    environment: str = "local"
    log_level: str = "INFO"


settings = Settings()

