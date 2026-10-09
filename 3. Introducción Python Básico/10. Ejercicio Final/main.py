from menu import display_menu , get_menu_option, display_students_table, display_top3_table, display_table_students_who_failed,  display_overall_average
from actions import add_students , delete_students
from data import load_student_data, save_students_to_file



def main():

    filepath = "students_grades.csv"

    students_list = []

    while True:

        display_menu()

        option = get_menu_option()

        match option:

            case 1:
                new_student = add_students(students_list)
                if new_student is None:
                    continue
                students_list.append(new_student)
                print("\nStudent successfully added.")
            case 2:
                display_students_table(students_list)
            case 3:
                display_top3_table(students_list)
            case 4:
                display_overall_average(students_list)
            case 5:
                result = delete_students(students_list)
                if result is None:
                    continue
                students_list = result
            case 6:
                display_table_students_who_failed(students_list)
            case 7:
                save_students_to_file(students_list,filepath)
            case 8:
                imported_students = load_student_data(filepath)
                if imported_students is not None:
                    students_list = imported_students
            case 9:

                print("\nClosing system. Goodbye!")
                break


if __name__ == "__main__":
    main()