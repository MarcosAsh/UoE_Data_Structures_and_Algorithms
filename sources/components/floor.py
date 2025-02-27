class floor:
    def __init__(self, ID):
        self.__people_list = []
        self.__floor_ID = ID
        self.__number_people = 0

    def AddToPeople(self, person) -> None:
        """
        Adds a person to the floor. Person representation in this context is a requested floor
        """
        self.__people_list.append(person)
        self.__number_people += 1

    def RemoveFromPeople(self, person) -> None:
        """
        Removes a target person class from the floor
        """
        self.__people_list.remove(person)
        self.__number_people -= 1

    def GetNumPeople(self) -> list:
        """
        Returns the number of people classes on the floor
        """
        self.__SetNumberOfPeople()
        return(self.__number_people)

    def GetFloorID(self) -> int:
        """
        Returns the the number of the floor
        """
        return(self.__floor_ID)

    def GetPeople(self) -> list:
        """
        Returns the list of people classes
        """
        return self.__people_list
    
    def SetPeople(self,peopleList) -> None:
        '''
        Sets people list.
        '''
        self.__people_list = peopleList
    
    def __SetNumberOfPeople(self) -> None:
        """
        Sets the number of people on the floor to the number of people classes in the list
        """
        self.__number_people = len(self.__people_list)