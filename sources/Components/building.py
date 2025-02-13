# building components

from floor import *
from person import *
from lift import *

class building:
    def __init__(self,floorsNum,requests):
        '''
        Creates building. (int floorsNum, int liftCapacity, 2dArray requests)
        '''
        self.__numOfFloors = floorsNum
        self.__requests = requests
        self.__people = []
        self.__floors = []

        # self.__createLift()
        self.__createFloors()
        self.__distributePeople()

    def __distributePeople(self) -> None:
        '''
        Creates people and distributes them to their floors.
        '''
        for i in self.__requests:
            for j in self.__requests[i]:
                newPerson = Person(j)
                self.__people.append(newPerson)
                self.__floors[i].AddToPeople(newPerson)

    def __createFloors(self) -> None:
        '''
        Creates the floors and adds to the floors list.
        '''
        for i in range(self.__numOfFloors):
            self.__floors.append(Floor(i))
    
    # def __createLift(self) -> None:
    #     '''
    #     Creates the lift
    #     '''
    #     self.__lift = lift(0,False,False,1,self.__capacity)