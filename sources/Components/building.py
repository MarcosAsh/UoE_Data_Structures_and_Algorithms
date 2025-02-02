# building components

from floor import *
from person import *
from lift import *

class building:
    def __init__(self,floorsNum,liftCapacity,requests,currentLocations):
        self.__numOfFloors = floorsNum
        self.__capacity = liftCapacity
        self.__requests = requests
        self.__people = []
        self.__floors = []
        self.__currentLocations = currentLocations

    def __createPeople(self) -> None:
        for i in self.__requests:
            currentFloor = self.GetFloor(i)
            for j in i:
                newPerson = Person(j)
                self.__people.append(newPerson)
                currentFloor.AddToPeople(newPerson)

    def __createFloors(self) -> None:
        for i in range(self.__numOfFloors):
            self.__floors.append(Floor(i))
    
    def __createLift(self) -> None:
        self.__lift = lift(0,False,False,1,self.__capacity)
