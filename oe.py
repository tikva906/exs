class User():
    def __init__(self,name, last_name, region):
        self.name = name
        self.last_name = last_name
        self.region = region

    def describe_user(self):
        print("Имя пользователя " + self.name + self.last_name )
        print("Регион пользователя " + self.region)

    def greet_user(self):
        print("Hello" + self.name + self.last_name)

user1 = User('Mixs','Minov','FNEFF')
user2 = User('Tikva','nine hundred six','FNEAPXFF')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()