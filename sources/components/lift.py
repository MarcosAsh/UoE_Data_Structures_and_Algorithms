#lift components

class lift:
    def __init__(self, current_floor, moving, direction, capacity):
        self.__current_floor = current_floor
        self.__moving = moving
        self.__direction = direction
        self.__capacity = capacity
        self.__num_people = 0
        self.peopleList = []

    def move_up(self) -> None:
        '''
        set lift to move up, direction = 1
        '''
        self.__moving = True
        self.__direction = 1

    def move_down(self) -> None:
        '''
        set lift to move down, direction = -1
        '''
        self.__moving = True
        self.__direction = -1
    
    def get_move(self) -> int:
        '''
        returns move direction, 1 / -1
        '''
        return self.__direction

    def stop(self) -> None:
        '''
        set lift moving to False
        '''
        self.__moving = False

    def state(self) -> bool:
        '''
        returns the state of the lift, True if moving, False if not
        '''
        return self.__moving

    def change_current_floor(self, floor) -> None:
        '''
        change the current floor of the lift
        '''
        self.__current_floor = floor
    
    def get_current_floor(self) -> int:
        '''
        return the current floor of the lift
        '''
        return self.__current_floor
    
    def add_people(self,request) -> None:
        '''
        add a person to the lift + 1
        '''
        self.__capacity += 1
        self.peopleList.append(request)
        self.__num_people += 1
    
    def remove_people(self,request) -> None:
        '''
        remove a person from the lift - 1
        '''
        self.__capacity -= 1
        self.peopleList.remove(request)
        self.__num_people -= 1
    

    def get_num_people(self) -> int:
        '''
        return the number of people in the lift
        '''
        return self.__num_people

    def __str__(self) -> str:
        return self.name