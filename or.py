class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Название ресторана " + self.restaurant_name)
        print("Кухня ресторана " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " открыто")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

restaurantt = Restaurant('por','rop')

print(restaurantt.restaurant_name)
print(restaurantt.cuisine_type)
restaurantt.describe_restaurant()
restaurantt.open_restaurant()

print("\nNumber served: " + str(restaurantt.number_served))
restaurantt.number_served = 100
print("Number served: " + str(restaurantt.number_served))

restaurantt.set_number_served(445)
print("Number served: " + str(restaurantt.number_served))

restaurantt.increment_number_served(85)
print("Number served: " + str(restaurantt.number_served))