import sys
import os
import tkinter as tk
import time
import threading

# Ensure the sources directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Components")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "algorithms")))

from components.lift import lift
from components.building import building
from components.floor import Floor
from algorithms.scan_algorithm import scan_algorithm_real_time


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
                num_floors, lift_capacity = map(int, line.split(","))
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


def mainloop():
    Lift = building.getLift()
     # While the lift is not at the top floor
    while building.getLift().get_current_floor() < max_floors:
        total_seek, sequence = scan_algorithm_real_time(requests, Lift.get_current_floor(), Lift.get_move(), max_floors)
        print(f"Total seek operations: {total_seek}")
        print("Seek sequence:", sequence)
        # For each floor in the sequence
        for floor in sequence:
            # For each person on the current floor
            for person in requests[floor]:
                # Add the person to the lift
                Lift.add_people()

if __name__ == "__main__":
    mainloop()