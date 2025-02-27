import time
import threading
from stack import Stack
from quicksort_algorithm import quicksort
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


def scan_algorithm_loop(building):
    """
    Continuosly runs SCAN algorithm for the elevator simulation
    building: The building instance containing the lift and floors
    """
    # initialising elevator
    elevator = building.getLift()
    # accessing the private attribute to get number of floors
    num_floors = building.__building__numOfFloors 
    # initialise variable to count how many times the loop has been completed
    num_times_loop_completed = 0
    while True:

        # get current floor and get direction from elevator
        current_floor = elevator.get_current_floor()
        direction = elevator.get_move()

        # get all requests form building floors
        all_requests = []
        for i in range(num_floors):
            all_requests.extend(building.getFloor(i).GetPeople())

        if not all_requests:
            # make algorithm sleep
            time.sleep(1)
            # if no requests keep waiting
            continue 

        # get scan sequence 
        sequence = scan_algorithm(all_requests, current_floor, direction, num_floors)

        for floor in sequence:
            # go to next floor
            elevator.change_current_floor(floor)
            # print floor that it moved to
            print(f"ELevator moved to the floor {floor}")

            # simulate people geting in and out of the elevaator
            floor_obj = building.getFloor(floor)
            people_waiting =  floor_obj.GetPeople()
            # copy list to modift safely
            for person in people_waiting[:]:
                if elevator.get_num_people() < elevator._lift__capacity:
                    elevator.add_people(person)
                    floor_obj.RemoveFromPeople(person)
            
            # simulate elevator movement
            time.sleep(1)

        # change direction at the end
        elevator.move_up() if direction == -1 else elevator.move_down()

        time.sleep(1)

        # add 1 to the number of times loop completed as loop has been iterated through once
        num_times_loop_completed += 1
        # print number of times loop completed
        print(f"number of times loop completed: {num_times_loop_completed}")