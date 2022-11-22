import random

def coffee_lotto(student_list, target_num):

    temp_student_list = random.sample(student_list, target_num)

    temp_student_list = ' '.join(temp_student_list)

    print(f'\n축하합니다\n{temp_student_list} 당첨입니다.')

    print('\n프로그램 종료\n재 실행')

def presentation_order(student_list):


    join_student_list = ' '.join(student_list)

    print("\n< 학생 명단 >")
    print(join_student_list)

    print("\n발표자 순서는 아래와 같습니다.")


    select_student = random.sample(student_list, len(student_list))

    join_student_list = ' '.join(select_student)
    print(join_student_list)

while True:

    select = input("\n\t1. 커피 로또\n\t2. 발표자 순서\n\n메뉴를 선택하세요 ( 엔터는 종료 ) : ")

    student_base_list = ['김유진', '문성준', '박종민', '송지예', '양석훈', '이예지', '임성혁', '한권제', '현재봉']
    class_all_list = student_base_list
    class_all_list.append('이현구')

    if select == '1':
        target_num=int(input("당첨자 수를 입력 하세요 : "))
        coffee_lotto(class_all_list, target_num)

    elif select == '2':
        presentation_order(student_base_list)

    else:
        quit()