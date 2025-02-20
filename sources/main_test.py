import sys
import os
import tkinter as tk
import time
import threading

# Ensure the sources directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "components")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "algorithms")))

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
max_floors, lift_capacity, requests = read_input_file('sources/input.txt')
# Create building class
Building = building(max_floors, lift_capacity, requests)


def mainloop(algorithm):
    Lift = Building.getLift()
     # While the lift is not at the top floor
    while Lift.get_current_floor() < max_floors:
        total_seek, sequence = algorithm(requests, Lift.get_current_floor(), Lift.get_move(), max_floors)
        print(f"Total seek operations: {total_seek}")
        print("Seek sequence:", sequence)
        # For each floor in the sequence
        for floor in sequence:
            # For each person on the current floor
            for person in requests[floor]:
                # Add the person to the lift
                Lift.add_person()
                print(person)

if __name__ == "__main__":
    mainloop(scan_algorithm_real_time)