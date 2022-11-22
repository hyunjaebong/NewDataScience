def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')
userFunc1()

def userFunc2(x,y):
    print('userFunc2')
    z=x+y
    print('z=',z)
userFunc2(10,20)

def userFunc3(x,y):
    print('userFunc3')
    tot=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return tot,sub,mul,div
x=int(input('x입력: '))
y=int(input('y입력: '))

t,s,m,d = userFunc3(x,y)
print('tot= ', t)
print('sub= ', s)
print('mul= ', m)
print('div= ', d)

