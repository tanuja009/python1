with open("demo.txt","r+") as f:
    a=f.read()
    with open("demo.py","w") as f1:
        s=str(a)
        f1.write(a)

with open("demo.py","r") as t:
    print(t.read())





