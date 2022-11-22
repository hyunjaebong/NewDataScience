size = int(input('vector수: '))

lst = []
for i in range(size):
    lst.append(int(input()))

print('vector크기: ', len(lst))

if int(input()) in lst:
    print('YES')
else:
    print('NO')
