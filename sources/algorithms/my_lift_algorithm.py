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
        if Building.get_floor(i).GetNumPeople() > 0:
            requests_pointer.append(1)
        else:
            requests_pointer.append(0)

    requests_pointer = []

    # Initialize requests_pointer with 0s for each floor
    for i in range(Building.get_num_floors()):
        if Building.get_floor(i).GetNumPeople() > 0:
            requests_pointer.append(1)
        else:
            requests_pointer.append(0)

    while Building.get_remaining_people() > 0:
        up_count = 0
        down_count = 0
        # Get the next closest request
        for floor in range(Lift.get_current_floor(), num_floors):
            if requests_pointer[floor] == 1:
                next_request_up = floor
                break
            up_count += 1
        for floor in range(Lift.get_current_floor(),-1, -1):
            
            if requests_pointer[floor] == 1:
                next_request_down = floor 
                break
            down_count += 1


        # Move the lift to the next closest request
        if up_count < down_count:
            Lift.move_up()
            Lift.change_current_floor(next_request_up)
            requests_pointer[next_request_up] = 0
        if down_count < up_count:
            Lift.move_down()
            Lift.change_current_floor(next_request_down)
            requests_pointer[next_request_down] = 0
        else:
            if Lift.get_move() == 1:
                Lift.change_current_floor(next_request_up)
                requests_pointer[next_request_up] = 0
            else:
                Lift.change_current_floor(next_request_down)
                requests_pointer[next_request_down] = 0

        # add floor to seek sequence
        seek_sequence.append(Lift.get_current_floor())

        # get the vacancy of the lift
        vacancy = Lift.get_capacity() - Lift.get_num_people()

        # remove people from the lift if they are on the current floor
        for person in Lift.peopleList:
            if person == Lift.get_current_floor():
                Lift.remove_people(person)

        # Adding people onto the lift if capacity allows
        while Lift.get_num_people() < Lift.get_capacity():
            person = Building.get_floor(Lift.get_current_floor()).RemoveFromPeople()
            # Making sure the item is not added if the queue has nothing in it and returns None
            if person is None:
                break
            else:
                # add people to the lift
                Lift.add_people(person)
                print(f"Added {person} to lift. Capacity: {Lift.get_num_people()}")
                # print people on the floor
                print(Building.get_floor(Lift.get_current_floor()).GetPeople())
                # print people in the lift
                print(Lift.peopleList)
                # print remaining people in the building
                print(Building.get_remaining_people())
                print(requests_pointer)
 
    return seek_sequence


if __name__ == '__main__':
    print(mylift(Building))
    