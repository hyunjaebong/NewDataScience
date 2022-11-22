import random

names = ['홍길동','이순신','유관순']
print(names)
print(names[2])

if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 없음')

idx = random.randint(0, 2)
print(f'idx={idx}')
print(names[idx])
