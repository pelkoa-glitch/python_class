class User:
    def __init__(self, first_name, last_name, age, height, weight, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print(f"Number of login attempts = {self.login_attempts}")

    def describe_user(self):
        print(f"User's name is {self.first_name} {self.last_name}.")
        print(f"User's age is {self.age}.")
        print(f"User's height is {self.height}.")
        print(f"User's weight is {self.weight}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")


class Admin(User):
    def __init__(self, first_name, last_name, age, height, weight):
        self.privileges = Privileges()
        super().__init__(first_name, last_name, age, height, weight, login_attempts=0)


class Privileges:
    def __init__(self):
        self.privileges = ["allowed to add messages",
                           "allowed to delete users",
                           "allowed to ban users"]

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)


albert = Admin('albert', 'einstein', 80, 165, 55)
albert.privileges.show_privileges()

