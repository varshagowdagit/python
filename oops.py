#demo on basic class and object
class Basic():
    def __init__(self,name):
        self.name = name

    def dis(self):
        print("Hi",self.name,"welcome to class")
obj=Basic('Varsha')
obj.dis()

#data encapsulation : wrapping data members and its methods work together

class Emp():
    def __init__(self,name,sal):
        self.name=name
        self.salary=sal                                         #data members
    def display(self):
        print("Name",self.name,"works for",self.salary)         #data methods
e=Emp("varsha",27800)
e.display()

#polymorphism
class Vehicle():
    def __init__(self,model):
        self.model=model
    def move(self):
        print("MOVE")

class Car(Vehicle):
    pass

class Plane(Vehicle):
    def move(self):
        print("FLY")

class Boat(Vehicle):
    def move(self):
        print("Sail")

c=Car('audi')
c.move()
p=Plane("Deccan Airlines")
p.move()
b=Boat('Titanic')
b.move()
#with model and its method
for x in (c,p,b):
    print(x.model)
    x.move()

#data abstraction : hiding unnecessary details and showing only the necessary requirements/features
from abc import ABC
class Car(ABC):
    def move(self):
        pass

class Audi(Car):
    def move(self):
        print("High speed")

class Swift(Car):
    def move(self):
        print("Medium Speed")

a=Audi()
a.move()
s=Swift()
s.move()

for i in (a,s):
    print(i)
    i.move()

#Access specifier
#public ------Accessible anywhere from any part of the prgm
class Emp():
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def dis(self):
        print("name:",self.name,"salary:",self.sal)
e=Emp('vs',27800)
e.dis()

#private ------Accessible within that class
class Emp():
    def __init__(self,name,sal):
        self.__name=name
        self.__salary=sal
    def dis(self):
        print("name:",self.__name,"salary:",self.__salary)
e=Emp('vs',34567)
e.dis()

#protected ------Accessible within the class and class derived from it
class Emp():
    def __init__(self,name,sal):
        self._name=name
        self._sal=sal
    def disp(self):
        print("name:",self._name,"salary:",self._sal)
class New(Emp):
    def disp(self):
        print("Name:",self._name,"salary:",self._sal)
e=Emp('vs',987654)
e.disp()
n=New('sagar',150000)
n.disp()

#Inheritance
