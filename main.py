from student_functions import *
user_choice = input("Enter your choice (1: Read and Display CSV, 2: Total Number of Records, 3: List of Column Names): ")
if user_choice == '1':
    read_display_csv(myfile)
elif user_choice == '2':
    total_number_of_records(myfile)
elif user_choice == '3':
    list_of_column_names(myfile)
else:
    print("Error, invalid entry. Please try again.")