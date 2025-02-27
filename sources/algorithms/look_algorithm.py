import sys
import os

# Add the directory containing the components module to the Python path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import time
from quicksort_algorithm import quicksort
from components.building import building
from read_input_file_algorithm import read_input_file

# Quick Sort for LOOK algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def look_algorithm(building):
    current_floor = 0
    direction = 1
    lift = building.get_lift()
    print(building.get_remaining_people())
    remaining_people = building.get_remaining_people()

    while remaining_people != 0:
        for i in range(building.get_num_floors() - 1, -1, -1):
            print(f"{i}: {building.get_floor(i).GetPeople().get_count()}")

        print(f"Current floor is {current_floor}")
        # Removing people from the lift
        for i in range(len(lift.peopleList) - 1, -1, -1):
            if lift.peopleList[i] == current_floor:
                print(f"    Removed {lift.peopleList[i]} from lift. Capacity: {lift.get_num_people()}")
                lift.remove_people(lift.peopleList[i])

        # Adding people onto the lift if capacity allows
        while lift.get_num_people() < lift.get_capacity():
            person = building.get_floor(current_floor).RemoveFromPeople()

            if person is None:
                break
            else:
                lift.add_people(person)
                print(f"    Added {person} to lift. Capacity: {lift.get_num_people()}")
                    
        # Finding the next request or call (if capacity allows) in the current direction
        # Sort the requests in the elevator that are along the current direction
        print(f"    People in lift: {lift.peopleList}, Current direction: {direction}")
        moving = True
        if direction == 1:
            next_requests = [req for req in lift.peopleList if req >= current_floor]
            next_requests = quicksort(next_requests)
            if next_requests:
                # Select the closest request
                next_request = next_requests[0]
                print(f"    Next floor going up: {next_request}")
                if lift.get_num_people() < lift.get_capacity():
                    # Check for calls in between the current floor and the next request
                    for i in range(current_floor, next_requests[0] + 1):
                        if building.get_floor(i).GetPeople().get_count() != 0:
                            next_request = i
                            print(f"    New call found at {next_request}")
                            break
            elif lift.get_num_people() < lift.get_capacity():
                next_request = None
                for i in range(current_floor, building.get_num_floors()):
                    if building.get_floor(i).GetPeople().get_count() != 0:
                            next_request = i
                            print(f"    New call found at {next_request}")
                            break
                if next_request is None:
                    direction = -1
            else:
                direction = -1
        if direction == -1:
            next_requests = [req for req in lift.peopleList if req <= current_floor]
            print(next_requests)
            next_requests = quicksort(next_requests)
            if next_requests:
                # Select the closest request
                next_request = next_requests[-1]
                print(f"    Next floor going down: {next_request}")
                if lift.get_num_people() < lift.get_capacity():
                    # Check for calls in between the current floor and the next request
                    for i in range(current_floor, next_requests[-1], -1):
                        print(i)
                        if building.get_floor(i).GetPeople().get_count() != 0:
                            next_request = i
                            print(f"    New call found at {next_request}")
                            break
            elif lift.get_num_people() < lift.get_capacity():
                next_request = None
                for i in range(current_floor, -1, -1):
                    if building.get_floor(i).GetPeople().get_count() != 0:
                        next_request = i
                        print(f"    New call found at {next_request}")
                        break
                if next_request is None:
                    direction = 1
                    moving = False
            else:
                direction = 1
                moving = False

        # Going to that floor
        if moving:
            time.sleep(0.2)
            current_floor = next_request
        
        remaining_people = building.get_remaining_people()
        print(remaining_people)

# Test code
if __name__ == "__main__":
    floorNim, capacity, requests = read_input_file("sources/input_files/input0.txt")
    print(f"{floorNim} {capacity} {requests}")
    testBuilding = building(floorNim, capacity, requests)
    look_algorithm(testBuilding)
