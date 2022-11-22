# 7. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
# www.naver.com
def make_url(str):
    return 'www.'+str+'.com'

while True:
    str=input("인터넷 주소로 만들 문자열을 입력하시오>>> ")
    url=make_url(str)
    print(f'만들어진 url은 다음과 같습니다: {url}')
