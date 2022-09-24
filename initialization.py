from model import Student, Librarian, Author

import json


class Initialization:
    def __init__(self, file_path):
        self.__data = self.__read_data(file_path)

    @staticmethod
    def __read_data(file_path):
        file = open(file_path)
        data = json.load(file)
        file.close()
        return data

    def get_students(self):
        students = []
        for student in self.__data['students']:
            students.append(Student(student['firstname'], student['lastname'], student['username']))
        return students

    def get_librarians(self):
        librarians = []
        for librarian in self.__data['librarians']:
            librarians.append(Librarian(librarian['firstname'], librarian['lastname'], librarian['username']))
        return librarians

    def get_authors(self):
        authors = []
        for author in self.__data['authors']:
            authors.append(Author(author['firstname'], author['lastname']))
        return authors

