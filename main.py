from service.student_service import StudentService

if __name__ == "__main__":

    student_svc = StudentService()
    students = student_svc.get_all()
    print(students)
    print("\n*********************************\n")
    student = student_svc.get_by_username("ahovakimyan")
    print(student)




