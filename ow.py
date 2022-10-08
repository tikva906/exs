class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Название ресторана " + self.restaurant_name)
        print("Кухня ресторана " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " открыто")

restaurant1 = Restaurant('por','rop')
restaurantt2 = Restaurant('ponron','rop')
restauranttt3 = Restaurant('nopon','rop')

restaurant1.describe_restaurant()
restaurantt2.describe_restaurant()
restauranttt3.describe_restaurant()
