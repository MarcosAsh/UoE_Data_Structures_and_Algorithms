import time
import threading

# Quick Sort for LOOK algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# LOOK algorithm handling real-time requests
def look_algorithm_real_time(floors, requests, current_floor, direction):
    """
    floors: Total number of floors in the building.
    requests: List of requested floors.
    current_floor: Current position of the lift.
    direction: Initial direction of movement ('up' or 'down').
    return: The final floor the lift reaches after serving all requests.
    """
    def add_request(new_request):
        """Simulates real-time request arrival"""
        requests.append(new_request)
        print(f"New request added: {new_request}")
    
    # Simulate dynamic requests appearing in real-time
    threading.Timer(3, lambda: add_request(25)).start()
    threading.Timer(5, lambda: add_request(90)).start()

    requests = quicksort(requests)
    while requests:
        print(f"Current floor: {current_floor}")
        print(f"Requests: {requests}")
        
        if direction == 1:  # Going up
            next_requests = [req for req in requests if req >= current_floor]
            if next_requests:
                next_floor = min(next_requests)
            else:
                direction = -1  # Change direction
                continue
        else:  # Going down
            next_requests = [req for req in requests if req <= current_floor]
            if next_requests:
                next_floor = max(next_requests)
            else:
                direction = 1  # Change direction
                continue
        
        current_floor = next_floor
        requests.remove(current_floor)
        time.sleep(1)  # Simulate real-time movement
    
    return current_floor

# Test code
requests = [0, 5, 3, 7, 9, 2]
floors = 10
current_floor = 50
direction = 1  # 1 for up, -1 for down

final_floor = look_algorithm_real_time(floors, requests, current_floor, direction)
print(f"Final Floor: {final_floor}")
