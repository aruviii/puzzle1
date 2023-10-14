import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

log_file = "core/static/logs/test_log.txt"
file_handler = logging.FileHandler(log_file)

formatter = logging.Formatter("%(asctime)s$ [%(levelname)s]$ %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
