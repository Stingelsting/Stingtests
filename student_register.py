
# Error handling: Ensure the input is an integer for the number of students registering.
try:
    # Initialize input variable for the number of students.
    nr_students = int(input("Enter the number of students registering: "))
    print("You entered a valid integer:", nr_students)
except ValueError:
    # Handle the case where the input is not an integer.
    print("Error: You entered a string instead of an integer.")
else:
    # Open a file named "reg_form.txt" in write mode to store the student numbers.
    # The file will automatically close when the 'with' block is exited.
    with open("reg_form.txt", "w") as f:
        f.write("Please sign on the dotted line next to your student number as proof of attendance:\n")
        
        # Loop through the range from 1 to the number of students.
        for i in range(1, nr_students + 1):
            # Prompt the user to enter each student's number.
            student = input(f"Enter student {i} number: ")
            # Write the student's number to the file in a formatted string.
            f.write(f"Student nr is: {student}  ....................\n")

    # Print a message indicating the completion of student number entry.
    print("\nThank you for entering student numbers.")