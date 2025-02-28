import sys
import os
"""
if lift not full:
	go to nearest floor with request
	pick up people
	repeat
if lift full:
	go to nearest floor that is requested by someone on lift
	let everyone who wants that floor off
	pick up people
"""
# Add the directory containing the components module to the Python path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from components.building import building
from read_input_file_algorithm import read_input_file


# Read the input file
num_floors, lift_capacity, requests = read_input_file('sources/input_files/input0.txt')
# Create a building object
Building = building(num_floors, lift_capacity, requests)

# Algorithm that moves the lift to the next closest request and can move up or down
def my_lift(Building):
    Lift = Building.get_lift()
    num_floors = Building.get_num_floors() 

    next_requested_floor_up = 0
    next_requested_floor_down = 0

    while Building.get_remaining_people() > 0:

        current_floor = Lift.get_current_floor()

        # If lift is not full
        if Lift.get_num_people() < lift_capacity:
            # Get the next closest request up
            # Start at floor above current, end at max floor, setting i as index/floor
            for i in range(current_floor + 1, num_floors):
                checking_floor = Building.get_floor(i)
                if checking_floor.GetNumPeople() > 0:
                    next_requested_floor_up = i
            
            if next_requested_floor_up > num_floors:
                next_requested_floor_up = None

            # Get the next closest request down
            for i in range(current_floor - 1, 0, -1):
                checking_floor = Building.get_floor(i)
                if checking_floor.GetNumPeople() > 0:
                    next_requested_floor_down = i
            
            if next_requested_floor_down < 0:
                next_requested_floor_down = None
            
            # If both dont exist
            if next_requested_floor_down is None and next_requested_floor_up is None:
                # Finished
                pass
            # If no down
            elif next_requested_floor_down is None:
                target_floor = next_requested_floor_up
            # If no up
            elif next_requested_floor_up is None:
                target_floor = next_requested_floor_down
            # If up direction is closer
            elif next_requested_floor_up - current_floor < current_floor - next_requested_floor_down:
                target_floor = next_requested_floor_up
            # Elif down is closer
            elif next_requested_floor_up - current_floor > current_floor - next_requested_floor_down:
                target_floor = next_requested_floor_down
            # Else same
            else:
                target_floor = next_requested_floor_up
        # If lift is full
        else:
            for request in Lift.peopleList:
                if request > current_floor:
                    pass
                elif request < current_floor:
                    pass
                # Same as current floor
                else:
                    pass
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
    