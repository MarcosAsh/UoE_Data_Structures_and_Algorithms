# building components

from floor import *
from lift import *

class building:
    def __init__(self,floorsNum,capacity,requests):
        '''
        Creates building. (int floorsNum, 2dArray requests)
        '''
        self.__numOfFloors = floorsNum
        self.__requests = requests
        self.__floors = []
        self.__capacity = capacity
        self.__lift = lift(0, False, 1, self.__capacity, self.__getNumPeople())
        self.__createFloors()
        self.__createPeople()

    def __getNumPeople(self):
        numPeople = 0
        for floor in self.__requests:
            numPeople += len(floor)

    def __createPeople(self) -> None:
        '''
        Creates people and distributes them to their floors.
        '''
        #gets the current floor as i
        for i in self.__requests:
            currentFloor = self.GetFloor(i)
            #gets the current request as j
            for j in self.__requests[i]:
                newPerson = j
                currentFloor.AddToPeople(newPerson)

    def __createFloors(self) -> None:
        '''
        Creates the floors and adds to the floors list.
        '''
        for i in range(self.__numOfFloors):
            self.__floors.append(Floor(i))

    def __getFloor(self,i) -> Floor:
        return self.__floors[i]

    def getLift(self):
        return self.__lift