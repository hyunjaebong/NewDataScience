import random


def coin(n):
    result = []
    for i in range(n):
        r=random.randint(0,1)
        if(r==1):
            result.append(1)
        else:
            result.append(0)
    return result
print(coin(10))

def montaCoin(n):
    cnt=0
    for i in range(n):
        cnt += coin(1)[0]
    result = cnt /n
    return result

print(montaCoin(10))
print(montaCoin(30))
print(montaCoin(100))
print(montaCoin(1000))
print(montaCoin(10000))
