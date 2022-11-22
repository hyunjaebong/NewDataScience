x=[2,4,1,5,7]
#print(x**2)

lst=[i**2 for i in x]
print(lst)

num=list(range(1,11))

lst2=[i*2 for i in num if i%2==0]
print(lst2)
