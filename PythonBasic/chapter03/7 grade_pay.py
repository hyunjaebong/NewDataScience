while True:
    fee=0
    age=int(input('나이를 입력하세요 '))
    if(age>=19 and age<=65):
        grade='성인'
        fee=5000
    elif (age>=14 and age<=18):
        grade='청소년'
        fee=3000
    elif (age>=4 and age<=13):
        grade='어린이'
        fee=2000
    elif (age>=66):
        grade='노인'
    elif (age<=3 and age>=0):
        grade='유아'
    else:
        print('다시 입력하세요\n')
        continue

    if(fee!=0):
        print(f'귀하는 {grade} 등급이며 요금은 {fee}원 입니다')
    else:
        print(f'귀하는 {grade} 등급이며 요금은 무료입니다')