import logging

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S"
    )
)

logger = logging.getLogger("dnsserver")
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


def set_log_level(level):
    logger.setLevel(getattr(logging, level.upper()))
    handler.setLevel(getattr(logging, level.upper()))
