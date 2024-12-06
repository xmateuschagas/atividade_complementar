import unittest
from UserManager import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.manager = UserManager()

    def test_add_user(self):
        self.manager.add_user("Alice")
        self.assertIn("Alice", self.manager.users)
        self.assertEqual(self.manager.add_user("Alice"), "User already exists")

    def test_remove_user(self):
        self.manager.add_user("Bob")
        self.manager.remove_user("Bob")
        self.assertNotIn("Bob", self.manager.users)
        self.assertEqual(self.manager.remove_user("Charlie"), "User not found")

if __name__ == '__main__':
    unittest.main()
