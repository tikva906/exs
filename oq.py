class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Название ресторана " + self.restaurant_name)
        print("Кухня ресторана " + self.cuisine_type)




    def open_restaurant(self):
        print(self.restaurant_name + " открыто")

restaurantt = Restaurant('por','rop')

print(restaurantt.restaurant_name)
print(restaurantt.cuisine_type)
restaurantt.describe_restaurant()
restaurantt.open_restaurant()