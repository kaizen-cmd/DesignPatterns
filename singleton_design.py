class SingleTonDecorator:

    def __init__(self, clss):
        self.clss = clss
        self.instance = None

    def __call__(self, *args, **kwargs):
        print(self.instance)
        if self.instance == None:
            self.instance = self.clss(*args, **kwargs)
        return self.instance


# Normal single Ton
class President:

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


o = President("Obama")

p = President("Trump")

q = President("Biden")

print(o, p, q)

print(o.name)
print(p.name)
print(q.name)


# SignleTon using decorator

@SingleTonDecorator
class President:

    def __init__(self, name):
        self.name = name


o = President("Obama")

p = President("Trump")

q = President("Biden")

print(o.name)
print(p.name)
print(q.name)
