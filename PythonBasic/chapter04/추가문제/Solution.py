# Q1
a = [1, 3, 5, 4, 2]
a.sort( )
a.reverse( )
#a.sort(reverse=True)
print(a)

# Q2
a = (1, 2, 3)
a = a + (4,)
print(a)       # (1, 2, 3, 4) 출력

# Q3
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)            # {'A':90, 'C':70} 출력
print(result)       # 80 출력

# Q4
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)     # a 리스트를 집합자료형으로 변환
b = list(aSet)    # 집합자료형을 리스트 자료형으로 다시 변환
print(b)          # [1,2,3,4,5] 출력

# Q5

shop = {'kim99': 12000,
        'lee66': 11000,
        'han55': 3000,
        'hong77': 5000,
        'hwang33': 18000}
num = 1

for k in shop: # k = key
    print(f'{num}. 아이디: {k}, 마일리지: {shop[k]}점')
    num += 1

# Q6
TARGET_ID = 'han55'
shop[TARGET_ID] = 5000

# Q6-1
for id in shop:
    if id == TARGET_ID:
        print(f'{id}님의 마일리지가 {shop[id]}점으로 수정되었습니다.')
# Q6-2
print(f'{TARGET_ID}님의 마일리지가 {shop.get(TARGET_ID)}점으로 수정되었습니다.')

# Q7
TARGET_ID = 'jang88'
shop[TARGET_ID] = 7000
print(f'전체 딕셔너리 : {shop}')
print(f'{TARGET_ID}님의 마일리지가 {shop.get(TARGET_ID)}점으로 수정되었습니다.')

# Q8
score = []

for id in shop:
    score.append(shop[id])

result = max(score)  # result에 최댓값 저장

for id in shop:
    if shop[id] == result:
        max_id = id

print(f'{max_id}님의 {result}점이 가장 높은 점수입니다.')

# Q9
temperature = {'월': 25.5,
               '화': 28.3,
               '수': 33.2,
               '목': 32.1,
               '금': 17.3,
               '토': 35.3,
               '일': 33.3}

LINE_NUM = 54
print('-' * LINE_NUM)
#day가 key
for day in temperature:
    print(f'  {day}\t', end='')

print()
print('-' * LINE_NUM)
#key의 value를 구함.
for day in temperature:
    print(f' {temperature[day]}\t', end='')

print()
print('-' * LINE_NUM)

# Q10
temperature_list = []

for day in temperature:
    temperature_list.append(temperature[day])

result = min(temperature_list)
print('가장 낮은 최고 기온 : %.1f˚' % result)

# Q11
result = []
#키를 통해 value가 30도 이상으로 구함
for day in temperature:
    if temperature[day] >= 30:
        result.append(day)

print('기온이 30˚ 이상인 요일 : ', end='')

# for r in range(len(result)):
#     if r == len(result) - 1:  # 마지막 요일은 , 표시 X
#         print(result[r], end='')
#     else:
#         print(result[r], end=', ')
print(f"{', '.join(result)}")

# Q12
sum = 0  # 합계를 저장할 변수(sum)

for day in temperature:
    sum += temperature[day]

avg = sum / len(temperature)  # 평균

print('일주일간 최고 기온의 평균 : %.1f˚' % avg)


