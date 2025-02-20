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
max_floors, lift_capacity, requests = read_input_file('sources/input_files/input0.txt') # file selected for simulation
Building = building(max_floors, lift_capacity, requests)

# GUI class
def update_gui():
    while True:
        total_seek, sequence = scan_algorithm_real_time(requests, Building.getLift().get_current_floor(), Building.getLift().get_move(), max_floors)
        for floor in reversed(range(max_floors)):
            if floor == Building.getLift().get_current_floor():
                labels[floor].config(bg='green') # green for floor we are currently located on
            else:
                labels[floor].config(bg='white') # white for any floors we are not on

# Starting simulation of tkinter
def start_simulation():
    threading.Thread(target=update_gui, daemon=True).start()

# Function to measure and plot time complexity
def measure_time_complexity():
    scan_times = []
    look_times = []
    num_requests = []

    for i in range(0, 300): # simulation 300 input files
        print(i)
        filename = "sources/components/input_files/input"+ i +".txt" # file names for input file
        num_floors, lift_capacity, requests = read_input_file(filename)
        lift = building(num_floors, lift_capacity, requests).getLift()

        # Get times for SCAN algorithm
        start = time.time()
        scan_algorithm_real_time(requests, lift.get_current_floor(), lift.get_move(), num_floors)
        scan_times.append(time.time()- start)

        # Get time for LOOK algorithm
        start = time.time()
        look_algorithm_real_time(num_floors, [req for floor in requests for req in floor], lift.get_current_floor(), lift.get_move())
        look_times.append(time.time() - start)

        num_requests.append(sum(len(floor)for floor in requests))
    # Plot both graphs
    plt.figure(fig_size=(10,5))
    plt.plot(num_requests, scan_times, label='SCAN algorithm', marker='o')
    plt.plot(num_requests, look_times, label='LOOK algorithm', marker='s')
    plt.xlabel('Number of Requests')
    plt.ylabel('Execution time (s)')
    plt.title("Time Complexity of SCAN vs LOOK Algorithm")
    plt.legend()
    plt.grid()
    plt.show()

# Create the Tkinter window
root = tk.Tk()
root.title("Lift simulation")
root.geometry("600x600")

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