i=tot=10
i += 1 #i=i+1
tot += i #tot = tot+i
print(i,tot)

#print('출력')
print('출력',end=' , ')
print('출력')

#안녕하세요 반갑습니다.
print('안녕하세요', end=' ')
print('반갑습니다')

v1,v2=100,200
v2,v1=v1,v2
print('v1=',v1,'v2=',v2)

lst=[1,2,3,4,5]
v1,*v2= lst
print(v1,v2)

*v1, v2=lst
print(v1,v2)