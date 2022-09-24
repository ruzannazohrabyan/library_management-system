from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"
