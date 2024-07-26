with open("file1.txt","w") as f:
    f.write("msdksjhnchdscbxbcbdhbcgflblflmcbmkcfvkbmkmc")
with open("file1.txt","r") as f:
    a=f.read()
# for i in a:
#     l=i.strip()
# w=[l.replace(a,"hello guys") for l in a]
# print(w)
b=a.replace(a,"hello guys this is our coding tech")
with open("file1.txt","w") as f:
    f.write(b)
with open("file1.txt","r") as f:
    print(f.read())