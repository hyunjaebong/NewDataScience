import random

lotto = random.randint(1,10)

while lotto:
    input_value = int(input('1~10까지 숫자를 입력하세요: '))
    print(lotto)
    if lotto == input_value :
        print('성공')
        break
    elif input_value>lotto:
        print('더 작은 수를 입력하세요')
    else :
        print('더 큰 수를 입력하세요')
