age = int(input('나이를 등록하세요: '))

if age >=0 and age<3:
    print('귀하는 유아등급이며 요금은 무료입니다')
elif age >=4 and age<13:
    print('귀하는 어린이등급이며 요금은 2000원입니다')
elif age >=14 and age<18:
    print('귀하는 청소년등급이며 요금은 3000원입니다')
elif age >=19 and age<65:
    print('귀하는 성인요금은 5000원입니다')
elif age >=65:
    print('귀하는 노인등급이며 요금은 무료입니다.')
