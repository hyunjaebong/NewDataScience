class Person:


    #생성자
    def __init__(self,age,name,gender):
        self.age=age
        self.name=name
        self.gender=gender

    #메서드
    def display(self):
        print("="*30)
        if self.gender == 'female':
            print("이름:{}, 성별:{}\n나이:{}".format(self.name,"여자",self.age))
        else:
            print("이름:{}, 성별:{}\n나이:{}".format(self.name,"남자",self.age))
        print("="*30)

name=input('이름: ')
age=int(input('나이: '))
gender = input('성별(1.남성, 2.여성): ')
if gender == 1:
    gender = 'male'
else:
    gender = 'female'

ps=Person(name,age,gender)
ps.display()
