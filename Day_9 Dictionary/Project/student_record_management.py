"""
Mini Project – Student Record Dictionary

Program stores student details.

Example structure:

name
age
marks
grade

Concepts used:

dictionary
key value pairs
update values
retrieve values

Real life use:
store user profile.
"""

student_profile = {
    101: {
        "name": "Alice Johnson",
        "age": 20,
        "marks": 88,
        "grade": "A"
    },
    102: {
        "name": "Bob Smith",
        "age": 21,
        "marks": 76,
        "grade": "B+"
    }
}

while True:
    choice = int(input("**STUDENT PROFILE**"\
                       "\n 1.ADD STUDENT "\
                       "\n 2.SHOW STUDENT "\
                       "\n 3.UPDATE STUDENT "\
                       "\n 4.DELETE STUDENT "\
                       "\n 5.SHOW ALL STUDENT  "\
                       "\n 6.EXIT "\
                       "\n ENTER YOUR CHOICE : "))
    if(choice == 1):
        num = int(input("How many student want to add : "))
        for i in range(1,num+1):
            student_detail = {}

            roll = int(input("Enter your roll number : "))
            name = input("Enter your name : ")
            age = int(input("Enter your age : "))
            marks = float(input("Enter your marks : "))
            grade = input("Enter your grade : ")

            student_detail.update({"roll":roll,"name":name,"age":age,"marks":marks,"grade":grade})

            student_profile[roll] = student_detail

            print("===========================")
            print("Student Profile Created")
            print("===========================")
    elif(choice == 2):
        roll_number = int(input("Enter your roll number : "))
        if(roll_number in student_profile):
            print("=====================")
            student_record = student_profile.get(roll_number)
            print(f"Student Roll Number Is : {roll_number}\n")
            for key , value in student_record.items():
                print(f"{key} ---> {value}")
            print("=====================")
        else:
            print("===========================")
            print("Student Profile Not Present")
            print("===========================")
    elif(choice == 3):
        roll_number = int(input("Enter your roll number : "))
        if(roll_number in student_profile):
            print("=====================")
            student_record_update = student_profile.get(roll_number)
            print(f"Student Roll Number Is : {roll_number}\n")
            for key , value in student_record_update.items():
                print(f"{key} ---> {value}")
            print()
            while True:
                ch = int(input("**UPDATE PROFILE**"\
                       "\n 1.NAME "\
                       "\n 2.AGE "\
                       "\n 3.MARKS "\
                       "\n 4.GRADE "\
                       "\n 5.EXIT "\
                       "\n ENTER YOUR CHOICE : "))
                if(ch == 1):
                    updated_name = input("Enter New Updated Name : ")
                    student_record_update['name'] = updated_name
                    print("=====================")
                    print("Name Updated Successfully")
                    print("=====================")
                elif(ch == 2):
                    updated_age = int(input("Enter New Updated Age : "))
                    student_record_update['age'] = updated_age
                    print("=====================")
                    print("Age Updated Successfully")
                    print("=====================")
                elif(ch == 3):
                    updated_marks = float(input("Enter your marks : "))
                    student_record_update['marks'] = updated_marks
                    print("=====================")
                    print("Marks Updated Successfully")
                    print("=====================")
                elif(ch == 4):
                    updated_grade = input("Enter New Updated Grade : ")
                    student_record_update['grade'] = updated_grade
                    print("=====================")
                    print("Grade Updated Successfully")
                    print("=====================")
                elif(ch == 5):
                    break
                else:
                    print("=====================")
                    print("Incorrect Choice")
                    print("=====================")
            print("=====================")
        else:
            print("===========================")
            print("Student Profile Not Present")
            print("===========================")
    elif(choice == 4):
        roll_number = int(input("Enter your roll number : "))
        if(roll_number in student_profile):
            print("===========================")
            print("Student Profile Deleted Successfully")
            student_profile.pop(roll_number)
            print("===========================")
        else:
            print("===========================")
            print("Student Profile Not Present")
            print("===========================")
    elif(choice == 5):
        print("=====================")
        if(student_profile):
            print("ALL STUDENT IN STUDENT DICTIONARY : ")
            for student,student_info in student_profile.items():
                print("=====================")
                print("roll : ",student)
                for key,value in student_info.items():
                    print(f"{key} ---> {value}")
                print()
        else:
            print("=====================")
            print("Student Profiles Empty")
            print("=====================")
        print("=====================")
    elif(choice == 6):
        break
    else:
        print("=====================")
        print("Incorrect Choice")
        print("=====================")