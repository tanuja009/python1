# l=[10,20,30,40,50,60]
# l.insert(2,70)
# print(l)   
# l.remove(30)
# l.pop()
# l1=l[:3:]
# print(l1)  
# print(l+l1)
# p=[x**2 for x in range(1,10)]
# print(p)
# if 20 in l:
#     print("true")
# l.extend(l1)
# print(l)
L=[5,1,6,7,4,1,2,5,6]
L.sort()#permanantaly sort
print(L)


p=[]
for i in range(len(L)-1,-1,-1):
    p.append(L[i])
print(p)


lst = [1, 2, 3, 4, 5]
reversed_lst = [lst[i] for i in range(len(lst)-1, -1, -1)]
print(reversed_lst)  # Output: [5, 4, 3, 2, 1]


lst = [1, 2, 3, 4, 5]
stack = lst[:]
reversed_lst = []
while stack:
    reversed_lst.append(stack.pop())
print(reversed_lst)  # Output: [5, 4, 3, 2, 1]

