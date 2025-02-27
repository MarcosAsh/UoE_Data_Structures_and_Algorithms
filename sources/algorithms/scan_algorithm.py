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
    requests: List of requested floors.
    head: Current floor of the lift.
    lift: Lift object that handles the movement.
    one_floor_moving_time: Time to move one floor.
    return: Tuple containing the total seek operations and the sequence of visited floors.
    """
    seek_count = 0
    left = Stack()
    right = Stack()
    seek_sequence = []
    
    # Get the initial direction of the lift
    direction = lift.get_move()  
    request_queue = []

    # Flatten requests (if there are any nested lists)
    for req in requests:
        if isinstance(req, list):
            request_queue.extend(req)
        else:
            request_queue.append(req)

    # Partition requests into left and right stacks based on the initial head position
    for req in request_queue:
        if req < head:
            left.push(req)
        elif req > head:
            right.push(req)

    # Sort the stacks only once
    left.items = quicksort(left.items)
    right.items = quicksort(right.items)

    # If the head is equal to one of the requested floors, visit it immediately
    if head in request_queue:
        seek_sequence.append(head)
        request_queue.remove(head)
    
    while left.size() > 0 or right.size() > 0:
        if direction == -1 and left.size() > 0:
            while left.size() > 0:
                current_track = left.pop()
                if current_track not in seek_sequence:
                    seek_sequence.append(current_track)
                    seek_count += abs(head - current_track)
                    head = current_track
            direction = 1  # Change direction to up for the next iteration

        elif direction == 1 and right.size() > 0:
            while right.size() > 0:
                current_track = right.pop()
                if current_track not in seek_sequence:
                    seek_sequence.append(current_track)
                    seek_count += abs(head - current_track)
                    head = current_track
            direction = -1  # Change direction to down for the next iteration

        # Simulate lift movement time between floors
        time.sleep(one_floor_moving_time)

    return seek_count, seek_sequence
