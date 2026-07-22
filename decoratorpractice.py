def uppercase_decorator(func):
    def wrapper(self):
        return func(self).upper()
    return wrapper

class Student:
    def __init__(self, name):
        self.name = name

    @uppercase_decorator
    def display(self):
        return f"Student Name: {self.name}"

name = input("Enter student name: ")
s = Student(name)

print(s.display())
