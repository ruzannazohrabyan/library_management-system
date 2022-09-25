import json

from entity import Student


class StudentRepository:
    def __init__(self, file_path):
        self.__data = self.__read_data(file_path)

    @staticmethod
    def __read_data(file_path):
        file = open(file_path)
        data = json.load(file)
        file.close()
        return data

    def get_all(self):
        students = []
        for student in self.__data['students']:
            students.append(Student(student['firstname'], student['lastname'], student['username']))
        return students

    def get_by_username(self, username):
        student = next((item for item in self.__data["students"] if item["username"] == username), None)
        return student
