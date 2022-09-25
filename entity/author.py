from entity import Person


class Author(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
