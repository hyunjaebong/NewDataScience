class Restaurant:
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type

    def describe_restaurant(self):
        #정보출력
        print(f'저의 레스토랑 명칭은 {self.restaurant_name}이고 {self.cuisine_type} 전문점입니다.')
    def open_restaurant(self):
        #레스토랑이 열렸다는 메세지 출력
        print(f'저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요.')

name,type=input("레스토랑 이름과 요리 종류를 선택하세요(예 띵호화 중식): ").split(" ")
cl=Restaurant(name,type)
cl.describe_restaurant()
cl.open_restaurant()