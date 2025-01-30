# building components

from floor import *
from person import *
class building:
    def __init__(self,floorsNum,liftCapacity,requests):
        self.__numOfFloors = floorsNum
        self.__capacity = liftCapacity
        self.__requests = requests
        self.__people = []
        self.__floors = []

    def __createPeople(self) -> None:
        for i in self.__requests:
            newPerson = Person(i)
            self.__people.append(newPerson)

    def __createFloors(self) -> None:
        for i in range(numOfFloors):
            self.__floors.append(Floor(i))
    
