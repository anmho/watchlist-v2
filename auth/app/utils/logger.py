import logging
from logging import CRITICAL, ERROR, WARN, INFO, DEBUG


class LoggerFactory:
    level = logging.DEBUG

    @classmethod
    def configure(cls, level) -> None:
        if level not in (CRITICAL, ERROR, WARN, INFO, DEBUG):
            raise TypeError(
                "invalid log level. must one of critical, error, warning, info, debug")

        cls.level = level

    @classmethod
    def create(cls, name):
        return logging.Logger(name, cls.level)
