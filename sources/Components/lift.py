#lift components

class lift:
    def __init__(self, num_floors, current_floor, doors_open, moving, direction):
        self.num_floors = num_floors
        self.current_floor = current_floor
        self.doors_open = doors_open
        self.moving = moving
        self.direction = direction

    def move_up(self):
        self.moving = True
        self.direction = 1

    def move_down(self):
        self.moving = True
        self.direction = -1

    def get_move(self):
        return self.direction

    def stop(self):
        self.moving = False

    def change_floor(self, floor):
        self.current_floor = floor

    def __str__(self):
        return self.name