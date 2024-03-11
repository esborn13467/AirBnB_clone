# Importing necessary modules
import os
import sys

# Constants
CONSTANT_VARIABLE = 42

# Class definition
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

# Function definition
def my_function(arg1, arg2):
    result = arg1 + arg2
    return result

# Main code block
if __name__ == "__main__":
    my_object = MyClass("Alice")
    my_object.greet()
    print("The result is:", my_function(2, 3))

