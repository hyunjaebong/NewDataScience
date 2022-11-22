with open('메모장.txt', 'w', encoding='UTF-8') as file:
        message = input("메세지를 입력 하세요 : ")
        for i in range(1, 10):
            file.write(f'{message}{i}\n')
            print(f'{message}{i}')
