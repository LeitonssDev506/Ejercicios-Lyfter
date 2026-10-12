import csv
import os

from actions import Student


def load_bd_student_system(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            import_list = [ ] 

            for row in reader:
                id_students = row["Id_students"]
                fullname = row["Fullname"]
                section = row["Section"]
                spanish_grade = float(row["Spanish_grade"])
                english_grade = float(row["English_grade"])
                social_grade = float(row["Social_Studies"])
                science_grade = float(row["Science_grade"])

                new_student = Student(
                    id_students,
                    fullname,
                    section,
                    spanish_grade,
                    english_grade,
                    social_grade,
                    science_grade)

                import_list.append(new_student)

            
            print( f"\nInformation successfully imported from '{filepath}'!")


            
            return import_list
    except FileNotFoundError:
        print('File do not exits')
        print("\nThere is no previously exported CSV file.")
        return None

    except Exception as e:
        print(f"\nAn error occurred while importing the CSV file: {e}")
        return None



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
            
            students_dicts = []
            for student in students_list:
                student_dict = {
                    "Id_students": student.id_students,
                    "Fullname": student.fullname,
                    "Section": student.section,
                    "Spanish_grade": student.spanish_grade,
                    "English_grade": student.english_grade,
                    "Social_Studies": student.social_grade,
                    "Science_grade": student.science_grade,
                }

                students_dicts.append(student_dict)

            writer.writerows(students_dicts)

        print(f"\nInformation successfully exported to '{filename}'!")

    except Exception as e:
        print(f"An error occurred while saving the CSV file: {e}")