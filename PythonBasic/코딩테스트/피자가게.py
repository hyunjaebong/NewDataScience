def solution(n):
   if n%7==0:
      answer = n//7
      return answer
   else:
      answer = n//7+1
      return answer

print(solution(7))
print(solution(1))
print(solution(15))