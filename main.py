import sys
from file_handler import FileHandler

def main(input_file, output_file, changes):
    file_handler = FileHandler(input_file, output_file, changes)
    file_handler.read_data()
    file_handler.change_data_in_our_work()
    file_handler.write_data()

    print("Zaktualizowane dane:")
    for row in file_handler.work:
        print(row)

if __name__ == "__main__":
    if len(sys.argv) > 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        changes = sys.argv[3:]
        main(input_file, output_file, changes)
    else:
        print("Nieprawidłowe użycie: python main.py ")
