import csv
with open('data.csv','w',newline='') as file:
    write=csv.writer(file)
    write.writerow(['Name','Age','Gender'])
    write.writerows(
        [
        ['ram',20,'male'],
        ['syam',20,'male'],
        ['ragini',20,'female'],
        ['radhika',20,'female'],
        ['ravi',20,'female']
        ]
    )

with open("data.csv","r") as fill:
    reder=csv.reader(fill)
    for i in reder:
       print(i)