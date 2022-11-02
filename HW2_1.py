class Student:

    def __init__(self, student_name, student_surname, student_class):
        self.student_name = student_name
    class Student:

    def __init__(self, student_name, student_surname, student_class):
        self.student_name = student_name
        self.student_surname = student_surname
        self.student_class = student_class

class Question(Student):
    def __init__(self, Student):
        super().__init__(Student.student_name, Student.student_surname, Student.student_class)


    def net_amount(self, wrong_count, correct_count):
        net_count = correct_count - (wrong_count/4)
        return net_count

    def calculate(self, net_count):
        total_grade = (net_count*2)
        print("Student information:\n name: {}\n surname: {}\n class: {}\n total_grade: {}\n ".format(
            self.student_name, self.student_surname, self.student_class, total_grade))

#Take input from user
#
input_name = input("Please enter student name: ")
input_surname = input("Please enter student surname: ")
input_class = input("Please enter student class: ")
exit = False
try:
    input_wrong_count = int(input("Number of incorrect points: "))
    input_correct_count = int(input("Number of correct points: "))
    if input_wrong_count <0 or input_correct_count <0 :
        raise ValueError()

except ValueError as e:
    print()
    print("Input should be a positive number !")
    exit = True
if not exit:
    student = Student(input_name,input_surname,input_class)
    question = Question(student)
    question.calculate(question.net_amount(input_wrong_count, input_correct_count))

