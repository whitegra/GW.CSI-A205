from GWemployeeClass import Employees

def main():
    #innitialize list with employees:
    employees = []

    # loop through three times
    for i in range(1, 4):
        name = input(f"Enter the name for employee {i}: ")
        ID = int(input(f"Enter the ID for employee {i}: "))
        department = input(f"Enter the department for employee {i}: ")
        job_title = input(f"Enter the job title for employee {i}: ")

        employee = Employees(name, ID, department, job_title)
        employees.append(employee)

    i = 1
    for employee in employees:
        print("________________________________________________")
        print(f"\n INFORMATION FOR EMPLOYEE #{i}: \n")
        print("________________________________________________")
        print(f"name : {employee.get_name()}\n")
        print(f"age : {employee.get_ID()}\n")
        print(f"address : {employee.get_department()}\n")
        print(f"phone number : {employee.get_job_title()}\n")
    # incriment i to print all the people's information:
    i += 1


if __name__ == "__main__":
    main()
                
