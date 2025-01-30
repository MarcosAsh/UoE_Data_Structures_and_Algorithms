# building components

import floor
import person
class building:
    def __init__(self,floors,liftCapacity,requests):
        self.__numOfFloors = floors
        self.__capacity = liftCapacity
        self.__requests = requests
        self.__people = []

    def __createPeople(self) -> None:
        for i in self.__requests:
            newPerson = person.Person(i)
            self.__people.append(newPerson)
    
