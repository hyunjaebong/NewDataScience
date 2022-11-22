# 6. 연봉을 입력받아 월급을 계산하는
# calc_monthly_salary(annual_salary) 함수를 정의하라.
# 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.

def calc_monthly_salary(annual_salary):
    monthly_salary=int(annual_salary/12)
    print(f'월급은 {monthly_salary}원 입니다\n')

while True:
    annual_salary=int(input("연봉을 입력하시오>>> "))
    calc_monthly_salary(annual_salary)