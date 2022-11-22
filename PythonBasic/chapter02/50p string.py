#(1)왼쪽 기준
oneLine = "this is one line string"
print(oneLine)
print("문자열 길이:", len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:]) #전체 원소
print(oneLine[::2]) #2의 배수 index

#(2)오른쪽 기준
print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

#(3)부분 문자열 생성
subString = oneLine[-11:]
print(subString)
