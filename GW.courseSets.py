def get_course_info():
    """
    purpose: user enters course ID (or course number) and returns the info
    inputs: the course ID
    outputs: the course time, instructor, and room#
    """
    # first, define the libraries within the function:
    # first make the dicts for the course:rooms:

    # Dictionaries for course information
    course_room_dict = {
        "CS101": "3004",
        "CS102": "4501",
        "CS103": "6755",
        "NT110": "1244",
        "CM241": "1411"
    }

    course_instructor_dict = {
        "CS101": "Haynes",
        "CS102": "Alvarado",
        "CS103": "Rich",
        "NT110": "Burke",
        "CM241": "Lee"
    }

    course_time_dict = {
        "CS101": "8:00 a.m.",
        "CS102": "9:00 a.m.",
        "CS103": "10:00 a.m.",
        "NT110": "11:00 a.m.",
        "CM241": "1:00 p.m."
    }

    while True:
        course_id = input("Enter the course ID: ")
        # if the course id exists, then get the corresponding room, instructor, and time from the dicts above:
        if course_id in course_room_dict and course_id in course_instructor_dict and course_id in course_time_dict:
            course_instructor = course_instructor_dict[course_id]
            course_room = course_room_dict[course_id]
            course_time = course_time_dict[course_id]
            print("__________________________________")
            print(f"{course_id} Instructor: {course_instructor}")
            print(f"{course_id} Room #: {course_room}")
            print(f"{course_id} Time: {course_time}")
            print("___________________________________")

        run_again = input("Look up another course? ('y/n'): ")
        if run_again.lower() != 'y':
            break

if __name__ == "__main__":
    get_course_info()
    
                                                          

            
