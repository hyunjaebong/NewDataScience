MAX_BASE_LINE =5
for i in range(MAX_BASE_LINE) :
    for j in range(MAX_BASE_LINE-1-i) :
       print(' ', end='')
    for j in range(i+1) :
       print('*', end='')
    print()