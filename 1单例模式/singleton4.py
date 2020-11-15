from threading import Lock


class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with Lock():
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Logger(metaclass=SingletonType):
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return "{0!r} {1}".format(self, self.filename)


logger1 = Logger("filename1")
print(logger1)
logger2 = Logger("filename2")
print(logger2)
