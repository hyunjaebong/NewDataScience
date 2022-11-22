fat = int(input('지방의 그램을 입력하세요: '))
carbohydrate = int(input('탄수화물의 그램을 입력하세요: '))
protein = int(input('단백질의 그램을 입력하세요: '))

total_calorie= fat *9 + carbohydrate *4 + protein *4


print(f"총 칼로리: {format(total_calorie,'3,d')} cal")