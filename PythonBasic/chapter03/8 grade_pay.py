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

    if(fee==0):
        print(f'귀하는 {grade} 등급이며 요금은 무료입니다')
    else:
        print(f'귀하는 {grade} 등급이며 요금은 {fee}원 입니다')

        pay = int(input('요금을 입력하세요 '))
        if (pay>fee):
            print(f'"감사합니다. 티컷을 발행하고 거스름돈 {pay-fee}원을 반환 합니다."\n')
        elif (pay<fee):
            print(f'"{fee-pay}가 모자랍니다. 입력 하신 {pay}원를 반환합니다."\n')
        else:
            print(f'"감사합니다. 티컷을 발행합니다."\n')
