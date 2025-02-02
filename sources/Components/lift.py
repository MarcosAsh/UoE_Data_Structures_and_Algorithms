#lift components

class lift:
    def __init__(self, current_floor, doors_open, moving, direction, capacity):
        self.current_floor = current_floor
        self.doors_open = doors_open
        self.moving = moving
        self.direction = direction
        self.capacity = capacity

    def move_up(self) -> None:
        '''
        set lift to move up, direction = 1
        '''
        self.moving = True
        self.direction = 1

    def move_down(self) -> None:
        '''
        set lift to move down, direction = -1
        '''
        self.moving = True
        self.direction = -1
    
    def get_move(self) -> int:
        '''
        returns move direction, 1 / -1
        '''
        return self.direction

    def stop(self) -> None:
        '''
        set lift moving to False
        '''
        self.moving = False

    def state(self) -> bool:
        '''
        returns the state of the lift, True if moving, False if not
        '''
        return self.moving

    def change_current_floor(self, floor) -> None:
        '''
        change the current floor of the lift
        '''
        self.current_floor = floor
    
    def add_capacity(self) -> None:
        '''
        add a person to the lift capcity + 1
        '''
        self.capacity += 1

    def get_capacity(self) -> int:
        '''
        return the capacity of the lift
        '''
        return self.capacity

    def __str__(self) -> str:
        return self.name