while True:
    age=int(input('나이를 입력하세요 '))
#    if(age>=19 and age<=65):
    if 19 <= age <= 65:
            fee=5000
    elif (age>=14 and age<=18):
        fee=3000
    elif (age>=4 and age<=13):
        fee=2000
    else:
        fee=0
    if(fee!=0):
        print(f'요금은 {fee}원 입니다')
    else:
        print(f'요금은 무료입니다')