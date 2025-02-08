import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "Components")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "algorithms")))

from components.lift import lift
from components.building import building
from components.floor import Floor
from components.person import Person
from algorithms.scan_algorithm import scan_algorithm_real_time

def readInput(filename):
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
                floor_request, destinations = line.split(":")
                floor_request = int(floor_request.strip())
                destinations = list(map(int, destinations.split(","))) if destinations.strip() else []
                requests[floor_request] = destinations
    
    return num_floors, lift_capacity, requests
    
print(readInput("sources/input.txt"))