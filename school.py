class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        else:
            return False
    def get_average_grade(self):
        average = 0
        for std in self.students:
            average += std.get_grade()
        average = average / len(self.students)
        return average

s1 = Student("Zeinab", 13, 99)
s2 = Student("Jill", 13, 100)
s3 = Student("Bill", 13, 29)
s4 = Student("Tim", 13, 2)

c = Course("programming", 3)
c.add_student(s1)
c.add_student(s2)
c.add_student(s3)
print(c.add_student(s4))
avg = c.get_average_grade()
print(avg)
print(c.students[0].name)