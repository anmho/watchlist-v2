import logging


class LoggerFactory:
    level = logging.DEBUG

    @classmethod
    def set_level(cls, level):
        cls.level= level

    @classmethod
    def create(cls, name):
        return logging.Logger(name, cls.level)

