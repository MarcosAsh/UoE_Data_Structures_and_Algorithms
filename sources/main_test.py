import sys
import os
import tkinter as tk
import time
import threading

# Ensure the sources directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Components")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "algorithms")))

# Import all other classes
from components.building import building
from algorithms.scan_algorithm import scan_algorithm_real_time
from algorithms.look_algorithm import look_algorithm_real_time


def read_input_file(filename):
    """Reads the input file and returns number of floors, lift capacity, and requests."""
    num_floors = 0
    lift_capacity = 0
    requests = {}
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        # Read number of floors and lift capacity
        for line in lines:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if "," in line:
                num_floors, lift_capacity = map(int, line.split(","))
                break
        
        # Read floor requests
        for line in lines:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if ":" in line:
                floor, destinations = line.split(":")
                floor = int(floor.strip())
                destinations = list(map(int, destinations.split(","))) if destinations.strip() else []
                requests[floor - 1] = destinations
    
    return num_floors, lift_capacity, requests

# Assign variables from input file
max_floors, lift_capacity, requests = read_input_file('sources/input.txt')
# Create building class
Building = building(max_floors, lift_capacity, requests) 


def mainloop():
    Lift = building.getLift()
     # While the lift is not at the top floor
    while building.getLift().get_current_floor() < max_floors:
        total_seek, sequence = scan_algorithm_real_time(requests, Lift.get_current_floor(), Lift.get_move(), building.__numOfFloors)
        print(f"Total seek operations: {total_seek}")
        print("Seek sequence:", sequence)
        # For each person waiting on the current floor
        for request in scan_algorithm_real_time():
            # Add the person to the lift
            Building.getLift().add_people()
            # Print the current capacity of the lift to check
            print(building.getLift().get_num_people())

if __name__ == "__main__":
    mainloop()