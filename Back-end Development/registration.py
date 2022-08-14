class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def sleep(self):
        return "{} {} is now sleeping.".format(self.first_name, self.last_name)

class Student(Person):
    def __init__(self, first_name, last_name, student_number, is_registered = False):
        super().__init__(first_name, last_name)
        self.student_number = student_number
        self.is_registered = is_registered

    def sleep(self):
        return "Student {} is now sleeping.".format(self.student_number)

class Administrator(Person):
    def register(self, student):
        if not student.is_registered:
            student.is_registered = True
            return "Student {} is registered".format(student.student_number)
        else:
            return "Student {} is already registered".format(student.student_number)

student = Student("First Name", "Last Name", "1234567")
admin = Administrator("UP", "CRS")
print(student.sleep())
print(admin.sleep())
print(admin.register(student))
print(admin.register(student))