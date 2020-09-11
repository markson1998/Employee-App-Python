# Name: Markson Leite
# Student: R00172859
# Class: COMP1C-Y
# Project: Employee Program
# Date: 28/04/2019

import csv
import random

def GetChoice(employee_id_list, firstname_list, surname_list, email_list, salary_list):
    while True:
        print("1. View all employees")
        print("2. View a particular employee")
        print("3. Edit the salary of an employee")
        print("4. Add a new employee")
        print("5. Delete an employee")
        print("6. Give a bonus to each employee")
        print("7. Generate a report for management")
        print("8. Quit")
        choice = int(input("Choice >> "))
        print()

        if choice == 1:
            show_all_employees(employee_id_list, firstname_list, surname_list, salary_list, email_list)
        elif choice == 2:
            view_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list)
        elif choice == 3:
            change_salary(employee_id_list,salary_list)
        elif choice == 4:
            add_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list)
        elif choice == 5:
            remove_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list)
        elif choice == 6:
            generate_bonus_info()
        elif choice == 7:
            generate_reports(salary_list, firstname_list , surname_list)
        elif choice == 8:
            break
        else:
            print("Invalid Choice!. Enter 1-8")

def load_data(file): ## Loading data function DONE
    connection = open(file, "r")
    employee_id_list = []
    firstname_list = []
    surname_list = []
    salary_list = []
    email_list = []
    while True:
        line = connection.readline()
        if line == "":
            break
        line_info = line.split(",")
        employee_id_list.append(line_info[0])
        firstname_list.append(line_info[1])
        surname_list.append(line_info[2])
        email_list.append(line_info[3])
        salary_list.append(float(line_info[4]))
    return employee_id_list, firstname_list, surname_list, email_list, salary_list

# def load_data(): ## Loading data function DONE
#     employee_id_list = []
#     firstname_list = []
#     surname_list = []
#     salary_list = []
#     email_list = []
#     with open('employees.txt','r+') as csv_file:
#         csv_reader = csv.reader(csv_file)
#         for line in csv_reader:
#             employee_id_list.append(line[0])
#             firstname_list.append(line[1])
#             surname_list.append(line[2])
#             salary_list.append(line[4])
#             email_list.append(line[3])
#     return employee_id_list,firstname_list,surname_list,salary_list,email_list

def show_all_employees(employee_id_list, firstname_list, surname_list, salary_list, email_list): ## Show all employees function done
    print("Employees ID's: {}".format(employee_id_list))
    print("First Name's: {}".format(firstname_list))
    print("Surnames's: {}".format(surname_list))
    print("Salary's: {}".format(salary_list))
    print("Email's: {}".format(email_list))

def find_employee_pos_in_list(id,employee_id_list): ## Find employee index position done
    if id in employee_id_list:
        position_index = employee_id_list.index(id)
    else:
        position_index = -1
    return position_index

def view_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list):
    user_id = str(input("Enter Employee ID: "))
    id_position = find_employee_pos_in_list(user_id,employee_id_list)
    if id_position != -1:
        print("Employee ID: ", employee_id_list[id_position])
        print("First Name: ", firstname_list[id_position])
        print("Surname: ", surname_list[id_position])
        print("Salary: ", salary_list[id_position])
        print("Email: ", email_list[id_position])
        print("")
    else:
        print("Employee {} does not exist".format(user_id))

def change_salary(employee_id_list,salary_list):
    user_id = str(input("Enter Employee ID: "))
    id_position = find_employee_pos_in_list(user_id, employee_id_list)
    if id_position != -1:
        salary_list[id_position] = float(input("Enter new Salary:"))
        print("Salary of employee {} has been changed to {}".format(user_id, salary_list[id_position]))
    else:
        print("Employee of ID >> {} << cannot be found".format(user_id))

def add_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list):
    unique_id = random.randint(10000,99999)
    user_first = str(input("Employee First Name: "))
    user_surname = str(input("Employee Surname: "))
    user_salary = float(input("Employee Salary: "))
    user_email = "{}_{}@cit.ie".format(user_first,user_surname)
    employee_id_list.append(unique_id)
    firstname_list.append(user_first)
    surname_list.append(user_surname)
    salary_list.append(user_salary)
    email_list.append(user_email)

def remove_employee(employee_id_list, firstname_list, surname_list, salary_list, email_list):
    user_id = str(input("Enter Employee ID: "))
    id_position = find_employee_pos_in_list(user_id, employee_id_list)
    if id_position != -1:
        print("Removing {} {} from employee list".format(firstname_list[id_position], surname_list[id_position]))
        del employee_id_list[id_position]
        del firstname_list[id_position]
        del surname_list[id_position]
        del salary_list[id_position]
        del email_list[id_position]
    else:
        print("User ID not found")

def generate_reports(salary_list, firstname_list , surname_list):
    total = sum(salary_list)
    length = len(salary_list)
    average = total / length
    highest = max(salary_list)
    print("Total = ", total)
    print("Average = ", average)
    print("Highest = ", highest)
    print("Employees with highest salary:")
    for i in range(len(salary_list)):
        if salary_list[i] == highest:
            print(firstname_list[i], surname_list[i])
    print()

def generate_bonus_info():  # Was not able to do it!
    print()

def write_data(employee_id_list, firstname_list, surname_list, email_list, salary_list, file):
    with open(file, "w") as output:
        for i in range(len(employee_id_list)):
            print(employee_id_list[i], firstname_list[i], surname_list[i], email_list[i], salary_list[i], sep=",",
                    file = output)

def main():
    file = "employees.txt"
    employee_id_list, firstname_list, surname_list, email_list, salary_list = load_data(file)
    GetChoice(employee_id_list, firstname_list, surname_list, email_list, salary_list)
    write_data(employee_id_list, firstname_list, surname_list, email_list, salary_list, file)

main()
