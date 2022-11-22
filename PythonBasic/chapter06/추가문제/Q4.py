class Restaurant:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def restaurant_name(self):
        print(f'저의 레스토랑 명칭은{name}이고 {type}전문점입니다.')

    def describe_restaurant(self):
        print(f'저의 {name} 레스토랑 오픈했습니다. 어서오세요')

name,type=input("레스토랑 이름과 요리 종류를 선택하세요. 예) 띵호화 중식 : ").split()
rest=Restaurant(name,type)
rest.restaurant_name()
rest.describe_restaurant()
