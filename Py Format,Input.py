format
문자열.format()

문자열의 대괄호 자리에 format 뒤의 괄호안에 들어있는 값을 하나씩 넣는다

문자열에 포함된 대괄호 개수 보다 format안에 들어 있는 값의 수가 많으면 정상 동작
print('{} 번 손님'.format(number,greeting))

문자열에 포함된 대괄호 개수 보다 format안에 들어 있는 값의 수가 적으면 에러
print('{} 번 손님 {}'.format(number))


number = 20
welcome = '환영합니다'
base = '{} 번 손님 {}'

     #아래 3개의 print는 같은 값을 출력
print(number,'번 손님',welcome)
print(base.format(number,welcome))
print('{} 번 손님 {}'.format(number,welcome))
     #=>20 번 손님 환영합니다

------------------------------------------------------------------------------------------------------------

사용자 입력 받기

프로그래밍의 3단계
 1.사용자 입력
 2.자료 처리
 3.결과 출력

input()
사용자의 키보드 입력을 return

print('가위 바위 보 중 하나를 내주세요> ', end = ' ')
mine = input()
print('mine:', mine)


간단한 print기능을 내장

mine = input('가위 바위 보 중 하나를 내주세요> ')
print('mine:', mine)

Ctrl + c  프로그램 즉시 종료