def add_number4(first, second):
    result = first + second
    return result

first_num = int(input("첫번째 수를 입력하세요: "))
second_num = int(input("두번째 수를 입력하세요: "))
print(f'{first_num} + {second_num} = {add_number4(first_num,second_num)}')
print(f'{first_num} + {second_num} = {add_number4(1,2)}')
print(f'{first_num} + {second_num} = {add_number4(second_num,first_num)}')
result = add_number4(2,3)