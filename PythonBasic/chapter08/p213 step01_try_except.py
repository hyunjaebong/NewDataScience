print('프로그램시작 !!!')
x=[10,30,25.2,'num',14,51]

for i in x:
    print(i)
    y=i**2
    print('y=',y)
print('프로그램 종료')

print('프로그램시작 !!!')
for i in x:
    try:
        y=i**2
        print('i=', i, 'y,=', y)
    except:
        print('숫자 아님: ',i)
print('프로그램 종료')



