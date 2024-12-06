class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        else:
            return "User already exists"

    def remove_user(self, user):
        try:
            self.users.remove(user)
        except ValueError:
            return "User not found"
