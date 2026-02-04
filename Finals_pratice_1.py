class Student():
    def __init__(self, name: str, age: int, major: str, gpa: float):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
    
    def update_gpa(self, amount:float):
        new_gpa = self.gpa + amount
        if new_gpa > 4.0:
            self.gpa = 4.0
        else:
            self.gpa = new_gpa

    def new_name(self, namenew : str):
        self.name = namenew

    def __str__(self):
        return f"Gpa of {self.gpa:.2f} and name of {self.name}"
    
class Courses():
    def __init__(self, class_code: str, class_name: str, credits: int, instructor: str):
        self.class_code = class_code
        self.class_name = class_name
        self.credits = credits
        self.instructor = instructor
    def __str__(self):
        return f"{self.class_code} - {self.class_name} ({self.credits} credits) | Instructor: {self.instructor}"
    
class University:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = {}

    def add_student(self, student: Student):
        self.students.append(student)

    def add_course(self, course: Courses):
        self.courses.append(course)
        
    def enroll(self, student_name: str, course_code: str):
        
        student_exist = False

        for s in self.students:
            if s.name.lower() == student_name.lower():
                student_exist = True
                break
        if not student_exist:
            print("Student not Found")
            return
            
        courses_exist = False
        for c in self.courses:
            if c.class_code.lower() == course_code.lower():
                courses_exist = True
                break
        if not courses_exist:
            print("The course does not exist")
            return
        
        if course_code not in self.enrollments:
            self.enrollments[course_code] = []
        
        if student_name in self.enrollments[course_code]:
            print("Student already enrolled in this course")
            return

        self.enrollments[course_code].append(student_name)
        print(f"{student_name} is added to {course_code}.")

    def drop(self, student_name: str, course_code: str):

        if course_code not in self.enrollments:
            print('The course does not exist')
            return
        if student_name not in self.enrollments[course_code]:
            print(' The student does not exist')
            return
        
        self.enrollments[course_code].remove(student_name)
        print(f"{student_name} has been removed from {course_code}. ")

    def list_students(self):
        if len(self.students) == 0:
            print("No Students found")
        else:
            for s in self.students:
                print(s)

    def list_courses(self):
        if len(self.courses) == 0:
            print("No courses found")
        else:
            for c in self.courses:
                print(c)

    def list_enrollments(self):
        if len(self.enrollments) == 0:
            print('You have no enrollments')
        else:
            for course_code in self.enrollments:
                print(course_code)
                student_in_course = self.enrollments[course_code]
                if len(student_in_course) == 0:
                    print("There is not students enrolled")
                else: 
                    for s in student_in_course:
                        print(s)

    def course_stats(self):
        stats = {}
        for course_code in self.enrollments:
            student_list = self.enrollments[course_code]
            count = len(student_list)
            stats[course_code] = count
        return stats
    

def main():
    
    uni = University()  

    while True: 
        
        option = input("""\n University System
                       1: Add Student  
                       2: Add Course 
                       3: Enroll
                       4: Drop student from course
                       5: List all students
                       6: List all courses
                       7: List all enrollments
                       8: Show statistics
                       9: Quit
                       Enter Option: """)
        
        if option == "1":
            name = input("What is the Name: ")
            age = int(input("What is students Age: "))
            major = input("What is students Major: ")
            gpa = float(input("What is students GPA:"))
            s = Student(name,age,major,gpa)
            uni.add_student(s)
            print('student added')

        elif  option == "2":
            code = input("What is the course code: ")
            name = input("What is the class name: ")
            credits = int(input("What is the class credits: "))
            instructor = input("What is the class instructor: ")
            c = Courses(code,name,credits,instructor)
            uni.add_course(c)
            print("Course added")

        elif  option ==  "3":
            name = input("What is the student name: ")
            code = input("What is the Course Code: ")
            uni.enroll(name,code)
            

        elif  option == "4":
            name = input("What is the student name: ")
            code = input("What is the Course Code: ")
            uni.drop(name,code)
            
        
        elif  option == "5":
            uni.list_students()

        elif  option == "6":
            uni.list_courses()
        
        elif  option == "7":
            uni.list_enrollments()
        
        elif  option == "8":
            stats = uni.course_stats()
            if len(stats) == 0:
                print("No statistics available (no enrollments yet).")
            else:
                print("Course stats (students per course):")
                for code, count in stats.items():
                    print(f"{code}: {count} student(s)")

        elif  option == "9":
            print("Goodbye")
            break
        else:
            print("invalid option, try again")

if __name__ == "__main__":
    main()
