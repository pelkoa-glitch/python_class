class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def increment_number_served(self):
        self.number_served += 102

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}.")
        print(f"Cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} now is open.")

    def served(self):
        print(f"Number of visitors served is {self.number_served}.")

restaurant_0 = Restaurant('KFC', 'Backed chicken')
restaurant_1 = Restaurant('Mac', 'Beef')
restaurant_2 = Restaurant('Subway', 'Sandwich')

restaurant_0.served()
restaurant_0.increment_number_served()
restaurant_0.served()