# building components

from components.floor import *
from components.lift import *

class building:
    def __init__(self,floorsNum,capacity,requests):
        '''
        Creates building. (int floorsNum, 2dArray requests)
        '''
        self.__num_of_floors = floorsNum
        self.__requests = requests
        self.__floors = []
        self.__capacity = capacity
        self.__lift = lift(0, False, 1, self.__capacity)
        self.__create_floors()
        self.__create_people()

        self.__num_people = 0
        for floor in self.__requests:
            self.__numPeople += len(floor)
        self.__num_people

    def get_total_people(self) -> int:
        '''
        Returns the total number of people
        '''
        return self.__num_people
    
    def get_remaining_people(self) -> int:
        '''
        Iterates through each floor and totals up the number of people remaining
        '''
        num_people = 0
        for i in range(len(self.__floors)):
            f = self.getFloor(i)
            num_people += f.GetNumPeople()
        return num_people
    

    def __create_people(self) -> None:
         '''
         Creates people and distributes them to their floors.
         '''
         # iterate over the indices of self.__requests
         for i in range(len(self.__requests)):
             currentFloor = self.get_floor(i)
             # iterate over the requests for the current floor
             for j in self.__requests[i]:
                 newPerson = j
                 currentFloor.AddToPeople(newPerson)

    def __create_floors(self) -> None:
        '''
        Creates the floors and adds to the floors list.
        '''
        for i in range(self.__num_of_floors):
            self.__floors.append(floor(i))

    def get_floor(self,i) -> floor:
        '''
        Returns a floor instance given its index.
        '''
        return self.__floors[i]

    def get_lift(self):
        '''
        Returns the lift
        '''
        return self.__lift
    
    def get_num_floors(self) -> int:
        '''
        Returns the number of floors in the building
        '''
        return self.__num_of_floors