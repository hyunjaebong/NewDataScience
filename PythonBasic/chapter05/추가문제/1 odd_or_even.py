def odd_or_even(num):
    if num%2==0:
        print(f"숫자 {num}은 짝수 입니다")
    else:
        print(f"숫자 {num}은 홀수 입니다")

while True:
    num=int(input("숫자를 입력하시오>>> "))
    odd_or_even(num)