class Floor:
    def __init__(self):
        self.__people_list = []
    
    def AddToPeople(self, person):
        self.__people_list.append(person)
    
    def GetPeople(self):
        return self.__people_list