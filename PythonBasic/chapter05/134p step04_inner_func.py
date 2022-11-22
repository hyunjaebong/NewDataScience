def a():
    print('a함수')
    def b():
        print('b함수')
    return b
b=a()
b()

data=list(range(1,101))
def outer_func(data):
    dataSet = data
    def tot():
        tot_val=sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return  avg_val
    return tot, avg
tot, avg = outer_func(data)

tot_val=tot()
print(tot_val)
avg_val=avg(tot_val)
print(avg_val)
