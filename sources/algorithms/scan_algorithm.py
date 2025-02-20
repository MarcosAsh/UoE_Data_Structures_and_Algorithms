import time
import threading

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def scan_algorithm_real_time(requests, head, direction):
    """
    requests: List of requested floors.
    head: Current floor of the lift.
    direction: Initial direction of movement ('1' for up or '-1' for down).
    max_floor: The highest floor in the building.
    return: Tuple containing the total seek operations and the sequence of visited floors.
    """
    seek_count = 0
    left = []
    right = []
    seek_sequence = []
    
    while requests or left or right:
        for floor in requests:
            for req in floor:
                if req < head:
                    left.append(req)
                elif req > head:
                    right.append(req)
        
        left = quicksort(left)
        right = quicksort(right)
        requests.clear()
        
        if direction == -1 and left:
            while left:
                current_track = left.pop()
                seek_sequence.append(current_track)
                seek_count += abs(head - current_track)
                head = current_track
            direction = 1
        elif direction == 1 and right:
            while right:
                current_track = right.pop(0)
                seek_sequence.append(current_track)
                seek_count += abs(head - current_track)
                head = current_track
            direction = -1
        time.sleep(1)  # Simulate real-time movement
    
    return seek_count, seek_sequence

# test code
if __name__ == "__main__":
    requests = [176, 79, 34, 60, 92, 11, 41, 114]
    head = 50
    direction = -1
    max_floor = 200

    total_seek, sequence = scan_algorithm_real_time(requests, head, direction)
    print(f"Total seek operations: {total_seek}")
    print("Seek sequence:", sequence)
