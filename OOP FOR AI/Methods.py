class student:
    def __init__(self,name):
        self.name=name
        print("Adding new student")


    def welcome(self):
        print("Welcome to the school",self.name)


s1=student("Azzam")
print(s1.name)
s1.welcome()