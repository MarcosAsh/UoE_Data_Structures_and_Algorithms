# building components

from floor import *
from person import *
from lift import *

class building:
    def __init__(self,floorsNum,capacity,requests):
        '''
        Creates building. (int floorsNum, 2dArray requests)
        '''
        self.__numOfFloors = floorsNum
        self.__requests = requests
        self.__people = []
        self.__floors = []
        self.__capacity = capacity
        self.__lift = lift(0, False, 1, self.__capacity)
        self.__createFloors()
        self.__createPeople()

    def __createPeople(self) -> None:
        '''
        Creates people and distributes them to their floors.
        '''
        for i in self.__requests:
            currentFloor = self.GetFloor(i)
            for j in self.__requests[i]:
                newPerson = Person(j)
                self.__people.append(newPerson)
                currentFloor.AddToPeople(newPerson)

    def __createFloors(self) -> None:
        '''
        Creates the floors and adds to the floors list.
        '''
        for i in range(self.__numOfFloors):
            self.__floors.append(Floor(i))

    def getLift(self):
        return self.__lift