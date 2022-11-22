class Super:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('name: %s, age:%d'%(self.name, self.age))

sup = Super('부모',55)
sup.display()

class Sub(Super):
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print('name: %s, age:%d, gender:%s'%(self.name, self.age, self.gender))
sub = Sub('자식',25,'여자')
sub.display()
