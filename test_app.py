import unittest
from app import greet  

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")
        self.assertNotEqual(greet("Charlie"), "Hi, Charlie!")

if __name__ == "__main__":
    unittest.main()
