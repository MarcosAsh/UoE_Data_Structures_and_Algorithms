# building components

from components.floor import *
from components.lift import *

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
        self.__numPeople = self.__getTotalPeople()

    def __getTotalPeople(self) -> int:
        '''
        Returns the total number of people
        '''
        numPeople = 0
        for floor in self.__requests:
            numPeople += len(floor)
        return numPeople
    
    def getRemainingPeople(self) -> int:
        '''
        Iterates through each floor and totals up the number of people remaining
        '''
        numPeople = 0
        for i in range(len(self.__floors)):
            f = self.getFloor(i)
            numPeople += f.GetNumPeople()
        return numPeople
    

    def __createPeople(self) -> None:
         '''
         Creates people and distributes them to their floors.
         '''
         # iterate over the indices of self.__requests
         for i in range(len(self.__requests)):
             currentFloor = self.getFloor(i)
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
        '''
        Returns a floor instance given its index.
        '''
        return self.__floors[i]

    def getLift(self):
        '''
        Returns the lift
        '''
        return self.__lift