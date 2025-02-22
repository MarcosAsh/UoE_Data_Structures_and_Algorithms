import time
import threading

from stack import stack

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def scan_algorithm_real_time(requests, head, direction, one_floor_moving_time):
    """
    requests: List of requested floors.
    head: Current floor of the lift.
    direction: Initial direction of movement ('1' for up or '-1' for down).
    max_floor: The highest floor in the building.
    return: Tuple containing the total seek operations and the sequence of visited floors.
    """
    seek_count = 0
    left = stack()
    right = stack()
    seek_sequence = []
    
    while requests or not left.is_empty() or not right.is_empty():
        for req in requests:
            # Handle nested requests (lists inside the requests list)
            if isinstance(req, list):
                for sub_req in req:
                    if sub_req < head:
                        left.push(sub_req)
                    elif sub_req > head:
                        right.push(sub_req)
            else:
                if req < head:
                    left.push(req)
                elif req > head:
                    right.push(req)
        
        # Sort the stacks
        left.items = quicksort(left.items)
        right.items = quicksort(right.items)
        requests.clear()
        
        if direction == -1 and not left.is_empty():
            while not left.is_empty():
                current_track = left.pop()
                seek_sequence.append(current_track)
                seek_count += abs(head - current_track)
                head = current_track
            direction = 1
        elif direction == 1 and not right.is_empty():
            while not right.is_empty():
                current_track = right.pop(0)  # Removing from the start of the list
                seek_sequence.append(current_track)
                seek_count += abs(head - current_track)
                head = current_track
            direction = -1
        time.sleep(one_floor_moving_time)
    
    return seek_count, seek_sequence

# Test code
if __name__ == "__main__":
    requests = [176, 79, 34, 60, 92, 11, 41, 114]
    head = 50
    direction = -1
    one_floor_moving_time = 0.1  # Example real-time simulation

    total_seek, sequence = scan_algorithm_real_time(requests, head, direction, one_floor_moving_time)
    print(f"Total seek operations: {total_seek}")
    print("Seek sequence:", sequence)
