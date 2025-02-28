import tkinter as tk
import threading
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from algorithms.scan_algorithm import scan_algorithm
from algorithms.look_algorithm import look_algorithm
from algorithms.my_lift_algorithm import my_lift
from algorithms.read_input_file_algorithm import read_input_file
from components.building import building

class LiftSimulationGUI:
    def __init__(self, root, building):
        self.root = root
        self.building = building
        self.lift = self.building.get_lift()
        self.algorithms = {"SCAN": scan_algorithm, "LOOK": look_algorithm, "MY_LIFT": my_lift}
        self.algorithm = "SCAN"  # Default algorithm

        self.root.title("Lift Simulation")
        self.root.geometry("400x700")

        self.floor_labels = []
        for i in range(self.building.get_num_floors()):
            label = tk.Label(root, text=f"Floor {i+1}: 0 waiting", width=20, height=2, bg='white', relief="solid")
            label.pack(side="bottom")
            self.floor_labels.append(label)

        self.lift_status = tk.Label(root, text="Lift: 0 people inside", font=("Arial", 12))
        self.lift_status.pack()

        self.start_button = tk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack()

        self.toggle_algorithm_button = tk.Button(root, text="Change Algorithm", command=self.toggle_algorithm)
        self.toggle_algorithm_button.pack()

        self.algorithm_label = tk.Label(root, text=f"Current Algorithm: {self.algorithm}")
        self.algorithm_label.pack()

    def update_gui(self):
        for i, label in enumerate(self.floor_labels):
            num_waiting = self.building.get_floor(i).GetNumPeople()
            label.config(text=f"Floor {i+1}: {num_waiting} waiting", bg='green' if i == self.lift.get_current_floor() else 'white')
        self.lift_status.config(text=f"Lift: {self.lift.get_num_people()} people inside")
        self.root.update()

    def toggle_algorithm(self):
        algo_keys = list(self.algorithms.keys())
        current_index = algo_keys.index(self.algorithm)
        self.algorithm = algo_keys[(current_index + 1) % len(algo_keys)]
        self.algorithm_label.config(text=f"Current Algorithm: {self.algorithm}")

    def run_algorithm(self):
        selected_algorithm = self.algorithms[self.algorithm]

        if self.algorithm == "SCAN":
            all_requests = []
            for i in range(self.building.get_num_floors()):
                all_requests.extend(self.building.get_floor(i).GetPeople().return_queue())  # Get requests from each floor
            sequence = selected_algorithm(all_requests, self.lift.get_current_floor(), 1, self.building.get_num_floors())
        else:
            sequence = selected_algorithm(self.building)

        for floor in sequence:
            self.lift.change_current_floor(floor)
            self.update_gui()
            time.sleep(1)

            floor_obj = self.building.get_floor(floor)
            people_waiting = floor_obj.GetPeople()
            for person in people_waiting.return_queue()[:]:
                if self.lift.get_num_people() < self.lift.get_capacity():
                    self.lift.add_people(person)
                    floor_obj.RemoveFromPeople()
            self.update_gui()
            time.sleep(1)

    def start_simulation(self):
        threading.Thread(target=self.run_algorithm, daemon=True).start()

if __name__ == "__main__":
    num_floors, lift_capacity, requests = read_input_file('sources/input_files/input0.txt')
    sim_building = building(num_floors, lift_capacity, requests)
    root = tk.Tk()
    app = LiftSimulationGUI(root, sim_building)
    root.mainloop()