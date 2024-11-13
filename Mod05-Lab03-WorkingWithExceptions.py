import json

# Define the program's data
FILE_NAME: str = ('MyLabData.json')
MENU: str = '''
---- Student GPAs ------------------------------
    Select from the following menu:  
        1. Show current student data. 
        2. Enter new student data.
        3. Save data to a file. 
        4. Exit the program.
--------------------------------------------------
'''
student_first_name: str = ''
student_last_name: str = ''
student_gpa: float = 0.0
message: str = ''
menu_choice: str = ''
student_data: dict = {} # one row of student data
students: list = [] # table of student data
file_data: str = '' # holds combined string data separated by a comma
file = None

# When the program starts, read the file data into a list of dictionary rows (table)
# file = open(FILE_NAME,'r')
# for row in file.readlines():
#     student_data = row.split(',')
#     student_first_name = student_data[0]
#     student_last_name = student_data[1]
#     student_gpa = float(student_data[2].strip())
#     student_data = {"FirstName" : student_first_name,
#                     "LastName" : student_last_name,
#                     "GPA" : student_gpa}
#     students.append(student_data)
# file.close()
try:
    file = open(FILE_NAME,'r')
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

print(students)
for row in students:
    print(f'{row["FirstName"]},{row["LastName"]},{row["GPA"]}')
# Extract the data from the file
    # Transform the data from the file
    # Load it into the collection

# Repeat the follow tasks
while True:
    print(MENU)
    menu_choice = input('Enter your selection: ')
    print()

    if menu_choice == '1':
        # Process the data to create and display a custom message
        for student in students:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"
            print(message.format(student["FirstName"],student["LastName"],student["GPA"]))
        print('-'*50)
        continue

    elif menu_choice == '2':
        # get user input and add to student_data table
        try:
            student_first_name = input('first name, please: ')
            if not student_first_name.isalpha():
                raise ValueError('The first name can\'t have numbers')
            student_last_name = input('last name, please: ')
            if not student_last_name.isalpha():
                raise ValueError('The last name can\'t have numbers either')
            try:
                student_gpa = float(input('gpa, please: '))
            except ValueError:
                raise ValueError('gpa\'s are numbers, dummy')

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "GPA": student_gpa}
            students.append(student_data)
        except ValueError as e:
            print(e)
            print('tech msg here')
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print('gen error')
            print('tech msg here')
            print(e, e.__doc__, type(e), sep='\n')

        continue

    elif menu_choice == '3':
        # Save the data to the file
        try:
            file = open('FILENAME','w')
            # for student in students:
            #     file.write(f'{row["FirstName"]},{row["LastName"]},{row["GPA"]}')
            json.dump({'just a string','string'},file)
            file.close()
            print('Data Saved!')
            continue
        except TypeError as e:
            print('is this a valid json format you\'re giving me?')
            print('tech msg here:')
            print(e,e.__doc__, type(e), sep='\n')
        except Exception as e:
            print('tech msg here:')
            print('builtin python error info:')
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.close() == False:
                file.close()
    # Exit the program
    elif menu_choice == '4':
        break