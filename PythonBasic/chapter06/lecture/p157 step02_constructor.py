class multiply3:
    def data(self,x,y):
        self.x=x
        self.y=y
    def mul(self):
        result = self.x * self.y
        self.display(result)

    def display(self, result):
        print("곱셈= %d" %(result))
obj = multiply3()
obj.data(10,20)
obj.mul()