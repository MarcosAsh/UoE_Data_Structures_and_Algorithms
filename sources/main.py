import sys
import os
import tkinter as tk
import threading
import time
import matplotlib.pyplot as plt

# Ensure the sources directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "components")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "algorithms")))

from components.building import building
from algorithms.scan_algorithm import scan_algorithm_real_time
from algorithms.look_algorithm import look_algorithm_real_time

# Read input file
def read_input_file(filename):
    num_floors = 0
    lift_capacity = 0
    requests = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if "," in line:
                num_floors, lift_capacity = map(int, line.split(","))
                requests = [[] for _ in range(num_floors)]
                break
        for line in lines:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            if ":" in line:
                floor, destinations = line.split(":")
                floor = int(floor.strip()) - 1
                if destinations.strip():
                    requests[floor] = list(map(int, destinations.split(",")))
    return num_floors, lift_capacity, requests

# Initialize building
max_floors, lift_capacity, requests = read_input_file('sources/input_files/input0.txt') # File for simulation
Building = building(max_floors, lift_capacity, requests)
Lift = Building.getLift()
print(requests)

# GUI Class
def update_gui():
    for floor in reversed(range(max_floors)):
        if floor == Lift.get_current_floor():
            labels[floor].config(bg='green')
        else:
            labels[floor].config(bg='white')

def main_loop():
    while True:
        total_seek, sequence = scan_algorithm_real_time(requests, Lift.get_current_floor(), Lift, 0.1)
        print(sequence)
        for target_floor in sequence:
            Lift.change_current_floor(target_floor)
            update_gui()
            time.sleep(1)
            
            # Handle people getting on and off
            floor_obj = Building.getFloor(target_floor)
            people_waiting = floor_obj.GetPeople()
            for person in people_waiting[:]:  # Copy list to avoid modifying while iterating
                if Lift.get_num_people() < lift_capacity:
                    Lift.add_people(person)
                    floor_obj.RemoveFromPeople(person)
            update_gui()
            time.sleep(1)

def start_simulation():
    threading.Thread(target=main_loop, daemon=True).start()

# Function to measure and plot time complexity
def measure_time_complexity():
    scan_times = []
    look_times = []
    num_requests = []
    
    for i in range(1, 201):  # Simulating 200 input files
        filename = f"sources/input_files/input{i}.txt"
        num_floors, lift_capacity, requests = read_input_file(filename)
        lift = building(num_floors, lift_capacity, requests).getLift()
        
        start = time.time()
        scan_algorithm_real_time(requests, lift.get_current_floor(), lift.get_move(), num_floors)
        scan_times.append(time.time() - start)
        
        start = time.time()
        look_algorithm_real_time(num_floors, [req for floor in requests for req in floor], lift.get_current_floor(), lift.get_move())
        look_times.append(time.time() - start)
        
        num_requests.append(sum(len(floor) for floor in requests))
    
    plt.figure(figsize=(10, 5))
    plt.plot(num_requests, scan_times, label='SCAN Algorithm', marker='o')
    plt.plot(num_requests, look_times, label='LOOK Algorithm', marker='s')
    plt.xlabel('Number of Requests')
    plt.ylabel('Execution Time (s)')
    plt.title('Time Complexity of SCAN vs LOOK Algorithm')
    plt.legend()
    plt.grid()
    plt.show()

# Create the Tkinter window
root = tk.Tk()
root.title("Lift Simulation")
root.geometry("300x600")

# Create floor labels
labels = []
for i in range(max_floors):
    label = tk.Label(root, text=f"Floor {i+1}", width=20, height=2, bg='white', relief="solid")
    label.pack(side="bottom")
    labels.append(label)

# Start button
start_button = tk.Button(root, text="Start Simulation", command=start_simulation)
start_button.pack()

# Plot complexity button
plot_button = tk.Button(root, text="Plot Time Complexity", command=measure_time_complexity)
plot_button.pack()

# Run the application
root.mainloop()
