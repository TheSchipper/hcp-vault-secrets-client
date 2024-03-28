"""
pytest configuration file.
"""
import logging
import logging.config
import pytest


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {},
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%z",
        },
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": "ext://sys.stdout",
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "simple",
            "stream": "ext://sys.stderr",
        },
        "log_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "filename": "test_loggers.log",
            "maxBytes": 10000000,
            "backupCount": 10,
        },
    },
    "loggers": {
        "root": {"level": "DEBUG", "handlers": ["stderr", "stdout", "log_file"]},
    },
}


def pytest_configure(config):
    """Pytest configuration hook."""
    logging.config.dictConfig(LOGGING_CONFIG)
    pytest.logger = logging.getLogger()
    pytest.logger.debug(config)
