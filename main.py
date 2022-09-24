from initialization import Initialization as Init

if __name__ == "__main__":
    print("WELCOME LIBRARY MANAGEMENT SYSTEM")
    print("DATA INITIALIZATION")

    entities = Init("./resources/data_init.json")

    students = entities.get_students()
    librarians = entities.get_librarians()
    authors = entities.get_authors()

    print("You can login as a Librarian")
    username = input("Please enter username > ")

    lib = next((item for item in librarians if item.username == username), None)

    if lib is not None:
        print(f"Welcome {lib.lastname} {lib.firstname}")
    else:
        print("Invalid username")


    # print(students)
    # print(librarians)
    # print(authors)

