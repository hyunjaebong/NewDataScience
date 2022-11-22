# 5. 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸

def print_5xn(str):
    str_num=int(len(str)/5)
    for i in range(str_num+1):
        print(str[i*5:(i+1)*5])


while True:
    str=input("문자열을 입력하시오>>> ")
    print_5xn(str)
