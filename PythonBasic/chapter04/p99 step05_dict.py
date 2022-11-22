dic = dict(key1 =100, key2=200, key3=300)
print(dic)

person ={'name':'홍길동','age':35,'address':'서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

person['age'] = 45
print(person)

del person['address']
print(person)

person['pay'] = 350
print(person)

print(person['age'])
print('age' in person)

for key in person.keys():
    print(key)
for v in person.values():
    print(v)
for i in person.items():
    print(i)
