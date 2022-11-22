class Rectangle:
    width=height=0

    #생성자
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area_calc(self):
        area=self.width*self.height
        return area
    def circum_calc(self):
        circum=(self.width+self.height)*2
        return circum

print('-'*30)
w=int(input("넓이를 입력하세요: "))
h=int(input("높이를 입력하세요: "))
rec=Rectangle(w, h)

area = rec.area_calc()
print('사각형의 넓이:', area)

circum=rec.circum_calc()
print('사각형의 둘레:',circum)
print('-'*30)




