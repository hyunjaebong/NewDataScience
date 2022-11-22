#입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

sum=0
input_num=0
def find_avg(sum,input_num,num):
    sum+=num
    input_num+=1
    avg=sum/input_num
    return avg,sum,input_num

while True:
    num=int(input("숫자를 입력하시오>>> "))
    avg,sum,input_num=find_avg(sum,input_num,num)
    print(f'지금까지 입력한 모든 수의 평균은 {avg}입니다')