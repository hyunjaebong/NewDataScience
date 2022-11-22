import random

lst = []
for i in range(10):
    r =random.randint(1,10)
    lst.append(r)
print('lst=', lst)

for i in range(10) :
    print(lst[i] * 0.25)

