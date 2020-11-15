from threading import Lock


class Singleton:
    def __init__(self, name):
        self.name = name

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with Lock():
                if not hasattr(cls, "_instance"):
                    cls._instance = cls(*args, **kwargs)
        return cls._instance

    def __str__(self):
        return "{0!r} {1}".format(self, self.name)


logger = Singleton.instance("logger1")
print(logger)
logger2 = Singleton.instance("logger2")
print(logger2)

