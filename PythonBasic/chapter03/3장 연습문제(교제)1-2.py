weight = int(input('짐의 무게는 얼마입니까?'))
if weight>=10:
    price = (weight//10) *10000
    print('수수료는 '+format(price,'3,d')+'입니다.')

else:
    print('수수료는 없습니다.')

