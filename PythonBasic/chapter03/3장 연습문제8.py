age = int(input('나이를 등록하세요: '))
grade = ''

if age >=0 and age<3:
    grade = '유아'
    charge = 0
elif age >=4 and age<13:
    grade = '어린이'
    charge = 2000
elif age >=14 and age<18:
    grade = '청소년'
    charge = 3000
elif age >=19 and age<65:
    grade = '성년'
    charge = 5000
elif age >=65:
    grade = '노인'
    charge = 0
print(f"귀하는 '{grade}'등급이며 요금은' {charge} '입니다.")

charge = int(input("요금을 입력하세요: "))
if grade =='어린이'  :
    gap = 2000-charge
    if 2000>charge :
        print(f"{gap}'가 모자랍니다. 입력하신'{charge}를 반환합니다.")
    else :
        print(f"감사합니다. 티켓을 발행합니다.")
elif grade =='청소년'  :
    gap = 3000-charge
    if 3000>charge :
        print(f"{gap}'가 모자랍니다. 입력하신'{charge}를 반환합니다.")
    else :
        print(f"감사합니다. 티켓을 발행합니다.")
elif grade =='성년'  :
    gap = 5000-charge
    if 5000>charge :
        print(f"{gap}'가 모자랍니다. 입력하신'{charge}를 반환합니다.")
    else :
        print(f"감사합니다. 티켓을 발행합니다.")
else:
    if gap -charge <0:
        print(f"{gap}'가 모자랍니다. 입력하신'{charge}를 반환합니다.")
    else :
        print(f"감사합니다. 티켓을 발행합니다.")
