class User():
    def __init__(self,name, last_name, region):
        self.name = name
        self.last_name = last_name
        self.region = region
        self.login_attempts = 0

    def describe_user(self):
        print("Имя пользователя " + self.name + self.last_name )
        print("Регион пользователя " + self.region)

    def greet_user(self):
        print("Hello" + self.name + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Mixs','Minov','FNEFF')
print("Login attempts: " + str(user1.login_attempts))
print("loging...")
user1.increment_login_attempts()
print("Login attempts: " + str(user1.login_attempts))
print("loging...")
user1.increment_login_attempts()
print("Login attempts: " + str(user1.login_attempts))
print("loging...")
user1.increment_login_attempts()
print("Login attempts: " + str(user1.login_attempts))

print("resetting login attempts...")
user1.reset_login_attempts()
print("Login attempts: " + str(user1.login_attempts))
