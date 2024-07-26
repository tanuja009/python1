class A:
    def __init__(self,name,number):
        self.name=name
        self.number=number
    def people(self):
        print(self.name)
        print(self.number)

    def details(self):
        print(f"my name is{self.name}")
        print(f"my id numbe is{self.number}")
class B(A):
    def __init__(self,name,number,age,salary):
        self.age=age
        self.salary=salary

        A.__init__(self,name,number)
    def details(self):
        print(f"name is {self.name}")
        print(f"name is {self.number}")
        print(f"name is {self.age}")
        print(f"name is {self.salary}")
class C(A):
    def __init__(self, name, number,post,experience):
        super().__init__(name, number)
        self.post=post
        self.experience=experience
    def datails(self):
        print(f"name is {self.name}")
        print(f"name is {self.number}")
        print(f"name is {self.post}")
        print(f"name is {self.experience}")

b=B("ram",1050,22,40000)
c=C("syam",2536,"Software Intern",4)
b.details()
b.people()
c.details()
c.people()