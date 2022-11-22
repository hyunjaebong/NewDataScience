
import sys
def solution(num_list):
    #num_list.reverse()
    reversed_list=num_list[::-1]
    print(reversed_list)
   # return answer

num_list = sys.argv[1:]
solution(num_list)