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
    Lift = Building.get_lift()
    remaining_people = Building.get_remaining_people()
    print(remaining_people)
    num_floors = Building.get_num_floors() 

    requests_pointer = []

    for i in range(num_floors):
        print(Building.get_floor(i).GetNumPeople())
        if Building.get_floor(i).GetNumPeople() > 0:
            requests_pointer.append(1)
        else:
            requests_pointer.append(0)
            
    while remaining_people > 0:
        # Get the current floor of the lift
        current_floor = Lift.get_current_floor()
        # Get the next closest request  
        print(requests_pointer)


if __name__ == '__main__':
    mylift(Building)
    