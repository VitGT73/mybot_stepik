import sys
import logging
import logging.config
import structlog

CONSOLE_HANDLER: str = "console"
CONSOLE_FORMATTER: str = "console_formatter"

JSONFORMAT_HANDLER: str = "jsonformat"
JSONFORMAT_FORMATTER: str = "jsonformat_formatter"


class SetupLogging:
    def __str__(self) -> str:
        return f'<{__class__.__name__} dev:{sys.stderr.isatty()}>'

    def __repr__(self):
        return self.__str__()

    @property
    def renderer(self) -> str:
        '''
        JSONFORMAT is automatically enabled in Docker
        '''
        if sys.stderr.isatty():
            return CONSOLE_HANDLER
        return JSONFORMAT_HANDLER

    @property
    def timestamper(self) -> structlog.processors.TimeStamper:
        return structlog.processors.TimeStamper(
            fmt="%Y-%m-%d %H:%M:%S"
        )

    def preprocessors(self, addit=False) -> list[any]:
        preprocessors = [
            self.timestamper,
            structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.StackInfoRenderer(),
        ]
        if addit:
            preprocessors = [
                                structlog.contextvars.merge_contextvars,
                                structlog.stdlib.filter_by_level,
                            ] + preprocessors + [
                                structlog.stdlib.PositionalArgumentsFormatter(),
                                structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
                            ]
        return preprocessors

    def initStructlog(self):
        logging.config.dictConfig(
            {
                "version": 1,
                "disable_existing_loggers": False,
                "formatters": {
                    JSONFORMAT_FORMATTER: {
                        "()": structlog.stdlib.ProcessorFormatter,
                        "processor": structlog.processors.JSONRenderer(),
                        "foreign_pre_chain": self.preprocessors()
                    },
                    CONSOLE_FORMATTER: {
                        "()": structlog.stdlib.ProcessorFormatter,
                        "processor": structlog.dev.ConsoleRenderer(),
                        "foreign_pre_chain": self.preprocessors()
                    },
                },
                "handlers": {
                    CONSOLE_HANDLER: {
                        "class": "logging.StreamHandler",
                        "formatter": CONSOLE_FORMATTER,
                    },
                    JSONFORMAT_HANDLER: {
                        "class": "logging.StreamHandler",
                        "formatter": JSONFORMAT_FORMATTER,
                    },
                },
                "loggers": {
                    "": {
                        "handlers": [self.renderer],
                        "level": "DEBUG",
                        "propagate": True,
                    },
                }
            }
        )

        structlog.configure(
            processors=self.preprocessors(True),
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )