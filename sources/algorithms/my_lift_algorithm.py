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

    next_requested_floor_up = None
    next_requested_floor_down = None

    while Building.get_remaining_people() > 0 or Lift.get_num_people() > 0:

        current_floor = Lift.get_current_floor()
        target_floor = None

        # If lift is not full
        if Lift.get_num_people() < lift_capacity:
            # Get the next closest request up
            # Start at floor above current, end at max floor, setting i as index/floor
            for i in range(current_floor + 1, num_floors):
                if Building.get_floor(i).GetPeople().get_count() > 0:
                    next_requested_floor_up = i
                    break
            

            # Get the next closest request down
            for i in range(current_floor -1, -1, -1):
                if Building.get_floor(i).GetPeople().get_count() > 0:
                    next_requested_floor_down = i
                    break
            
            
            # # If both dont exist
            # if next_requested_floor_down is None and next_requested_floor_up is None:
            #     # Finished
            #     pass
            # If no down
            if next_requested_floor_down is None:
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
                if Building.get_floor(next_requested_floor_up).GetPeople().get_count() < Building.get_floor(next_requested_floor_down).GetPeople().get_count():
                    target_floor = next_requested_floor_down
                else:
                    target_floor = next_requested_floor_up

        # If lift is full
        elif Lift.get_num_people() == lift_capacity or (Building.get_remaining_people() == 0 and Lift.get_num_people() > 0):
            min_distance = 999
            for request in Lift.peopleList:
                # print(request)
                if abs(request - current_floor) < min_distance or (abs(request - current_floor) == min_distance):
                    min_distance = abs(request - current_floor)
                    print('min_distance = ', min_distance, 'request = ', request)
                    target_floor = request
            

        # Check if the target floor is the current floor
        if target_floor is not None and target_floor != current_floor:
            Lift.change_current_floor(target_floor)
            print(next_requested_floor_up, next_requested_floor_down)
            print(f"Lift moving to floor {Lift.get_current_floor()}")



        # remove people from the lift if they are on the current floor
        people_to_remove = []
        for person in Lift.peopleList:
            if person == Lift.get_current_floor():
                people_to_remove.append(person)

        for person in people_to_remove:
            Lift.remove_people(person)
            print(f"Removed {person} from lift. Capacity: {Lift.get_num_people()}")
        

        # add people onto the lift if capacity allows
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
                print('People on the floor after', Building.get_floor(Lift.get_current_floor()).GetPeople().return_queue())
                # print people in the lift
                print('People in lift:', Lift.peopleList)
                # print remaining people in the building
                print('remaining people in the building: ', Building.get_remaining_people())
                print('every floor on')
                # print length of floor queue
                print('------------------------------------')
    return None
if __name__ == '__main__':
    print(my_lift(Building))
    