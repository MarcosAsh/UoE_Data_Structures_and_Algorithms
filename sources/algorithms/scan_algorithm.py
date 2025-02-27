import time
import threading
from stack import Stack

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def scan_algorithm_real_time(requests, head, lift, one_floor_moving_time):
    """
    SCAN Algorithm with real-time updates.
    
    requests: List of requested floors.
    head: Current floor of the lift.
    lift: Lift object that handles movement.
    one_floor_moving_time: Time to move one floor.
    
    Returns:
        seek_count: Total movement count.
        seek_sequence: The order of floors visited.
    """
    
    seek_count = 0
    seek_sequence = []
    
    direction = lift.get_move()  # Initial direction (1 = up, -1 = down)
    
    # Flatten all requests into a single list
    request_queue = []
    for req in requests:
        if isinstance(req, list):
            request_queue.extend(req)
        else:
            request_queue.append(req)
    
    # If no requests, return early
    if not request_queue:
        return 0, []

    # Split requests into "left" (below head) and "right" (above head)
    left = sorted([req for req in request_queue if req < head], reverse=True)  # Going down
    right = sorted([req for req in request_queue if req > head])  # Going up

    while left or right:
        if direction == 1 and right:  # Moving UP
            while right:
                next_floor = right.pop(0)
                if next_floor not in seek_sequence:
                    seek_sequence.append(next_floor)
                    seek_count += abs(head - next_floor)
                    head = next_floor
            # Switch direction when the highest request is reached
            if left:
                direction = -1

        elif direction == -1 and left:  # Moving DOWN
            while left:
                next_floor = left.pop(0)
                if next_floor not in seek_sequence:
                    seek_sequence.append(next_floor)
                    seek_count += abs(head - next_floor)
                    head = next_floor
            # Switch direction when the lowest request is reached
            if right:
                direction = 1

        # Ensure the lift keeps running while requests exist
        if not left and not right:
            remaining_requests = [req for req in requests if req not in seek_sequence]
            if remaining_requests:
                left = sorted([req for req in remaining_requests if req < head], reverse=True)
                right = sorted([req for req in remaining_requests if req > head])

        # Simulate movement time
        time.sleep(one_floor_moving_time)

    return seek_count, seek_sequence
