class Laptop:

    def __init__(self, name):
        self.name = name

    def charge(self):
        return "charging"


class Computer:

    def __init__(self, name):
        self.name = name

    def download(self):
        return "downloading"


class DeviceAdapter:

    def __init__(self, obj, **adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


l = Laptop("dell")
l = DeviceAdapter(l, nm=l.charge)

c = Computer("HP")
c = DeviceAdapter(c, nm=c.download)

print(l.nm(), l.name)
print(c.nm(), c.name)

# GETATTR can be used to return a function to be called using strings
# eg: func = getattr(l, "charge")
# this will return the charge method of l object and can be called using func()
