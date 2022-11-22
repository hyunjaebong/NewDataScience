t=(10,)
print(t)

t2=(1,2,3,4,5,3)
print(t2)

print(t2[0], t2[1:4], t2[-1])

#t2[0]=10

for i in t2:
    print(i, end=' ')

if 6 in t2:
    print("6 있음")
else:
    print("6 없음")