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
