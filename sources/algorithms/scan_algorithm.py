import time
from stack import Stack
from components.building import building

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def scan_algorithm_real_time(requests, head, lift, one_floor_moving_time,maxFloor):
    """
    requests: List of requested floors.
    head: Current floor of the lift.
    lift: Lift object that handles the movement.
    one_floor_moving_time: Time to move one floor.
    return: Tuple containing the total seek operations and the sequence of visited floors.
    """

    seek_count = 0
    seek_sequence = []
    left = []
    right = []
    
    direction = lift.get_move()  # Initial direction of movement (1 for up, -1 for down)
    
    # Flatten requests into a single list
    request_queue = []
    for req in requests:
        if isinstance(req, list):
            request_queue.extend(req)
        else:
            request_queue.append(req)

    for req in request_queue:
        if req < head:
            left.append(req)
        elif req > head:
            right.append(req)

    # Sort each half
    left = quicksort(left)[::-1]  # down
    right = quicksort(right)       # up

    while left or right:
        if direction == 1 and right:  # Going up
            while right:
                next_floor = right.pop(0)
                if next_floor not in seek_sequence:
                    seek_sequence.append(next_floor)
                    seek_count += abs(head - next_floor)
                    head = next_floor
            direction = -1  # Change direction to down after reaching the highest request

        elif direction == -1 and left:  # Going down
            while left:
                next_floor = left.pop(0)
                if next_floor not in seek_sequence:
                    seek_sequence.append(next_floor)
                    seek_count += abs(head - next_floor)
                    head = next_floor
            direction = 1  # Change direction to UP after reaching the lowest request
        
        else:
            direction *= -1

        # Simulate lift movement time between floors
        time.sleep(one_floor_moving_time)

    return seek_count, seek_sequence