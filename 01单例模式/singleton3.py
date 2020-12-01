from threading import Lock


class Singleton:
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with Lock():
                if not hasattr(cls, "_instance"):
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __str__(self):
        return "{0!r} {1}".format(self, self.name)


logger = Singleton("filename1")
logger2 = Singleton("filename2")
print(logger)
print(logger2)
