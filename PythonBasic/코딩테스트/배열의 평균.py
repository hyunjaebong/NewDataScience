def solution(numbers):
    answer = 0
    sum=0
    for i in numbers:
        sum = sum+i
    answer = sum/len(numbers)
    return answer

print(solution(10))