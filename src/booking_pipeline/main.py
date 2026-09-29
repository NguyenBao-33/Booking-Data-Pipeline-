import logging

from booking_pipeline.config import settings
from booking_pipeline.logging_config import setup_logging

logger = logging.getLogger(__name__)


def main() -> None:
    setup_logging()
    logger.info("Pipeline started | env=%s", settings.environment)
    logger.info("Pipeline finished")


if __name__ == "__main__":
    main()