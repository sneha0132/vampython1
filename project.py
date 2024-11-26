class Student:
    def __init__(self, student_id, name, age, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.email = email
        self.courses = []
    
    def enroll_in_course(self, course):
        self.courses.append(course)
    
    def __str__(self):
        course_list = ', '.join([course.course_name for course in self.courses])
        return f"Student ID: {self.student_id}\nName: {self.name}\nAge: {self.age}\nEmail: {self.email}\nEnrolled in: {course_list if course_list else 'No courses enrolled yet'}"

class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.enrolled_students = []
    
    def add_student(self, student):
        self.enrolled_students.append(student)
    
    def __str__(self):
        return f"Course Code: {self.course_code}\nCourse Name: {self.course_name}\nCredits: {self.credits}\nEnrolled Students: {len(self.enrolled_students)}"

class CollegeManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def add_course(self, course):
        self.courses.append(course)
    
    def enroll_student_in_course(self, student_id, course_code):
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_code == course_code), None)
        
        if student and course:
            student.enroll_in_course(course)
            course.add_student(student)
            print(f"Student {student.name} enrolled in {course.course_name} successfully!")
        else:
            print("Student or Course not found!")
    
    def display_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            for student in self.students:
                print(student)
                print("-" * 40)
    
    def display_courses(self):
        if not self.courses:
            print("No courses in the system.")
        else:
            for course in self.courses:
                print(course)
                print("-" * 40)

def main():
    system = CollegeManagementSystem()
    
    # Adding sample students
    student1 = Student("S1001", "Alice Johnson", 20, "alice@example.com")
    student2 = Student("S1002", "Bob Smith", 21, "bob@example.com")
    
    system.add_student(student1)
    system.add_student(student2)
    
    # Adding sample courses
    course1 = Course("CSE101", "Computer Science Basics", 3)
    course2 = Course("MTH101", "Calculus I", 4)
    
    system.add_course(course1)
    system.add_course(course2)
    
    # Display all students and courses
    print("All Students:")
    system.display_students()
    
    print("\nAll Courses:")
    system.display_courses()
    
    # Enroll students in courses
    print("\nEnrolling Students:")
    system.enroll_student_in_course("S1001", "CSE101")
    system.enroll_student_in_course("S1002", "MTH101")
    
    # Display updated student and course information
    print("\nUpdated Students:")
    system.display_students()
    
    print("\nUpdated Courses:")
    system.display_courses()

if __name__ == "__main__":
    main()
