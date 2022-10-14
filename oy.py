class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Название ресторана " + self.restaurant_name)
        print("Кухня ресторана " + self.cuisine_type)

    def open_restaurant(self):
        print(" открыто")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def favoritee(self):
        for favorite in self.flavors:
            print("Любимый вкусы мороженого " + favorite)

iceCreamStand = IceCreamStand('por' ,'rop')
iceCreamStand.flavors = ['манго' ,'драконий фрут']

iceCreamStand.describe_restaurant()
iceCreamStand.favoritee()