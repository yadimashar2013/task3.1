class Buiding:  # Создайте новый класс
    def __init__(self):  # инициализатор для класса Buiding
        self.numberOfFloors = 10  # целочисленный атрибут этажности self.numberOfFloors
        self.buildingType = 'Десятиэтажка'  # строковый атрибут self.buildingType

    def __eg__(self, other):
        return self.numberOfFloors == other.buildingType


numberOfFloors = Buiding()
buildingType = Buiding()
if numberOfFloors == buildingType:  # используйте атрибут numberOfFloors и buildingType для сравнения
    print('Объекты равны')
else:
    print('Объекты нельзя сравнивать')
