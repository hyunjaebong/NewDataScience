print("원주율=", format(3.14159,"8.3f"))
print("금액=", format(10000,"10d"))
print("금액=", format(125000,"3,d"))

name = "홍길동"
age = 35
price = 125.456
print("이름: %s, 나이:%d, data= %.2f" %(name,age,price))

print("이름: {}, 나이:{}, data= {}".format(name,age,price))

print("이름: {1}, 나이:{0}, data= {2}".format(age,name,price))

uid= input("id input: ")
query = f"select * from member where uid={uid}"
print(query)

