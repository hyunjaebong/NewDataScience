def my_div(num1, num2):
    div = div_q = div_r = 0
    try:
        div = num1 / num2
        div_q = num1 // num2
        div_r = num1 % num2
    except Exception as e:
        print(f"오류 발생 : {e}")
        quit()

    return div,div_q,div_r


num1 = int(input("첫번째 수를 입력하여 주세요 : "))
num2 = int(input("두번째 수를 입력하여 주세요 : "))

div,div_q,div_r = my_div(num1, num2)

print(f"나눈 값 : {div}\n몫 : {div_q}\n나머지 : {div_r}")
