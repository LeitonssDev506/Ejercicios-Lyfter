from actions import get_average, get_overall_average




def get_menu_option():
    while True:
        try:
            option = int(input('Type a number from 1 to 9: '))
            if not (1 <= option <= 9):
                raise ValueError("Option out of range.")
            return option
        except ValueError:
            print("Error: Invalid option. Please enter an integer between 1 and 9.")
            


def options(option_number, text:str ):
    print(f"{str(option_number)}. {text}")



def display_menu():

    print(50 * "-")

    print("Hello Welcome to Student tracking system\n")

    print("Select an option:\n")

    options(1, "Add student/grades to the system")
    options(2, "View grades of the entered students")
    options(3, "View the top 3 students with the highest average grade")
    options(4, "View overall students average")
    options(5, "Delete student")
    options(6, "View grades of students who failed")
    options(7, "Export students to CSV")
    options(8, "Import students from CSV")
    options(9, "Close system\n")

    print(50 * "-")


def display_students_table(students_list):

    if not students_list:
        print("\n The DB don't have students yet!.")
    else:

        print("\n" + "=" * 88)
        print(f"{'Full Name':<25} | {'Section':<8} | {'Spanish':<8} | {'English':<8} | {'Social Studies':<10} | {'Science':<8}")
        print("=" * 88)

        for student in students_list:
            print(
                f"{student['Fullname']:<25} | "
                f"{student['Section']:<8} | "
                f"{student['Spanish_grade']:<8} | "
                f"{student['English_grade']:<8} | "
                f"{student['Social_Studies']:<14} | "
                f"{student['Science_grade']:<8}"
            )
        print("=" * 88)




def display_top3_table(students_list : list):
    
    if not students_list:
        print("\n The DB don't have students yet!.")
    else:
        top3 = sorted(students_list, key= get_average, reverse=True)[:3]


        print("\nTOP 3")
        

        print("\n" + "=" * 50)
        print(f"{'Full Name':<25} | {'Section':<8} | {'Average Grade':<8}")
        print("=" * 50)

        for student in top3:

            average = get_average(student)
            print(
                f"{student['Fullname']:<25} | "
                f"{student['Section']:<8} | "
                f"{average:<8.2f}" #.2f muestra dos decimales en el print
        )
        print("=" * 50)


def display_overall_average(students_list):

    if not students_list:
        print("\nThe DB doesn't have students yet!")
        return

    overall_average = get_overall_average(students_list)

    print("\n" + "=" * 40)
    print("OVERALL STUDENTS AVERAGE")
    print("=" * 40)
    print(f"Average Grade: {overall_average:.2f}")
    print("=" * 40)


    
def display_table_students_who_failed(existing_students):


        
    if not existing_students:
        print("\n The DB don't have students yet!.")
    else:
        print("\n" + "=" * 88)
        print(f"{'Full Name':<25} | {'Section':<8} | {'Spanish':<8} | {'English':<8} | {'Social Studies':<14} | {'Science':<8}")
        print("=" * 88)

        for student in existing_students:
            fn = student.get("Fullname")
            sec = student.get("Section")
            
            s = float(student.get("Spanish_grade", 0))
            e = float(student.get("English_grade", 0))
            se = float(student.get("Social_Studies", 0))
            sc = float(student.get("Science_grade", 0))
            
            if s < 60 or e < 60 or se < 60 or sc < 60: 
                grade_columns = []
                
                for grade in [s, e, se, sc]:
                    if grade < 60:
                        grade_columns.append(f"{grade:.2f}")
                    else:
                        grade_columns.append("")

                print(
                    f"{fn:<25} | "
                    f"{sec:<8} | "
                    f"{grade_columns[0]:<8} | "
                    f"{grade_columns[1]:<8} | "
                    f"{grade_columns[2]:<14} | "
                    f"{grade_columns[3]:<8}"
                )
                print("-" * 88)

        print("=" * 88)
                










                



            
