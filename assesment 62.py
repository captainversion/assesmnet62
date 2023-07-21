class Dog:
    def __init__(self,name,age,coatcolor):
        self.name=name
        self.age=age
        self.coatcolor=coatcolor
    def description(self):
        return f"Name is {self.name} and age is {self.age} years old"
    def get_info(self,coatcolor):
        self.coatcolor=coatcolor
        return f"{self.name} is {coatcolor}"
class JackRussellTerrier(Dog):
    pass
class Bulldog(Dog):
    pass

obj=JackRussellTerrier("Riya",3,"red")
obj1=Bulldog("manith",1,"white")

print(obj.description())
print(obj.get_info("red"))
print(obj1.description())
print(obj1.get_info("white"))