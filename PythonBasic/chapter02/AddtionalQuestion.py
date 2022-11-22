# Q1
korean = 80
english = 75
math = 90
science = 95
agv = (korean + english + math + science) / 4
print("평균 :",agv)

# Q2
num = 13
check = (num%2 == 1)
print(int(check))

num = 16
check = (num%2 == 1)
print(int(check))

# Q3
hong = "881120-1068234"
print(hong.index("-"))
print(hong[:6])
print(hong[7:])

# Q4
#print(hong.rfind("1"))
print(hong[7])

#Q5
str = "a:b:c:d"
print(str.replace(":","#"))

#Q6
str2 = ['우리','끝까지',"힘내요!"]
print(f"\"{' '.join(str2)}\"")

