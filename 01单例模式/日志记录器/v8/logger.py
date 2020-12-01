class Logger(object):
    class __Logger:
        def __init__(self, filename):
            self.filename = filename

        def __str__(self):
            return "{0!r} {1}".format(self, self.filename)

        def _write_log(self, level, msg):
            with open(self.filename, "a") as log_file:
                log_file.write("[{0}] {1}\n".format(level, msg))

        def critical(self, msg):
            self._write_log("CRITICAL", msg)

        def error(self, msg):
            self._write_log("ERROR", msg)

        def warn(self, msg):
            self._write_log("WARN", msg)

        def info(self, msg):
            self._write_log("INFO", msg)

        def debug(self, msg):
            self._write_log("DEBUG", msg)

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = cls.__Logger(*args, **kwargs)
        return cls.instance

    def __init__(self, filename):
        self.filename = filename

    # def __getattr__(self, name):
    #     return getattr(self.instance, name)
    #
    # def __setattr__(self, key, value):
    #     return setattr(self.instance, key, value)


