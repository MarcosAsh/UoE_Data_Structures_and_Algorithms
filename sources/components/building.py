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
        self.__lift = lift(0, False, 1, self.__capacity)
        self.__createFloors()
        self.__createPeople()
        self.__numPeople = self.__getNumPeople()

    def __getNumPeople(self) -> int:
        '''
        Returns the total number of people
        '''
        numPeople = 0
        for floor in self.__requests:
            numPeople += len(floor)
        return numPeople

    def __createPeople(self) -> None:
        '''
        Creates people and distributes them to their floors.
        '''
        # iterate over the indices of self.__requests
        for i in range(len(self.__requests)):
            currentFloor = self.__getFloor(i)
            # iterate over the requests for the current floor
            for j in self.__requests[i]:
                newPerson = j
                currentFloor.AddToPeople(newPerson)

    def __createFloors(self) -> None:
        '''
        Creates the floors and adds to the floors list.
        '''
        for i in range(self.__numOfFloors):
            self.__floors.append(floor(i))

    def getFloor(self,i) -> floor:
        return self.__floors[i]

    def getLift(self):
        return self.__lift