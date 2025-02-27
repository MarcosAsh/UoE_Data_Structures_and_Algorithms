from data_structures.queue import queue

class floor:
    def __init__(self, ID):
        self.__people_queue = queue([],length=8)
        self.__floor_ID = ID
        self.__number_people = 0

    def AddToPeople(self, person) -> None:
        """
        Adds a person to the floor. Person representation in this context is a requested floor.
        """
        self.__people_queue.enqueue(person)
        self.__number_people += 1

    def RemoveFromPeople(self) -> int:
        """
        Dequeues a person from the floor
        """
        self.__number_people -= 1
        return self.__people_queue.dequeue()

    def GetNumPeople(self) -> int:
        """
        Returns the number of people on the floor
        """
        self.__SetNumberOfPeople()
        return(self.__number_people)

    def GetFloorID(self) -> int:
        """
        Returns the the number of the floor
        """
        return(self.__floor_ID)

    def GetPeople(self) -> queue:
        """
        Returns the list of people classes
        """
        return self.__people_queue
    
    def SetPeople(self,peopleList) -> None:
        '''
        Sets people list.
        '''
        self.__people_queue = queue(peopleList,length=8)
    
    def __SetNumberOfPeople(self) -> None:
        """
        Sets the number of people on the floor to the number of people in the list
        """
        self.__number_people = self.__people_queue.get_count()

    def peek(self) -> int:
        '''
        Returns the person at the head of the queue without removing it.
        '''
        return self.__people_queue.peek()