class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print("저희 레스토랑 명칭은 [ %s ]이고 [ %s ] 전문점입니다." %(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("저희 [ %s ] 레스토랑 오픈했습니다. 어서오세요" %self.restaurant_name)

    def __del__(self):
         print("%s 레스토랑 문 닫습니다." %self.restaurant_name)


restaurant=[]
for i in range(3):
     data = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ")
     data = data.split()

     restaurant.append(Restaurant(data[0], data[1]))
     restaurant[i].describe_restaurant()
     restaurant[i].open_restaurant()
     print("\n")

print("저녁 10시가 되었습니다.")