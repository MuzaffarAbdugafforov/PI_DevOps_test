from app import greet  
import unittest


class TestGreetFunction():
    def test_greet(self):
        greet("Alice")
        greet("Bob")
        greet("Charlie")


x = TestGreetFunction()
x.test_greet()
