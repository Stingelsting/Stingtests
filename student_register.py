'''
The purpose of this code is to view the available student records and
register new students on available records
'''
try:
    nr_students = int(input("Enter the number of students registering: "))
    print("You entered a valid integer:", nr_students)

except ValueError:
    print("Error: You entered a string instead of an integer.")

else:
    with open("reg_form.txt", "a", encoding="utf-8") as f:
        f.write(
            "Please sign on the dotted line next to your student number "
            "as proof of attendance:\n")

        for i in range(1, nr_students + 1):
            student = input(f"Enter student {i} number: ")
            f.write(f"Student nr is: {student}  ....................\n")

    print("\nThank you for entering student numbers.")
