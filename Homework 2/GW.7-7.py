import random

def main():
    num_students = int(input("Enter the number of students: "))
    
    fees_per_credit = 253
    students_fees = [] #create empty list to store the student fees

    for i in range(num_students): #for each student
        credits = random.randint(1, 15)#random credits 1-15
        student_fees = credits * fees_per_credit #fees = credit * credit_fee
        student_output_info = f"student# {i + 1}: fees paid = ${student_fees}" #this will make sure to print the student and corresponding fee that is due
        students_fees.append(student_output_info) #append to the student fees list to print
    for student_fee in students_fees: #this will print the above info for each student in column format:
        print(student_fee)
    
if __name__ == "__main__":
    main()    
        
