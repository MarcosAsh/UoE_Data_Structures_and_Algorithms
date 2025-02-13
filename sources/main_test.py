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
from components.person import Person
from algorithms.scan_algorithm import scan_algorithm_real_time


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


max_floors, lift_capacity, requests = read_input_file('sources/input.txt')
print(requests, lift_capacity, max_floors)
Building = building(max_floors, requests) 
Lift = lift(1, False, 1, lift_capacity)


def mainloop():
    while Lift.get_current_floor() < max_floors: # while the lift is not at the top floor
        for waiting in requests[Lift.get_current_floor()]: # for each person waiting on the current floor
            Lift.add_capacity() # add the person to the lift
            print(Lift.get_capacity()) # print the current capacity of the lift to check

if __name__ == "__main__":
    mainloop()