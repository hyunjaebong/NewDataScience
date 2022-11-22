class Car:
    cc=0
    door=0
    carType=None

    def __init__(self,cc,door,carType):
        self.cc=cc
        self.door=door
        self.carType=carType

    def display(self):
        print("자동차 %d cc이고, 문짝은 %d개, 타입은 %s" %(self.cc, self.door, self.carType))

car1 = Car(2000,4,"승용차")
car2 = Car(3000,5,"SUV")

car1.display()
car2.display()