from repository.student_repository import StudentRepository


class StudentService:
    def __init__(self):
        self.student_repo = StudentRepository("./db_resources/data_init.json")

    def get_all(self):
        return self.student_repo.get_all()

    def get_by_username(self, username):
        return self.student_repo.get_by_username(username)
