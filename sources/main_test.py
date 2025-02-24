import sys
import os
import tkinter as tk
import time
import threading

# Ensure the sources directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "components")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "algorithms")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "input_files")))

from components.building import building
from algorithms.scan_algorithm import scan_algorithm_real_time
from algorithms.look_algorithm import look_algorithm_real_time

class InvalidInputError(Exception):
    """Exception raised for invalid input."""
    def __init__(self, message="Invalid input provided"):
        super().__init__(message)

def read_input_file(filename):
    """Reads the input file and returns number of floors, lift capacity, and requests as a 2D array."""
    num_floors = 0
    lift_capacity = 0
    requests = []

    with open(filename, 'r') as file:
            lines = file.readlines()

            # Read number of floors and lift capacity
            for line in lines:
                line = line.strip()
                if line.startswith("#") or not line:
                    continue
                if "," in line:
                    #checks both number of floors and lift capacity are correct in the input file
                    try:
                        #ensures both are present
                        parts = line.split(",")
                        if len(parts) != 2 or not parts[0].strip():  
                            raise InvalidInputError("Invalid input provided. Line 2 in inputFile.")
                        num_floors, lift_capacity = map(int, line.split(","))
                    #ensures both are integers
                    except(ValueError):
                        raise InvalidInputError(message="Invalid input provided. Line 2 in input file, non-integer value.")
                    requests = [[] for _ in range(num_floors)]  # Initialize a 2D array
                    break

            # Read floor requests
            for line in lines:
                line = line.strip()
                if line.startswith("#") or not line:
                    continue
                if ":" in line:
                    floor, destinations = line.split(":")
                    floor = int(floor.strip()) - 1  # Convert floor to 0-based index
                    if destinations.strip():
                        requests[floor] = list(map(int, destinations.split(",")))
    return num_floors, lift_capacity, requests

# Assign variables from input file
max_floors, lift_capacity, requests = read_input_file('sources/input_files/input0.txt')
# Reverse Requests list
requests = requests[::-1]
# Create building object
Building = building(max_floors, lift_capacity, requests)
# Create Lift object
Lift = Building.getLift()


def main_loop():
    current_requests = []
    # ensures the lift is within bounds
    while Lift.get_current_floor() < max_floors:
        # Lift starts by moving up
        Lift.move_up()
        # Check how much space is in the lift
        vacancy = lift_capacity - Lift.get_num_people()
        # A loop that only takes the requests of people that can fit in the lift
        for req in range(vacancy):
            # adds requests to an updating requests list to simulate people getting on
            current_requests.append(requests[Lift.get_current_floor()][req])
        seek_count, seek_sequence = scan_algorithm_real_time(current_requests, Lift.get_current_floor(), Lift, 0.1)
        print(seek_sequence)
            
        #     # Handle people getting on and off
        #     floor_obj = Building.getFloor(target_floor)
        #     people_waiting = floor_obj.GetPeople()
        #     for person in people_waiting[:]:  # Copy list to avoid modifying while iterating
        #         if Lift.get_num_people() < lift_capacity:
        #             Lift.add_people(person)
        #             floor_obj.RemoveFromPeople(person)
    

main_loop()