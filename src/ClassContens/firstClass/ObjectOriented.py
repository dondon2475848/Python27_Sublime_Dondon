#coding=utf-8
class Person():
    count = 0 # Static/class variable
    def __init__(self, name, city):
        self.name = name # Variable for the instance
        self.city = city # Variable for the instance
        Person.count += 1
    def number_of_persons(self):
        return Person.count

p1 = Person('Bob','New York')
print p1.count
print p1.number_of_persons()
print p1.name
print p1.city


p2 = Person('Judy', 'Hong kong')
print p2.number_of_persons()
print p2.name
print p2.city
Person.count
Person.number_of_persons(p1)
p1.number_of_persons()

(1).__add__(2)
1+2

class MyInteger():
    def __init__(self, integer):
        #print "constructor"
        self.integer = integer
    def __add__(self, integer): # Overloaded '+' operator
        if self.integer == 2 and integer == 2:
            return 5
        else:
            return self.integer + integer
m = MyInteger(1)
print m.__add__(1)
m2 = MyInteger(2)
print m2.__add__(2)
print m2.__add__(4)
print m2 + 2
print m + 3



class Vehicle():
    def my_own(self): return True
    
class Bicycle(Vehicle):
    def __init__(self, color): self.color = color
    def has_wheels(self): return True

class rent_bike(Bicycle):
    def my_own(self): return False
    def has_wheels(self): return False

Ubike = rent_bike('yellow')
print Ubike.color
print Ubike.my_own()
print Ubike.has_wheels()






# class Vehicle():
#     def my_own(self): return True
#     
# class Bicycle(Vehicle):
#     def __init__(self, color): self.color = color
#     def has_wheels(self): return True
#     def __str__(self): return "%s is %s"%(self.__class__.__name__,self.color)
# 
# class rent_bike(Bicycle):
#     def my_own(self): return False
# Ubike = rent_bike('yellow')
# print Ubike









