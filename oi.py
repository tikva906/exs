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

class Admin(User):
    def __init__(self,name,last_name,region):
        super().__init__(name,last_name,region)
        self.privilege = []
        self.privilegee = Privilegs

    def show_privileges(self):
        for privilegee in self.privilege:
            print("Admin" + privilegee)

            class Privilegs():
                def __init__(self, privilege=[]):
                    self.privileges = privilege

Adminn = Admin('Markus','PROGEGL','EGL')

Adminn.privilege = [' может сделать админом' ,' может добавить когонибудь' ,' может удолить' ,'может забанить']
Adminn.show_privileges()
Adminn.privilege.show_privileges()