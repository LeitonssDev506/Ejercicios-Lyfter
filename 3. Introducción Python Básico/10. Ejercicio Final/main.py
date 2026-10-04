from menu import display_menu , get_menu_option, display_students_table, display_top3_table
from actions import add_students , delete_students , review_students_who_failed
from data import load_bd_student_system, save_students_to_file






def main():

    filepath = "students_grades.csv"
    filepath1 = "students_gradesv2.csv"

    while True:
        display_menu()
        option = get_menu_option()

        if option == 6:
            print("\nClosing system. Goodbye!")
            break
        
        match option:
            case 1:
                existing_students = load_bd_student_system(filepath)
                new_student_list = add_students(filepath)
                if  new_student_list is None:
                    continue
                existing_students.extend(new_student_list)
                save_students_to_file(existing_students, filepath)

            case 2:
                existing_students = load_bd_student_system(filepath)

                display_students_table(existing_students)

            case 3:
                existing_students = load_bd_student_system(filepath)
                if not existing_students:
                    continue
                display_top3_table(existing_students)

            case 4:
                existing_students = load_bd_student_system(filepath)
                delete_student_list = delete_students(existing_students, filepath)

                if  new_student_list is None:
                    continue
                save_students_to_file(delete_student_list, filepath1)









if __name__ == '__main__':
    main()
