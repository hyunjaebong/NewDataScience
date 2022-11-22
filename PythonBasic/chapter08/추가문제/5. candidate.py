def show_candidates(candidate_list):
    # print(candidate_list)
    for name in candidate_list:
        print(name)

def make_idol(candidate_list):
    for name in candidate_list:
        print(f'신예 아이돌 {name} 인기 급상승')

def make_world_star(candidate_list):
    for name in candidate_list:
        print(f'아이돌 {name} 월드스타 등극')

candidates_list=[]
with open('연습생.txt', 'r',encoding='UTF-8') as file:
    names = file.readlines()
    for name in names:
        candidates_list.append(name.strip())

show_candidates(candidates_list)
print()
make_idol(candidates_list)
print()
make_world_star(candidates_list)