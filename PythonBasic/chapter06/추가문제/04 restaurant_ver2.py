class Restaurant:
    restaurant_name=''
    cuisine_type=''

    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type

    def describe_restaurant(self):
        print(f"\n저희 레스토랑 명칭은 {self.restaurant_name} 이고 {self.cuisine_type} 전문점입니다.")

    def open_restaurant(self):
        print(f"저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요.\n")

    def __del__(self):
        print(f"{self.restaurant_name} 레스토랑 문 닫습니다.")


restaurant_list=[]

for num in range(0,3):
    restaurant_name,cuisine_type=input("레스토랑 이름과 요리 종류를 선택하세요.[공백으로 구분] 예) 띵호화 중식 : ").split()
    restaurant_list.append(Restaurant(restaurant_name,cuisine_type))
    restaurant_list[num].describe_restaurant()
    restaurant_list[num].open_restaurant()

print("\n 저녁 10시가 되었습니다.\n")

#for num in range(0,3):
#    del restaurant_list[0]