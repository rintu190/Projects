class Employee:
    def __init__(self,name ="rintu",age=13):
        self.name = name
        self.age =age
    def displayEmployee(self):
        print("Name:",self.name,", age: ",self.age)

print("doc", Employee.__doc__)
print("module", Employee.__module__)
print("base", Employee.__bases__)
print("dict", Employee.__dict__)
print("name", Employee.__name__)