import sys
import os

# Add the directory containing the components module to the Python path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from components.building import building
from read_input_file_algorithm import read_input_file


# Read the input file
num_floors, lift_capacity, requests = read_input_file('sources/input_files/input0.txt')
# Create a building object
Building = building(num_floors, lift_capacity, requests)

# Algorithm that moves the lift to the next closest request and can move up or down
def mylift(Building):
    Lift = Building.get_lift()
    remaining_people = Building.get_remaining_people()
    num_floors = Building.get_num_floors() 

    seek_sequence = []
    requests_pointer = []
    next_request_up = 0
    next_request_down = 0

    for i in range(num_floors):
        print(Building.get_floor(i - 1).GetNumPeople())
        if Building.get_floor(i).GetNumPeople() > 0:
            requests_pointer.append(1)
        else:
            requests_pointer.append(0)

    requests_pointer = []

    # Initialize requests_pointer with 0s for each floor
    for i in range(Building.get_num_floors()):
        if Building.get_floor(i).GetNumPeople() > 0:
            requests_pointer.append([1])
        else:
            requests_pointer.append([0])

    while remaining_people > 0:
        up_count = 0
        down_count = 0
        # Get the current floor of the lift
        current_floor = Lift.get_current_floor()
        # Get the next closest request
        for floor in range(current_floor, len(requests_pointer)):
            up_count += 1
            if requests_pointer[floor][0] == 1:
                next_request_up = floor
                break
        for floor in range(current_floor, -1, -1):
            down_count += 1
            if requests_pointer[floor][0] == 1:
                next_request_down = floor
                break
        
        # Move the lift to the next closest request
        if up_count < down_count:
            Lift.move_up()
            Lift.change_current_floor(next_request_up)
        else:
            Lift.move_down()
            Lift.change_current_floor(next_request_down)
        
        # add floor to seek sequence
        seek_sequence.append(Lift.get_current_floor())

        # get the vacancy of the lift
        vacancy = Lift.get_capacity() - Lift.get_num_people()

        for i in range(vacancy):
            # add people to the lift
            Lift.add_people(Building.get_floor(current_floor).peek())
            # remove people from the floor
            Building.get_floor(current_floor).RemoveFromPeople()



if __name__ == '__main__':
    mylift(Building)
    