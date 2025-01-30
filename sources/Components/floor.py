class Floor:
    def __init__(self, ID):
        self.__people_list = []
        self.__floor_ID = ID    
        self.__number_people = 0
    
    def AddToPeople(self, person):
        self.__people_list.append(person)
    
    def SetNumberOfPeople(self):
        self.__number_people = len(self.__people_list)

    def GetNumPeople(self):
        return(self.__number_people)

    def GetFloorID(self):
        return(self.__floor_ID)

    def GetPeople(self):
        return self.__people_list
