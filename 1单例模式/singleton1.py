def singleton(cls):
    _instance = {}

    def wrapper(*args, **kwargs):
        if _instance.get("cls") is None:
            _instance["cls"] = cls(*args, **kwargs)
        return _instance["cls"]
    return wrapper


def singleton2(cls):
    _instance = {}

    def wrapper(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrapper


@singleton
class Logger:
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return "{0!r} {1}".format(self, self.filename)


logger1 = Logger("filename")
logger2 = Logger("filename2")
print(logger1)
print(logger2)
