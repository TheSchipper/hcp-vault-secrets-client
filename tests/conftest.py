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
        "simple": {"()": "json_log_formatter.JSONFormatter"},
        "detailed": {"()": "json_log_formatter.VerboseJSONFormatter"},
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
            "level": "INFO",
            "formatter": "simple",
            "filename": "logs/unit_test.log",
        },
        "log_file_detailed": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "filename": "logs/unit_test_detailed.log",
        },
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["stderr", "stdout", "log_file", "log_file_detailed"],
        },
    },
}


def pytest_configure(config):
    """Pytest configuration hook."""
    logging.config.dictConfig(LOGGING_CONFIG)
    pytest.logger = logging.getLogger()
    pytest.logger.debug(config)
