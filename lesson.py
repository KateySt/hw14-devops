class Person:
    age: int   # Encapsulation: age is encapsulated as a private attribute.
    _name: str  # Encapsulation: _name is encapsulated as a protected attribute.

    def GetName(self):
        return self._name  # Define a method to get the name attribute

    def SetName(self, name):# Encapsulation: _name is set using a protected attribute
        if name != "":
            self._name = name  # Define a method to set the name attribute if the provided name is not empty

    def __init__(self, name: str, age: int = None, occupation: str = None) -> None:
        self._name = name  # Initialize the private _name attribute with the provided name

        self.age = age  # Initialize the age attribute with the provided age, or set it to 18 if age is None
        if self.age is None:
            self.age = 18 # Encapsulation: Access to age through a setter method.

        self.occupation = occupation  # Initialize the occupation attribute with the provided occupation, or None if not provided

    def __str__(self) -> str:
        return f"Hello, I'm {self._name}, I'm {self.age} years old."  # Define the string representation of the object

    def __del__(self):
        print(f"{self._name} says goodbye!")  # Define what happens when the object is deleted

    def meet(self, name: str):
        print(f"Hello, nice to meet you, {name}. I'm {self._name}!")  # Define a method for greeting another person

# Inheritance: Worker class inherits from Person class
class Worker(Person):
    occupation: str  # Declare a class attribute occupation

    @staticmethod
    def ClockIn(name): # Polymorphism: ClockIn is a static method that can be called on the class.
        print(f"{name} has clocked in")  # Define a static method for clocking in
        # ClockIn = staticmethod(ClockIn)

    def __init__(self, name: str, age: int = None, occupation: str = "worker") -> None:
        super(Worker, self).__init__(name, age)   # Inheritance: Call the parent class's constructor
        self.occupation = occupation  # Initialize the occupation attribute with the provided occupation, or "worker" by default

    def greet(self):
        return self._name  # Define a method to greet

    def __str__(self) -> str:  # Polymorphism: Overriding the __str__ method in the parent class.
        return f"Hello, I'm {self._name}, I'm {self.age} years old. I work as an {self.occupation}."  # Override the string representation method


def Meet(p1, p2): # Polymorphism: The Meet function works with different types of parameters.
    print(type(p1), type(p2))  # Print the types of the provided objects
    return str(p1) + " " + str(p2)  # Return a string concatenating the string representations of the objects


if __name__ == "__main__":
    alex = Worker("Alex", 32)  # Create an instance of the Worker class
    dima = Person("Dima")  # Create an instance of the Person class
    print(Meet(dima, alex))  # Polymorphism: Meet function works with both Person and Worker instances
    print(Meet(11, True))  # Call the Meet function with different types
    Worker.ClockIn("John")   # Polymorphism: Calling static method on the Worker class.
