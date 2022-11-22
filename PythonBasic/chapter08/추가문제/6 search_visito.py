def search_visitor(check_name):
    with open("방명록.txt","r",encoding="UTF-8") as file:
        visitor = file.read()
        if visitor.find(name) == -1:
            # if name in visitor:
            return False
        return True

name = input('이름을 입력하세요  ( 예 : 홍길동 )  : ')

is_visit = search_visitor(name)
print(is_visit)
if is_visit :
    print(f'{name}님 다시 방문해 주셔서 감사합니다. 즐거운 시간 되세요.')
else:
    birthday=int(input('생년월일을 입력 하세요 ( 예 : 900327 ) : '))
    with open("방명록.txt",'a',encoding='UTF-8') as file:
        file.write(f"\n{name} {birthday}")
    print(f"{name}님 환영합니다. 아래 내용을 입력하셨습니다.")
    print(f"{name} {birthday}")

