import logging
from logging.config import dictConfig
import logging.config
import newrelic
from pythonjsonlogger import jsonlogger
from newrelic.agent import NewRelicContextFormatter
class CustomFormatter(NewRelicContextFormatter):
    def format(self, record):
        record.service_name = "MyApiApp"
        return super().format(record)


# Custom log filter to add New Relic metadata
class NewRelicLogFilter(logging.Filter):
    def filter(self, record):
        # Add New Relic metadata to the log record
        nr_metadata = newrelic.agent.get_linking_metadata()
        for key, value in nr_metadata.items():
            setattr(record, key, value)
        return True

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'newRelicLogFilter': {
            '()': NewRelicLogFilter
        }
    },
    'formatters': {
        'console': {
            'class': 'utils.logging.CustomFormatter',
            'format': '%(asctime)s %(name)s %(threadName)s %(levelname)s %(message)s %(process)s %(thread)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'filters': ['newRelicLogFilter']
        },
    },

    'loggers': {
        'root': {
            'handlers': ['console'], 
            'level': 'INFO'
        },
        "uvicorn": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "uvicorn.access": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "uvicorn.error": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)