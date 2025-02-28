import sys
import os

# Add the directory containing the components module to the Python path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
from algorithms.quicksort_algorithm import quicksort
from components.building import building
from algorithms.read_input_file_algorithm import read_input_file

def look_algorithm(building):
    current_floor = 0
    direction = 1
    lift = building.get_lift()
    remaining_people = building.get_remaining_people()

    while remaining_people != 0:
        # print(f"Current floor is {current_floor}")
        # Removing people from the lift
        for i in range(len(lift.peopleList) - 1, -1, -1):
            if lift.peopleList[i] == current_floor:
                # print(f"    Removed {lift.peopleList[i]} from lift. Capacity: {lift.get_num_people()}")
                lift.remove_people(lift.peopleList[i])

        # Adding people onto the lift if capacity allows
        while lift.get_num_people() < lift.get_capacity():
            person = building.get_floor(current_floor).RemoveFromPeople()

            # Making sure the item is not added if the queue has nothing in it and returns None
            if person is None:
                break
            else:
                lift.add_people(person)
                # print(f"    Added {person} to lift. Capacity: {lift.get_num_people()}")
                    
        # Finding the next request or call (if capacity allows) in the current direction
        # Sort the requests in the elevator that are along the current direction
        # print(f"    People in lift: {lift.peopleList}, Current direction: {direction}")
        moving = True
        # When going up
        if direction == 1:

            # Find and sort all requests above the current floor from people in the lift
            next_requests = [req for req in lift.peopleList if req >= current_floor]
            next_requests = quicksort(next_requests)

            # When there is a floor above to go to
            if next_requests:
                # Select the closest request
                next_request = next_requests[0]
                # print(f"    Next floor going up: {next_request}")

                # When the capacity has not been met
                if lift.get_num_people() < lift.get_capacity():

                    # Check for calls in between the current floor and the next request
                    for i in range(current_floor, next_requests[0] + 1):
                        if building.get_floor(i).GetPeople().get_count() != 0: # When there are people on the checked floor
                            next_request = i
                            # print(f"    New call found at {next_request}")
                            break

            # When there are no requests for above floors but the capacity is not met so we can still check for calls above
            elif lift.get_num_people() < lift.get_capacity():
                next_request = None
                for i in range(current_floor, building.get_num_floors()):
                    if building.get_floor(i).GetPeople().get_count() != 0: # When the floor has people on it
                        next_request = i
                        # print(f"    New call found at {next_request}")
                        break
                if next_request is None: # If no call was found above, change direction
                    direction = -1

            # When there are no requests for above floors and the lift is at capacity so no calls can be answered
            else:
                direction = -1

        # When going down
        if direction == -1:

            # Find and sort all requests below the current floor from people in the lift
            next_requests = [req for req in lift.peopleList if req <= current_floor]
            next_requests = quicksort(next_requests)

            # When there is a floor below to go to
            if next_requests:
                # Select the closest request
                next_request = next_requests[-1]
                # print(f"    Next floor going down: {next_request}")

                # When the capacity has not been met
                if lift.get_num_people() < lift.get_capacity():

                    # Check for calls in between the current floor and the next request
                    for i in range(current_floor, next_requests[-1], -1):
                        # print(i)
                        if building.get_floor(i).GetPeople().get_count() != 0: # When there are people on the checked floor
                            next_request = i
                            # print(f"    New call found at {next_request}")
                            break

            # When there are no requests for below floors but the capacity is not met so we can still check for calls below
            elif lift.get_num_people() < lift.get_capacity():
                next_request = None
                for i in range(current_floor, -1, -1):
                    if building.get_floor(i).GetPeople().get_count() != 0: # When there are people on the checked floor
                        next_request = i
                        # print(f"    New call found at {next_request}")
                        break
                if next_request is None: # If no call was found below, change direction
                    direction = 1
                    moving = False # Do not move the elevator as that will make the program wait and the elevator should not be moving on this iteration
                    
            # When there are no requests for below floors and the lift is at capacity so no calls can be answered
            else:
                direction = 1
                moving = False # Do not move the elevator as that will make the program wait and the elevator should not be moving on this iteration

        # Going to that floor
        if moving:
            # time.sleep(0.2)
            current_floor = next_request
        
        remaining_people = building.get_remaining_people() # Updating the number of people left on the floors incase the loop needs to end

# Test code
if __name__ == "__main__":
    floorNim, capacity, requests = read_input_file("sources/input_files/input0.txt")
    print(f"{floorNim} {capacity} {requests}")
    testBuilding = building(floorNim, capacity, requests)
    look_algorithm(testBuilding)
    print("Everyone has reached their destinations!")
