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


# test
student = Student("Anisa", "Shaikh", "A2")
question = Question(student)
net_amount = question.net_amount(4, 46)
question.calculate(question.net_amount(4, 46))
