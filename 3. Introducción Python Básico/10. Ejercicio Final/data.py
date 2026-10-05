import csv
import os


def load_bd_student_system(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            print( f"\nInformation successfully imported from '{filepath}'!")
            
            return list(reader)
    except FileNotFoundError:
        print('File do not exits')
        print("\nThere is no previously exported CSV file.")
        return []

    except Exception as e:
        print(f"\nAn error occurred while importing the CSV file: {e}")
        return []



def save_students_to_file(students_list, filename, delimiter=","):

    if not students_list:
        print("\nThere are no students to export.")
        return

    if os.path.exists(filename):

        while True:

            confirmation = input(f"\n'{filename}' already exists. "
                "Do you want to overwrite it? (Y/N): ").strip().upper()

            if confirmation == "N":
                print("\nExport cancelled. Existing file was not modified.")
                return

            if confirmation == "Y":
                break

            print("Invalid option. Please type Y or N.")

    try:

        fieldnames = [
            "Id_students",
            "Fullname",
            "Section",
            "Spanish_grade",
            "English_grade",
            "Social_Studies",
            "Science_grade"
        ]

        with open(filename,mode="w",newline="",encoding="utf-8") as file:

            writer = csv.DictWriter(file,fieldnames=fieldnames,delimiter=delimiter)

            writer.writeheader()
            writer.writerows(students_list)

        print(f"\nInformation successfully exported to '{filename}'!")

    except Exception as e:
        print(f"An error occurred while saving the CSV file: {e}")