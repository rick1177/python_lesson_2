class Factories:
    def __init__(self, name: str = "Без названия", description: str = ""):
        self.name=name
        self.description=description

    def print(self):
        return  f'''Фабрика: {self.name}; Описание: {self.description}'''


class Units:
    def __init__(self, name: str = "Без названия", factoryId: int = 0):
        self.name=name
        if isinstance(factoryId, int) and factoryId>0:
            self.factoryId=factoryId
        else:
            self.factoryId = 0
    def print(self):
        return  f'''Продукт: {self.name}; Номер фабрики: {self.factoryId}'''

class Tanks:
    def __init__(self,
                 name: str = "Без названия",
                 volume: int = 0,
                 maxVolume: int = 0,
                 unitId: int = 0):

        self.name=name

        if isinstance(volume, int) and volume>0:
            self.volume=volume
        else:
            self.volume = 0

        if isinstance(maxVolume, int) and maxVolume>0:
            self.maxVolume=maxVolume
        else:
            self.maxVolume = 0

        if isinstance(unitId, int) and unitId > 0:
            self.unitId = unitId
        else:
            self.factoryId = 0

    def print(self):
        s=  f'Цистерна: {self.name}; ' \
            f'Емкость: {self.volume}; ' \
            f'Макссимальная ёмкость: {self.maxVolume}; ' \
            f' Номер продукта {self.unitId}'

        return  s