# main.py

# imports
from building import building
from lift import lift
from floor import Floor
from person import Person
from scan_algorithm import scan_algorithm_real_time


def main():
    num_of_floors = int(input("input number of floors: "))
    lift_capacity = int(input("Input lift cpacity: "))
    initial_requests = [2, 5, 5, 6, 6, 7, 4, 4]

    # Initialize building and lift
    my_building = building(num_of_floors, lift_capacity, initial_requests)
    my_lift = lift(current_floor=0, doors_open=False, moving=False, direction=1, capacity=lift_capacity)
    
    # Run SCAN algorithm for lift operation
    total_seek, seek_sequence = scan_algorithm_real_time(initial_requests, my_lift.current_floor, my_lift.direction, num_of_floors)
    
    print(f"Total seek operations: {total_seek}")
    print(f"Seek sequence: {seek_sequence}")
    
    # Display final lift state
    print(f"Final lift position: {my_lift.current_floor}")


if __name__ == "__main__":
    main()