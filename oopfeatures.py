# class animal:
#     def __init__(self,name):
#         self.name=name
    
#     def student(self,age):
#         self.age=age

# class animal2(animal):
#     def __init__(self,name,age,queue):
#         super().__init__(name)
#         super().student(age)
#         self.queue=queue

# animi=animal2("dog",25,"FIFO Style")
# print(animi.name,animi.age,animi.queue)



# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}")

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def greet(self):
#         super().greet()
#         print(f"I am {self.age} years old")

# # Create an instance of Child
# child_instance = Child("Alice", 12)
# child_instance.greet()


class hello:
    def __init__(self,name):
        self.name=name
    def student(self):
        print(self.name)


class hello1:
    def __init__(self,age):
        self.age=age
    def student(self):
        print(self.age)
        
class hello2(hello,hello1):
    def __init__(self,name,age):
        print("hello")
        super.__init__(name)
        super.__init__(age)

h1=hello2("tanuja",25)
h1.student()

       
