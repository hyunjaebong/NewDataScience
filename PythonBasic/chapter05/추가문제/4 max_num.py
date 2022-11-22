# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라.
# 단 if 문을 사용해서 수를 비교하라.

def print_max(num1,num2,num3):
    if num1>num2:
        max_num=num1
    else:
        max_num=num2

    if max_num<num3:
        max_num=num3

    print(f'가장 큰 수는 {max_num}입니다\n')

while True:
    num = []
    for i in range(3):
        num.append(int(input(f'{i+1}번째 숫자를 입력하세요: ')))
    print_max(num[0],num[1],num[2])