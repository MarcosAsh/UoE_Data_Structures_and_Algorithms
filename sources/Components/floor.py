class Floor:
    def __init__(self, ID):
        self.__people_list = []
        self.__floor_ID = ID
    
    def AddToPeople(self, person):
        self.__people_list.append(person)
    
    def GetFloorID(self):
        return(self.__floor_ID)

    def GetPeople(self):
        return self.__people_list