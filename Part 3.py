#mporting libaries
import csv

#creating student class
class Student:
    #initializing
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    #adding course method
    def add_course(self, course):
        #if course is unique than add course
        if course.course_code not in self.courses:
            #adding unique course to course list
            self.courses[course.course_code] = []
        #otherwise do not add course
        else:
            #output for repeat course
            print("Student already enrolled in this course.")

    #add grade method
    def add_grade(self, course_code, grade):
        #if course code is found in courses
        if course_code in self.courses:
            #than append the grade for that course
            self.courses[course_code].append(grade)
        #otherwise output that student is not in that course
        else:
            #output
            print("Student is not enrolled in this course.")

#Creating course class
class Course:
    #initializing
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

#Creating students grade class
class StudentGradingSystem:
    #initializing
    def __init__(self):
        self.students = {}
        self.courses = {}

    #adding student method
    def add_student(self):
        #input for student ID
        student_id = input("Enter student ID: ")
        #if student is already made
        if student_id in self.students:
            #output
            print("Student ID already exists.")
            return
        #enter name for student ID your creating
        name = input("Enter student name: ")
        self.students[student_id] = Student(student_id, name)

    #add course method
    def add_course(self):
        #input for the course name
        course_code = input("Enter course code: ")
        #if course is already in courses
        if course_code in self.courses:
            #output
            print("Course already exists.")
            return
        #course name for course code
        course_name = input("Enter course name: ")
        self.courses[course_code] = Course(course_code, course_name)

    #enrolling student into courses method
    def enroll_student(self):
        #input for finding your student you want to enroll
        student_id = input("Enter student ID: ")
        #if student cannot be found based odd ID
        if student_id not in self.students:
            #output student not found
            print("Student not found.")
            return
        #if student is found, enter the course code you want to enroll them in
        course_code = input("Enter course code: ")
        #if course is not found
        if course_code not in self.courses:
            #print course is not found
            print("Course not found.")
            return
        #enroll student to course
        self.students[student_id].add_course(self.courses[course_code])

    #adding students grade method
    def add_grade(self):
        #input to enter the students ID you want to grade
        student_id = input("Enter student ID: ")
        #if student cannot be found based odd ID
        if student_id not in self.students:
            #output student not found
            print("Student not found.")
            return
        #enter the course you would like to grade the student for
        course_code = input("Enter course code: ")
        #if student is not found enrolled in the course
        if course_code not in self.students[student_id].courses:
            #output Student is not enrolled
            print("Student is not enrolled in this course.")
            return
        try:
            #input for students grade (float)
            grade = float(input("Enter grade without % sign: "))
            #add grade
            self.students[student_id].add_grade(course_code, grade)
        #if error occours
        except ValueError:
            #output Invalid grade
            print("Invalid grade input. Please enter a number.")

    #menu method
    def menu(self):
        #until made false run
        while True:
            #menu output
            print("\nStudent Grading System")
            print("1. Add Student")
            print("2. Add Course")
            print("3. Enroll Student in Course")
            print("4. Add Grade")
            print("5. Exit")
            #user enters there menu selection
            choice = input("Enter your choice: ")
            #if choice 1
            if choice == "1":
                #run method add_student
                self.add_student()
            #if choice 2
            elif choice == "2":
                #run method add_course
                self.add_course()
            #if choice 3
            elif choice == "3":
                #run method enroll_student
                self.enroll_student()
            #if choice 4
            elif choice == "4":
                #run method add_grade
                self.add_grade()
            #if choice 5
            elif choice == "5":
                #break the loop
                break
            #otherwise
            else:
                #output not in menu list
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    system = StudentGradingSystem()
    system.menu()
