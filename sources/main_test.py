import sys
import os
import time
import threading

# Assign variables from input file
max_floors, lift_capacity, requests = read_input_file('sources/input_files/input0.txt')
# Reverse Requests list
requests = requests[::-1]
# Create building object
Building = building(max_floors, lift_capacity, requests)
# Create Lift object
Lift = Building.getLift()

# ************************ Main Loop taking requests on each floor (Real - Time) ************************

def main_loop_RealTime():
    """Main loop for the simulation."""
    # Get the requests for the current floor
    currentFloor = Building.getFloor(Lift.get_current_floor())
    for req in currentFloor.GetPeople():
        # Add the people to the lift
        if Lift.add_people(req):
            # Removes the person from the floor
            currentFloor.RemoveFromPeople(req)
        
    # Get seek count and seek sequence using the scan algorithm
    seek_count, seek_sequence = scan_algorithm_real_time(Lift.peopleList, Lift.get_current_floor(), Lift, 0.1,max_floors)
    seek_sequence = seek_sequence[::-1]
    print('current floor:', Lift.get_current_floor())
    print('seek count:', seek_count)
    print('seek sequence:', seek_sequence)
    print('requests in lift:', Lift.peopleList)

    # Process each floor in the seek_sequence
    for floor in seek_sequence:
        print(f"Moving to floor {floor}...")  # Debug statement
        
        # Ensure the lift moves to the target floor in the sequence
        Lift.change_current_floor(floor)
        
        # If the lift can move up, do so
        if Lift.get_current_floor() < floor:
            Lift.move_up()
        elif Lift.get_current_floor() > floor:
            Lift.move_down()

        # Check if there are people that want to get off at the current floor
        for person in Lift.peopleList:
            if person == Lift.get_current_floor():
                Lift.remove_people(person)
        
        # If there are no requests on the current floor, continue to the next floor
        if len(currentFloor.GetPeople()) == 0:
            print(f"No requests on floor {Lift.get_current_floor()}")  # Debug statement
            continue
        
        # Check how much space is in the lift
        vacancy = lift_capacity - Lift.get_num_people()

        # If the lift is full, only add the amount of people that can fit in the lift
        if vacancy < len(currentFloor.GetPeople()):
            for req in range(vacancy):
                Lift.add_people(currentFloor.GetPeople()[req])
            # Removes the people that were added to the lift from the requests list
            currentFloor.SetPeople(currentFloor.GetPeople()[vacancy:])

        # If the lift is not full, add all the requests to the lift
        else:
            for req in currentFloor.GetPeople():
                Lift.add_people(req)
            # Clear the requests list of people that have been added to the lift
            currentFloor.SetPeople([])

        # Re-run the scan algorithm to get the new seek count and sequence after handling current requests
        seek_count, seek_sequence = scan_algorithm_real_time(Lift.peopleList, Lift.get_current_floor(), Lift, 0.1,max_floors)
        seek_sequence = seek_sequence[::-1]
        print('current floor:', Lift.get_current_floor())
        print('seek count:', seek_count)
        print('seek sequence:', seek_sequence)

        # Simulate the lift's movement
        print(f"Remaining requests: {Building.getRemainingPeople()}")





# Run the main loop until all requests are processed
while Building.getRemainingPeople() + Lift.get_num_people() >= 0:
    print(f"Starting new loop with current floor: {Lift.get_current_floor()}")
    main_loop_RealTime()

# Once the loop is done, print the final status
print("All requests processed.")
