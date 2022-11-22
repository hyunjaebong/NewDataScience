def solution(n):
    answer = 0
    if(0 < n <= 1000):
     for i in range(2,n+1):
      if(i % 2 ==0) :
         answer += i
     return answer
print(solution(4))