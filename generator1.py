# def gen_demo():
#     yield "statemen1"
#     yield "statemen2"
#     yield "statemen3"

# gen=gen_demo()
# print(next(gen))
# for i in gen:
#     print(i)


# def gen_demo(num):
#     for i in range(1,num):
#         yield i**2
   
# gen=gen_demo(21)
# print(next(gen))
# print(next(gen))
# l=[]
# for i in gen:
#     l.append(i)
# print(l)
# l=[]
# def mera_range(start,end):
#     for i in range(start,end):
#         yield i
# for i in mera_range(15,30):
#     l.append(i)
# print(l)
# l1=[]
# gen=(i**2 for i in range(1,10))
# for i in gen:
#     l1.append(i)

# print(l1)

def fibbo(num):
    x,y=0,1
    for i in range(num):
        x,y=y,x+y
        return x
def square(num):
    for i in range(num):
        yield i**2

f=fibbo(10)
t=square(10)
for i in t:
    print(i)