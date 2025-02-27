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
    lift = building.getLift()
    print(building.getRemainingPeople())
    remaining_people = building.getRemainingPeople()
    while remaining_people:
        print(f"Current floor is {current_floor}")
        # Removing people from the lift
        for person in lift.peopleList:
            if person == current_floor:
                lift.remove_people(person)
                print(f"    Removed {person} from lift. Capacity: {lift.get_num_people()}")

        # Adding people onto the lift if capacity allows
        for person in building.getFloor(current_floor).getPeople():
            if lift.add_people(person) == False:
                break
            else:
                print(f"    Added {person} to lift. Capacity: {lift.get_num_people()}")
                    
        # Finding the next request or call (if capacity allows) in the current direction
        # Sort the requests in the elevator that are along the current direction
        print(f"    People in lift: {lift.peopleList}, Current direction: {direction}")
        if direction == 1:
            next_requests = [req for req in lift.peopleList if req >= current_floor]
            next_requests = quicksort(next_requests)
            
            # Select the closest request
            next_request = next_requests[0]
            print(f"    Next floor: {next_request}")
            if not lift.get_num_people() <= lift.get_capacity():
                # Check for calls in between the current floor and the next request
                for i in range(current_floor, next_requests[0] + 1):
                    if building.getFloor(i).getPeople:
                        next_request = i
                        print(f"    New call found at {next_request}")
                        break
        if direction == -1:
            next_requests = [req for req in lift.peopleList if req <= current_floor]
            next_requests = quicksort(next_requests)
            
            # Select the closest request
            next_request = next_requests[-1]
            print(f"    Next floor: {next_request}")
            if not lift.get_num_people() <= lift.get_capacity():
                # Check for calls in between the current floor and the next request
                for i in range(next_requests[-1] + 1, current_floor, -1):
                    if building.getFloor(i).getPeople:
                        next_request = i
                        print(f"    New call found at {next_request}")
                        break

        # Going to that floor
        time.sleep(0.2)
        current_floor = next_request

# Test code
if __name__ == "__main__":
    floorNim, capacity, requests = read_input_file("sources/input_files/input0.txt")
    testBuilding = building(floorNim, capacity, requests)
    look_algorithm(testBuilding)
