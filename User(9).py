class User:
    def __init__(self, first_name, last_name, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight

    def describe_user(self):
        print(f"User's name is {self.first_name} {self.last_name}.")
        print(f"User's age is {self.age}.")
        print(f"User's height is {self.height}.")
        print(f"User's weight is {self.weight}.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")


user = User('albert', 'einstein', 26, 182, 80)
user_ka = User('mary', 'kury', 25, 174, 64)
user.describe_user()
user.greet_user()
user_ka.describe_user()
user_ka.greet_user()
