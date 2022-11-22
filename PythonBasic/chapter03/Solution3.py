scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for score in scores :
    sum += score
average = sum / len(scores)
print(f'평균 점수 {average}')