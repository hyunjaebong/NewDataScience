x=50
def local_func(x):
    x +=50
    print(f'지역변수x: {x}')

def pringt_x():
    print(f'함수에서 전역변수 일기 시도: {x}')
    x += 50

local_func(x)
print(f'전역변수 x= {x}')


def global_func():
    global x
    x += 50
global_func()
print('x=', x)