from model import Person


class Student(Person):
    def __init__(self, firstname, lastname, username):
        super().__init__(firstname, lastname)
        self.username = username

