# building components

from floor import *
from person import *
from lift import *
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
        for i in range(self.__numOfFloors):
            self.__floors.append(Floor(i))
    
    def __createLift(self) -> None:
        self.__lift = Lift(0,False,False,1,self.__capacity)
