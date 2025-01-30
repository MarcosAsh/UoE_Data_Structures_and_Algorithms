#lift components

class lift:
    def __init__(self, current_floor, doors_open, moving, direction, capacity):
        self.current_floor = current_floor
        self.doors_open = doors_open
        self.moving = moving
        self.direction = direction

    def move_up(self):
        self.moving = True
        self.direction = 1

    # set the lift to move down
    def move_down(self):
        self.moving = True
        self.direction = -1
    
    # get the direction the lift is moving
    def get_move(self):
        return self.direction

    # stop the lift
    def stop(self):
        self.moving = False

    # update the current floor of the lift
    def change_current_floor(self, floor):
        self.current_floor = floor
    
    def add_capacity(self):
        self.capacity += 1

    # get capacity of the lift
    def get_capacity(self):
        return self.capacity

    def __str__(self):
        return self.name