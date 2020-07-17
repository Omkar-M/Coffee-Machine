class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print(f"Hello, I am {self.name}!")


name_in = input()
person = Person(name_in)
person.greet()
