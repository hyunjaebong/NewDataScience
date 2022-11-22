#문제1
su=5
dan=800
print(f'su 주소:',{id(su)})
print(f'dan 주소',{id(dan)})
sum=su*dan
print('금액= ', sum)

#문제2
x=2
y= 2.5 * (x**2) + (3.3*x) + 6
print(f'2차방정식 결과: ',{y})

#문제3
fat = int(input("지방의 그램을 입력하세요: "))
protein =  int(input("탄수화물의 그램을 입력하세요: "))
carbor =  int(input("단백질의 그램을 입력하세요: "))
totalCal = (fat*9) + (protein*4) + (carbor*4)
print(f'총 칼로리: ', {format(totalCal, '3,d')}, 'cal')

#문제4
word1 = input('첫번째 단어:' )
word2 = input('두번째 단어:' )
word3 = input('세번째 단어:' )
firsttext = word1[0] + word2[0] + word3[0]
print('====================')
print(f'약자: ', {firsttext})
