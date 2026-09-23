class person():
    def __init__(self,name,age=None,address=None):
        self.name=name
        self.age=age
        self.address=address

    def display(self):
        print("the name is ",self.name)
        print("the age  is",self.age)
        print("the address is ",self.address)
p1=person("vijay")
print(p1)
p2=person("gana",21)
print(p2)
p3=person("raj",22,"banglor")

p1.display()

p2.display()

p3.display()
