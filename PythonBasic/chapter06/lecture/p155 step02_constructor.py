class multiply:
    x=y=0

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def mul(self):
        return self.x * self.y

obj = multiply(10,20)
print('곱셈=', obj.mul())

class multiply2:
    x=y=0

    def __init__(self):
        pass
    def data(self,x,y):
        self.x=x
        self.y=y

    def mul(self):
        return self.x * self.y
obj = multiply2()
obj.data(10,20)
print('곱셈=', obj.mul())