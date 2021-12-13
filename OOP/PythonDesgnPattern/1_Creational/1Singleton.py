class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_logger"):
            cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger

    def __init__(self):
        print("Init object")
        pass

    def __call__(self, *args, **kwargs):
        print("Call")


logger1 = Logger()
logger2 = Logger()
print(Logger)
print(logger1)
print(logger2)
print(id(logger1)==id(logger2))
