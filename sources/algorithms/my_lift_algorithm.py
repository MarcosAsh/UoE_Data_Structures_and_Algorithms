import sys
import os

# Add the directory containing the components module to the Python path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from components.building import building
from read_input_file_algorithm import read_input_file


# Read the input file
num_floors, lift_capacity, requests = read_input_file('sources/input_files/input0.txt')
# Create a building object
Building = building(num_floors, lift_capacity, requests)

# Algorithm that moves the lift to the next closest request and can move up or down
def mylift(Building):
    Lift = Building.getLift()
    remaining_people = Building.getRemainingPeople()
    num_floors = building.__building__numOfFloors 

    all_requests = []

    for i in range(num_floors):
        all_requests.extend(building.getFloor(i).GetPeople())
        
    while remaining_people > 0:
        # Get the current floor of the lift
        current_floor = Lift.get_current_floor()
        # Get the next closest request
        print(all_requests)


if __name__ == '__main__':
    mylift(Building)
    