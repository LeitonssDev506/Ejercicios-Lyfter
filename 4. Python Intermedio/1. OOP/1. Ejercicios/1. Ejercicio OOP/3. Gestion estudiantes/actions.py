import re

def is_valid_name(fullname):


    if not isinstance(fullname, str):
        raise TypeError("Error: The fullname must be a string.")
    
    if not fullname.strip():
        raise ValueError("Error: The fullname cannot be empty.")
        
    if len(fullname) > 200:
        raise TypeError("Error: The fullname must be under 200 characters.")
        
    if re.search(r'\d', fullname):
        raise ValueError("Error: The fullname must not contain numbers.")
        
    return True


def is_valid_section(section):

    
    if not isinstance(section, str):
        raise TypeError("Error: The section class must be a string.")

    section = section.strip().upper()
    
    pattern = r'^\d{2}[A-Z]$'
    
    if not re.match(pattern, section):
        raise ValueError("Error: The format must be two numbers and a letter at the end (e.g., 11B)")
        
    return True

def is_valid_grade(subject_value):
    
    if not isinstance(subject_value, (int, float)):
        raise TypeError("Error: Type a number")

    if subject_value < 0 or subject_value > 100 :
        raise ValueError("Error: The value must be between [0 - 100]")

    return True


def get_grade(subject):
    while True:
        try:
            grade = float(input(f"Type the {subject} Grade: "))
            is_valid_grade(grade)
            return grade

        except (ValueError, TypeError) as e:
            print(f"Please try again: {e}")



def student_exists(id_students, students_list):
    for student in students_list:
        if student.id_students == id_students:
            return True

    return False
                

def average_grade_calculated(spanish_grade,english_grade,social_grade,science_grade):
        result = (spanish_grade + english_grade + social_grade + science_grade)/4
        return result



def get_student_info():
        while True:
            try:   
                fullname = str(input("Type the Full name or Press Enter to Return to main menu: ")).strip().title().replace(",", "")
                if not fullname:
                    print("\nReturning to main menu...")
                    return None, None , None
                is_valid_name(fullname)
                break
            except (ValueError, TypeError) as e:
                print(f"Please try again: {e}")

        while True:
            try:
                section = str(input("Type the class section (E.g. 11B): ")).upper()
                is_valid_section(section)
                break
            except (ValueError, TypeError) as e:
                print(f"Please try again: {e}")
            
        id_students = (fullname + section).replace(" ", "")

        return fullname, section, id_students


class Student():

    def __init__(self, id_students , fullname , section, spanish_grade, english_grade, social_grade, science_grade):
        self.id_students = id_students
        self.fullname = fullname
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_grade = social_grade
        self.science_grade = science_grade


def add_students(existing_students):

    while True:
        student_info = get_student_info()
        fullname, section, id_students = student_info
        if fullname is None:
            return None
        if student_exists(id_students, existing_students):
            print("\n")
            print("The students already exits, please try again with other name and section")
            print("\n")
            continue
        break


    spanish_grade = get_grade("Spanish")
    english_grade = get_grade("English")
    social_grade  = get_grade("Social Studies")
    science_grade = get_grade("Science")


    return Student(id_students , fullname , section, spanish_grade, english_grade, social_grade, science_grade)


def get_average(student):

    spanish_grade = float(student.spanish_grade)
    english_grade = float(student.english_grade)
    social_grade = float(student.social_grade)
    science_grade = float(student.science_grade)

    return average_grade_calculated(
        spanish_grade,
        english_grade,
        social_grade,
        science_grade
    )


def get_overall_average(students_list):

    if not students_list:
        return None

    total_average = 0

    for student in students_list:
        total_average += get_average(student)

    return total_average / len(students_list)


def delete_students(existing_students):


    if not existing_students:
        print("\nThere are no students to delete.")
        return existing_students


    print("Please type the following info to delete the student\n")

    while True:
        student_info = get_student_info()
        fullname, class_section, id_students = student_info
        if fullname is None:
            return None
        
        if not student_exists(id_students, existing_students):
            print("\nStudent not found. Please try again with an existing student.\n")
            continue
        break
        
    print("\nStudent found:")
    print(f"Name: {fullname}")
    print(f"Section: {class_section}")

    while True:

        confirmation = input(
            "\nAre you sure you want to delete this student? (Y/N): "
        ).strip().upper()

        if confirmation == "N":
            print("\nDeletion cancelled.")
            return existing_students

        if confirmation == "Y":
            break

        print("Invalid option. Please type Y or N.")

    for index, student in enumerate(existing_students):

        if student.id_students == id_students:
            existing_students.pop(index)
            break

    print("\nThe student was removed successfully.")

    return existing_students
