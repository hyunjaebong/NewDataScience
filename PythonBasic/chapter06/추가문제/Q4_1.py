class Restaurant:
    restaurant_name=None
    cuisine_type=None

    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type

    def describe_restaurant(self):
        print(f"\n저희 레스토랑 명칭은 {self.restaurant_name} 이고 {self.cuisine_type} 전문점입니다.")

    def open_restaurant(self):
        print(f"저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요.\n")

    def __del__(self):
        print(f"{self.restaurant_name} 레스토랑 문 닫습니다.")


restaurant=[]

for i in range(3):
     data = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ")
     data = data.split()

     restaurant.append(Restaurant(data[0], data[1]))
     restaurant[i].describe_restaurant()
     restaurant[i].open_restaurant()
     print("\n")


print("\n 저녁 10시가 되었습니다.\n")
