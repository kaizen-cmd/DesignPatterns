from abc import abstractmethod, ABCMeta


class ComputerAbstract(metaclass=ABCMeta):

    @abstractmethod
    def show_info(self):
        pass


class HPComputer(ComputerAbstract):

    def show_info(self):
        print("Brand: HP")


class LGComputer(ComputerAbstract):

    def show_info(self):
        print("Brand: LG")


class SamsungComputer(ComputerAbstract):

    def show_info(self):
        print("Brand: Samsung")


class ComputerFactory:

    @classmethod
    def produce_computer(cls, name):
        eval(f"{name}Computer")().show_info()


cf = ComputerFactory()
cf.produce_computer("Samsung")
cf.produce_computer("HP")
cf.produce_computer("LG")
