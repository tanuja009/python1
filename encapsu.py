# # class student:
# #     def __init__(self):
# #         self.__name=""
# #     def getname(self):
# #         return self.__name
# #     def setname(self):
# #         self.__name=name

# # obj=student()
# # obj.setname("testing")
# # name=obj.getname()
# # print(name)


# # Python program to 
# # demonstrate protected members 

# # Creating a base class 
# class Base: 
# 	def __init__(self): 

# 		# Protected member 
# 		self._a = 2

# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 

# 		# Calling constructor of 
# 		# Base class 
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", 
# 			self._a) 

# 		# Modify the protected variable: 
# 		self._a = 3
# 		print("Calling modified protected member outside class: ", 
# 			self._a) 


# obj1 = Derived() 

# obj2 = Base() 

# # Calling protected member 
# # Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 

# # Accessing the protected variable outside 
# print("Accessing protected member of obj2: ", obj2._a) 



# Python program to 
# demonstrate private members 

# Creating a Base class 


class Base: 
	def __init__(self): 
		self.a = "GeeksforGeeks"
		self.__c = "GeeksforGeeks"

# Creating a derived class 
class Derived(Base): 
	def __init__(self): 

		# Calling constructor of 
		# Base class 
		Base.__init__(self) 
		print("Calling private member of base class: ") 
		print(self._Base__c)


# Driver code 
obj1 = Base() 
print(obj1.a) 
obj2=Derived()


