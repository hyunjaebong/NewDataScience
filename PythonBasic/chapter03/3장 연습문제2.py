i=sum=0
dataset = []

while i<1000:
    i += 1
    if i%3 ==0:
        sum += i

print('1~100사이 3의 배수 합=%d' %sum)