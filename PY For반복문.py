for in list

for in 반복문
코드를 필요한만큼 반복해서 실행

for pattern in patterns:
    print (pattern)

리스트 patterns의 값을 하나씩 꺼내 pattern으로 전달
리스트의 길이만큼 print (pattern) 실행

------------------------------------------------------------------------------------------------------------

for in range
range 함수
필요한 만큼의 숫자를 만들어내는 유용한 기능

for i in range(5):
    print(i)


enumerate
리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능

names = ['철수', '영희', '영수']
for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))

------------------------------------------------------------------------------------------------------------

break, continue

break
반복문을 종료시키는 기능

sizes에는 진열된 바지 사이즈의 목록이 들어 있습니다. 다음 코드는 사이즈가 32인 바지의 위치를 모두 출력하고 있는데요.
5번째줄을 수정해서 사이즈가 32인 바지의 위치를 한 번만 출력하고 프로그램이 종료되도록 만들어 보세요.
sizes = [33,35,34,37,32,35,39,32,35,29]
for i,size in enumerate(sizes):
    if size == 32:
        print("사이즈 32인 바지는 {}번째에 있다.".format(i+1))
        break# 여기에 코드를 추가하세요


continue
반복문의 나머지 부분을 보지 않고, 반복문의 처음으로 돌아가는 기능

다음 코드는 numbers에 있는 튜플을 받아들여서 튜플의 첫번째 숫자를 두번째 숫자로 나누는 일을 합니다. 
이 때, b가 0이면 "0으로 나눌 수는 없습니다."라고 출력하는데요. 
이 if else문에서 continue문을 이용하여 else를 사용하지 않도록 변경해 보세요.
numbers = [ (1,2),(10,0) ]

for a,b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue# 이 부분이 else문에 들어있지 않도록 수정해야 합니다.
    print("{}를 {}로 나누면 {}".format(a,b,a/b))