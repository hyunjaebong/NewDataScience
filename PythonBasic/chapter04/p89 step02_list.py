x=[1,2,3,4]
y=[1.5,2.5]
z=x+y
print(z)

x.extend(y)
print(x)

x.append(y)
print(x)

lst=[1,2,3,4]
result = lst*2
print(result)

result.sort()
print(result)

result.sort(reverse=True)
print(result)

import random
r=[]
for i in range(5):
    r.append(random.randint(1,5))
print(r)

if 4 in r:
    print('있음')
else:
    print('없음')

