import logging
import sys

LOG_FORMAT = "[%(asctime)s - %(levelname)s] %(name)s: %(message)s"

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[logging.StreamHandler(sys.stdout)],
)

LOGGER = logging.getLogger("MatthewMusicBot")


def get_logger(name: str):
    return logging.getLogger(name)