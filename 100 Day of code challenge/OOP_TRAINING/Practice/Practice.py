from dataclasses import dataclass

@dataclass()
class Person:
    name: str
    age: int
    gender: str
    major: str

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Major: {self.major}")

# Create class object Person
person1 = Person("Alice", 25, "Female", "Scientist")
person2 = Person("Bob", 30, "Male", "Driver")

# Tests
person1.display_info()
person2.display_info()
