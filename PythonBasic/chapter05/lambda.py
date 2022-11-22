def add(a,b):
    return a+b

result = add(5,6)
print(result)

#2 람다 함수 정의
r_add = lambda a, b: a+b
result = r_add(5,6)
print("result2:", result)

# 람다 함수 직접 호출
print((lambda x,y:x+y)(5,6))
#print((lambda x,y: x+y) (5,6))

# 람다 함수와 map
# 일반 함수 버전
def plus_two(x):
    return x + 2


result1 = list(map(plus_two, [1, 2, 3, 4, 5]))
print(result1)

# 람다 함수 버전
result2 = list(map((lambda x: x + 2), [1, 2, 3, 4, 5]))
print(result2)

# 람다 함수와 filter
# 일반 함수 버전
def is_even(x):
    #return x % 2 == 0
    return x % 2 == 1

result1 = list(filter(is_even, range(10)))  # [0 ~ 9]
print(result1)

# 람다 함수 버전
result2 = list(filter((lambda x: x % 2 == 0), range(10)))  # [0 ~ 9]
print(result2)