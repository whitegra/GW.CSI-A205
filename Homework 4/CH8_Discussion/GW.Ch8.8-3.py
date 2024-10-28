def main():
    """
    purpose: generate student login sing first name, last name, and ID
    """
    first_name =input("Enter the student's first name: ")
    last_name = input("Enter student last name: ")
    student_id = input("Enter the student's ID number: ")

    # if first name > 3, use first three letters, else use full name:
    if len(first_name) >= 3:
        first_id_part = first_name[:3]
    else:
        first_id_part = first_name
    # same for last name:
    if len(last_name) >= 3:
        second_id_part = last_name[:3]
    else:
        second_id_part = last_name

    #same for ID
    if len(student_id) >= 3:
        last_id_part = student_id[:3]
    else:
        last_id_part = student_id

    #concatonate
    login_user = first_id_part + second_id_part + last_id_part
    print(f"The student's username is: {login_user}")

# to execute the main block 
if __name__ == "__main__":
    main()
 
    
