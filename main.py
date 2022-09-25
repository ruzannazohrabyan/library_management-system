from service.student_service import StudentService

if __name__ == "__main__":

    student_service = StudentService()
    students = student_service.get_all()
    print(students)
    print("\n*********************************\n")
    student = student_service.get_by_username("ahovakimyan")
    print(student)




