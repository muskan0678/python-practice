# #1. create a class car with attribute brand = "scorpio".

# class Car:
#     brand= "Scorpio"

# obj1= Car()
# print("Brand name is -", obj1.brand)

# # 2. create a class laptop with attributes: brand, ram, price. create 2 object with different values.

# class Laptop:
#     brand= "default 8GB"
#     price= "default 1 lakh"

# Laptop1= Laptop()
# Laptop1.brand= "Macbook"
# Laptop1.RAM= "16GB"
# print("Laptop1 Brand -", Laptop1.brand)

# Laptop2= Laptop()
# Laptop2.brand= "Lenovo"
# print("Laptop2 Brand -", Laptop2.brand)

# 3. create class student that takes 3 marks and has a method average().

class Student:

    def __init__(self, name, listOfMarks):
        self.name= name
        self.listOfMarks= listOfMarks

    def average(self):
        sum= 0
        for eachValue in self.listOfMarks:
            sum= sum+eachValue

            average= sum/3
            print("Average is: ", average)

student1= Student("Mussu", [99, 98, 97])
student1.average()

