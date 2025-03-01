import time
import sys
import os

# Add the directory containing the components module to the Python path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_structures.stack import Stack
from algorithms.quicksort_algorithm import quicksort
from components.building import building



def scan_algorithm(requests, head, direction, num_floors):
    """
    SCAN algorithm for elevator movement
    requests: list of floor requests
    head: current position of elevator
    direction: movement of lift 1 for up -1 for down
    num_floors: total number of floors
    return: ordered sequence of floor stops
    """
    # sort requests with quicksort
    requests = quicksort(requests)
    # initialise up and down list
    up_list = [req for req in requests if req >= head]
    down_list = [req for req in requests if req < head]

    # check direction of elevator
    if direction == 1: 
        sequence = up_list + down_list[::1]
    else: 
        sequence = down_list[::1] + up_list

    return sequence

def scan_algorithm_loop(building, update_gui_callback):
    """
    Continuously runs SCAN algorithm for the elevator simulation
    Calls update_gui_callback after every move to refresh the display
    """
    elevator = building.get_lift()
    num_floors = building.get_num_floors()
    num_times_loop_completed = 0  

    while True:
        current_floor = elevator.get_current_floor()
        direction = elevator.get_move()

        # Gather all requests
        all_requests = []
        for i in range(num_floors):
            all_requests.extend(building.get_floor(i).GetPeople().return_queue())

        if not all_requests:
            time.sleep(1)
            continue  

        # Compute SCAN sequence
        sequence = scan_algorithm(all_requests, current_floor, direction, num_floors)

        for floor in sequence:
            elevator.change_current_floor(floor)
            update_gui_callback()  
            time.sleep(1)

            # Manage people entering/exiting
            floor_obj = building.get_floor(floor)
            people_waiting = floor_obj.GetPeople().return_queue()

            for person in people_waiting[:]:
                if elevator.get_num_people() < elevator.get_capacity():
                    elevator.add_people(person)
                    floor_obj.RemoveFromPeople()

            update_gui_callback()  
            time.sleep(1)

        # Change direction
        if direction == -1:
            elevator.move_up()
        else:
            elevator.move_down()

        time.sleep(1)
        num_times_loop_completed += 1


def test_scan_algorithm_basic():
	requests = [2, 5, 8, 1, 7]
	head = 3
	direction = 1  # Moving up
	num_floors = 10
    
	sequence = scan_algorithm(requests, head, direction, num_floors)
    
	print("SCAN Algorithm Test")
	print("Initial Floor:", head)
	print("Floor Requests:", requests)
	print("Visit Sequence:")
	for floor in sequence:
          print(f"Elevator stopping at floor {floor}")
    
# Run the basic test
if __name__ == "__main__":
	test_scan_algorithm_basic()
