# def FizzBuzz_prblem(num):
#     for i in range(1,num+1):
#         if i%3==0:
#             print("FIZZ",":",i)
#         elif i%5==0:
#             print("BUZZ",":",i)
#         elif i%3==0 and i%5==0:
#             print("FIZZBUZZ",":",i)
# FizzBuzz_prblem(100)


# Function to check if the string is a palindrome
# def is_palindrome(s):
#     while len(s) > 1:
#         if s[0] != s[-1]:
#             return False
#         s = s[1:-1]
#     return True
# a=is_palindrome(s = input("Enter your string: "))

# if(a==True):
#     print("palindrom")
# elif (a==False):
#     print("not palindrom")

# def fun(num):
#     sum=0
#     while(num>0):
#         a=num%10
#         sum=sum+a
#         num=num//10
#     print(sum)

# fun(123)

# def duplicate(l):
#     l1=[]
#     if len(l)<=1:
#       print("no any duplicates")
#     else:
#        for i in l:
#           if i not in l1:
#              l1.append(i)
#     print(sorted(l1))

# duplicate([1,2,5,2,1,5,6,6,4,9,4,9])

# def fun1(num):
#     d1={}
#     for i in range(1,num+1):
#         d1.update({i:i**2})
#     print(d1)
# fun1(5)
    
# def sate(s,s1,a):
#     if a==1:
#         print(s.union(s1))
#     elif a==2:
#         print(s.intersection(s1))
#     elif a==3:
#         print(s.difference(s1))
#     else:
#         print("no any operation")
# a=int(input("enter the value"))
# sate({1,2,3,4,5,6},{1,2,4,5,6,1,2},a)


# def fact(n):
    
#     if n==1 or n==0:
#         print("factorial:1")
#     else:
#         return n*fact(n-1)

# fact(5)

# def num(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact

# print(num(5))



# # Original list of tuples
# my_list = [(1, 3), (4, 1), (2, 2), (5, 4)]

# # Sort the list of tuples by the second element of each tuple
# sorted_list = sorted(my_list, key=lambda x: x[1])

# # sorted_list now contains the tuples sorted by their second elements
# print(sorted_list)  # Output: [(4, 1), (2, 2), (1, 3), (5, 4)]

# import datetime
# print(datetime.datetime.today())
# print(datetime.date.today())
# print(datetime.datetime(2022,5,21))
# print(datetime.time())

# def gen(n):
#     x,y=0,1
#     for i in range(n):
#         yield x
#         x,y=y,x+y
       
# l=[]
# a=gen(10)
# for i in a:
#     l.append(i)
# print(l)


# s="tanujapatidar"
# s1=""
# for i in s:
#     s1=i+s1
# print(s1)
s=[]
s1="ioprtehsgdfavcbn"
p=list(s1)
for i in range(len(p)):
    print(p[i])
    
print(s)
  
        




                                

    
                    
