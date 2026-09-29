from pathlib import Path
import logging 

from booking_pipeline.config import settings

def setup_logging() -> None: 
    logger = logging.getLogger()

    if logger.handlers: # nếu trong list có thì ta sẽ chặn 
        return 
    logger.setLevel(logging.DEBUG)

   
    console_handler = logging.StreamHandler()
    console_handler.setLevel(settings.log_level)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler.setFormatter(formatter)

    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)   

    file_handler = logging.FileHandler(log_dir / "pipeline.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler) 
