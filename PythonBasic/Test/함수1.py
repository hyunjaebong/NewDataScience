def func1():
    return True

def func2(is_state):
    print(is_state)

# 안의 ()에서 바깥쪽의 ()로 수행
func2(func1())

result = func1()
func2(result)

def func3():
    return [1,2,3,4]