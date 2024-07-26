def own_for_loop(iterable):
    iteration1=iter(iterable)
    while True:
        try:
            print(next(iteration1))
        except StopIteration:
            break
a=[1,2,3,4,5,5,6]
b=(1,2,3,4,5,6)
c=range(1,11)
d={1,7,8,9,4,5}
e={1:2,5:6,8:9,10:5}

own_for_loop(e)