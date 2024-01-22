import csv
import json
import pickle
import os

class FileHandler:
    def __init__(self, input_file, output_file, changes_in_file):
        self.input_file = input_file
        self.output_file = output_file
        self.changes_in_file = changes_in_file
        self.work = []

    def read_data(self):
        if not os.path.exists(self.input_file):
            print(f"Plik nie istnieje: {self.input_file}")
            return

        if self.input_file.endswith('.csv'):
            with open(self.input_file, mode='r') as file:
                reader = csv.reader(file)
                self.work = [row for row in reader]
        elif self.input_file.endswith('.json'):
            with open(self.input_file, mode='r') as file:
                self.work = json.load(file)
        elif self.input_file.endswith('.pkl'):
            with open(self.input_file, mode='rb') as file:
                self.work = pickle.load(file)
        else:
            raise ValueError("Nieobsługiwany format pliku.")

    def change_data_in_our_work(self):
        for incoming_change in self.changes_in_file:
            data_to_change = incoming_change.split(",")
            if len(data_to_change) != 3 or not data_to_change[0].isnumeric() or not data_to_change[1].isnumeric():
                print("Nieprawidłowy format danych wejściowych.")
                continue

            x_value = int(data_to_change[0])
            y_value = int(data_to_change[1])
            new_value = data_to_change[2]

            if x_value >= len(self.work) or y_value >= len(self.work[x_value]):
                print(f"Indeks poza zakresem: {x_value}, {y_value}")
                continue

            self.work[x_value][y_value] = new_value

    def write_data(self):
        if not os.path.exists(self.output_file):
            print(f"Plik wyjściowy nie istnieje: {self.output_file}")
            return

        if self.output_file.endswith('.csv'):
            with open(self.output_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(self.work)
        elif self.output_file.endswith('.json'):
            with open(self.output_file, mode='w') as file:
                json.dump(self.work, file)
        elif self.output_file.endswith('.pkl'):
            with open(self.output_file, mode='wb') as file:
                pickle.dump(self.work, file)
        else:
            raise ValueError("Nieobsługiwany format pliku.")