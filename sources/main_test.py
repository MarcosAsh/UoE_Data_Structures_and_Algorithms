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


# main loop
def main_loop():
    """Main loop for the simulation."""
    # Get the requests for the current floor
    for req in requests[Lift.get_current_floor()]:
        # Add the people to the lift
        Lift.add_people(req)
        # Clear the requests list of people that have been added to the lift
        requests[Lift.get_current_floor()] = []
        
    # Get seek count and seek sequence
    seek_count, seek_sequence = scan_algorithm_real_time(Lift.peopleList, Lift.get_current_floor(), Lift, 0.1)
    print('current floor:', Lift.get_current_floor())
    print('seek count:', seek_count)
    print('seek sequence:', seek_sequence)
    print('requests in lift:', Lift.peopleList)


    # ensures the lift is within bounds
    for floor in seek_sequence:
        # get current floor
        Lift.change_current_floor(floor)
        # If the lift can move up
        if Lift.get_current_floor() < floor:
            # Lift starts by moving up
            Lift.move_up()
            #  check if there are people that want to get off on the floor
            for person in Lift.peopleList:
                if person == Lift.get_current_floor():
                    # remove the person from the current jobs list and remove the person from the lift
                    Lift.remove_people(person)
        
            # If there are no requests on the current floor, continue to the next floor
            if len(requests[Lift.get_current_floor()]) == 0:
                continue
            # Check how much space is in the lift
            vacancy = lift_capacity - Lift.get_num_people()

            # If the lift is full, only add the amount of people that can fit in the lift
            if vacancy < len(requests[Lift.get_current_floor()]):
                for req in range(vacancy):
                    # adds each person and there request to the lift
                    Lift.add_people(requests[Lift.get_current_floor()][req])
                # removes the people that were added to the lift from the requests list
                requests[Lift.get_current_floor()] = requests[Lift.get_current_floor()][vacancy:]

            # If the lift is not full, add all the requests to the lift
            else:
                for req in requests[Lift.get_current_floor()]:
                    Lift.peopleList.append(req)
                    Lift.add_people(req)
                # Clear the requests list of people that have been added to the lift
                requests[Lift.get_current_floor()] = []

            # Get seek count and seek sequence   
            seek_count, seek_sequence = scan_algorithm_real_time(Lift.peopleList, Lift.get_current_floor(), Lift, 0.1)
            print('current floor:', Lift.get_current_floor())
            print('seek count:', seek_count)
            print('seek sequence:', seek_sequence)
            # Move the lift to the next floor
            # Lift.change_current_floor(Lift.get_current_floor() + 1)



main_loop()