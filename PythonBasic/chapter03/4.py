sum=0

for i in range(1,101):
    if i%3==0 and i%2!=0:
        print(i, end=' ')
        sum+=i
print('누적합:',sum)