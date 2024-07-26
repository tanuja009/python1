# d={x:x**2 for x in range(2,11) if x%2==0}
# print(d)

# words = ["apple", "banana", "cherry"]
# d={w:len(w) for w in words}
# print(d)

# original = {'a': 1, 'b': 2, 'c': 3}
# d={value:key for key,value in original.items()}
# print(d)

# d={a:"even" if a%2==0 else "odd" for a in range(1,6)} 
# print(d)


# d={x:{x:b for b in range(3)} for x in range(3)}
# print(d)
# product_dict = {(i, j): i * j for i in range(3) for j in range(3)}
# print(product_dict)


# keys = ['name', 'age', 'gender']
# values = ['Alice', 25, 'Female']
# d={k:v for k,v in zip(keys,values)}
# print(d)

d={i:{j*i for j in range(5)} for i in range(5)}
print(d)