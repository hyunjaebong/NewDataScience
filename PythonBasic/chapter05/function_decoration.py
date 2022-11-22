import time

def my_timestamp (func):
    def decorated(count):
        start = time.time()
        func(count)
        end = time.time() # 정수부는 초, 소수부는 micro 초 단위
        print(f'\n함수 {func} 수행시간: {end-start}, 함수 인자 값 {count}')
    return decorated

@my_timestamp
def print_hello(count):
    for i in range(1, count+1):
        print(f'hello {i}!')

@my_timestamp
def add_operation(count):
    sum = 0
    for i in range(1, count + 1):
        sum+=i

MAX_COUNT = 100000
print_hello(MAX_COUNT)
add_operation(MAX_COUNT)
