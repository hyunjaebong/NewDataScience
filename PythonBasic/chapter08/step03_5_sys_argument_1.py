import sys
def operation_mode(mode):
    if mode == '절전모드':
        pass
    elif mode == '최대모드':
        pass
    elif mode == '고속모드':
        pass

def set_operator(name):
    pass
def set_code(code):
    pass

args = sys.argv[:]

print(args)
print(args[1:])

for argument in args:
    print(argument)

operation_mode(args[1])
print(f'{args[1]} 로 동작하겠습니다.')
print(f'동작은 {args[2]}에 의해 수행되었습니다.')
print(f'작업 코드는 {args[3]}')

