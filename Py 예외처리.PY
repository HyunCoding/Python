try except 예외 처리

try:
    # 에러가 발생할 가능성이 있는 코드
except Exception: # 에러 종류
    #에러가 발생 했을 경우 처리할 코드

경우에 따라 예외 처리 대신 if else를 사용 할 수 있다.

try:
    a = 3/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

------------------------------------------------------------------------------------------------------------

예외의 이름을 모를 때
예외 이름을 모르는 경우 처리 방법

try:
    # 에러가 발생할 가능성이 있는 코드
except Exception as ex: # 에러 종류
    print('에러가 발생 했습니다', ex) # ex는 발생한 에러의 이름을 받아오는 변수

try:
    a = 5
    b = 0
    c = a / b
except Exception as ex:
    print('다음과 같은 에러가 발생했습니다: {}'.format(ex))

------------------------------------------------------------------------------------------------------------

raise 예외 발생
사용자가 직접 에러를 발생시키는 기능

raise Exception # 에러 종류
많이 사용하면 코드를 읽기 어려워진다.


shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
for shop, products in shops.items():
    for product, price in products.items():
        if product =='풀':
            print("{}: {}원".format(shop, price))


StopIteration 예외처리
더이상 값을 가져오고 싶지않을때 쓰는 예외처리

풀을 파는 가게를 발견하면 for문 전체를 즉시 종료하고 싶습니다. 
for 문을 try/except로 감싸고 print문 다음에 raise StopIteration을 추가해서 풀을 파는 가게를 하나만 출력하도록 만들어 보세요.
except문에서는 StopIteration을 지정해 주어야 합니다.

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product =='풀':
                print("{}: {}원".format(shop, price))
                raise StopIteration
except StopIteration:
    print('종료')

------------------------------------------------------------------------------------------------------------

내 예외 만들기
예외 정의
사용자가 직접 예외처리를 하면 코드의 직관성을 높일 수 있다.
파일을 하나 만들어 예외를 정의
Exception 클래스를 상속받아 만든다

try:
    sign_up( )
except BadUserName:
    print( "이름으로 사용할 수 없는 입력" )
except PasswordNotMatched:
    print( "입력한 패스워드 불일치")


다음 코드는 문구점 3곳을 검사하면서 풀이 있으면 문구점의 이름과 가격을 출력하고 
MyException을 raise해서 즉시 for in문 전체를 종료합니다. 
코드의 2번째 줄에 Exception클래스를 상속받는 MyException이라는 예외 클래스를 만들어 보세요.

class MyException(Exception):
    pass

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product == '풀':
                print("{}: {}원".format(shop, price))
                raise MyException
except MyException:
    print("풀을 찾았습니다.")