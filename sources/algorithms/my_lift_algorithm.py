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
    while Building.getRemainingPeople() > 0:
        # Get the current floor of the lift
        current_floor = Lift.get_current_floor()
        # Get the list of people on the current floor
        people = Building.getFloor(current_floor).GetPeople()
        # Get the number of people on the current floor
        num_people = Building.getFloor(current_floor).GetNumPeople()
        # Get the direction the lift is moving
        direction = Lift.get_move()
        # Check if there are people on the current floor
        if num_people > 0:
            # Check if the lift is moving up
            if direction == 1:
                # Check if the lift is not at the top floor
                if current_floor < Building.__numOfFloors - 1:
                    # Move the lift up
                    Lift.change_current_floor(current_floor + 1)
                    print(f"Lift moving up to floor {current_floor + 1}")
                else:
                    # Move the lift down
                    Lift.move_down()
                    print(f"Lift moving down to floor {current_floor - 1}")
            # Check if the lift is moving down
            elif direction == -1:
                # Check if the lift is not at the bottom floor
                if current_floor > 0:
                    # Move the lift down
                    Lift.change_current_floor(current_floor - 1)
                    print(f"Lift moving down to floor {current_floor - 1}")
                else:
                    # Move the lift up
                    Lift.move_up()
                    print(f"Lift moving up to floor {current_floor + 1}")
        else:
            # Check if the lift is moving up
            if direction == 1:
                # Move the lift up
                Lift.change_current_floor(current_floor + 1)
                print(f"Lift moving up to floor {current_floor + 1}")
            # Check if the lift is moving down
            elif direction == -1:
                # Move the lift down
                Lift.change_current_floor(current_floor - 1)
                print(f"Lift moving down to floor {current_floor - 1}")

if __name__ == '__main__':
    mylift(Building)
    