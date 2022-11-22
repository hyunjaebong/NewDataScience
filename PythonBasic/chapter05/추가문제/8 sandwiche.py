def input_ingredient():
    ingredient_list=[]
    while True:
        ingredient=input("안녕하세요. 원하시는 재료를 입력하세요: ")
        if ingredient=='종료':
            print()
            return ingredient_list
        ingredient_list.append(ingredient)

def make_sandwiches(ingredient_list):
    print("샌드위치를 만들겠습니다")
    for i in range(len(ingredient_list)):
        print(f'{ingredient_list[i]}를 추가합니다')
    print('여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.\n')


while True:
    option=int(input("""안녕하세요. 저희 가게에 방문해 주세서 감사합니다.
1. 주문
2. 종료
입력: """))

    if option==1:
        ingredient_list=input_ingredient()
        make_sandwiches(ingredient_list)
    elif option==2:
        print('주문을 종료합니다.')
        break
    else:
        print("잘못된 접근입니다\n")