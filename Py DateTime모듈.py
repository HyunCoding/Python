datetime
datetime 모듈
날짜와 시간을 사용하게 해주는 라이브러리


christmas_2016이 2016년 12월25일을 값으로 가지는 datetime클래스의 인스턴스가 되도록 만들어 보세요.

import datetime
christmas_2016 = datetime.datetime(2016,12,25)
print(christmas_2016)


datetime은 날짜와 시간을 사용 할 수 있게 해주는 라이브러리입니다.
원하는 날짜와 시간으로 인스턴스를 만들기 위해서는 아래의 예와 같이 사용합니다.

start_time = datetime.datetime(2016, 2, 1)

------------------------------------------------------------------------------------------------------------

코드의 5번째 줄을 수정해서 days_until_christmas 함수가 오늘부터 2030년 12월 25일 사이에 몇일이 있는지를 리턴하도록 만들어 보세요.
(단, 시간단위는 고려하지 마세요.)

import datetime

def days_until_christmas():
    christmas_2030 = datetime.datetime(2030, 12, 25)
    days = christmas_2030 - datetime.datetime.now()
    return days.days

print("{}일".format(days_until_christmas()))


datetime은 -연산을 지원 합니다.
예를 들면,

start_time = datetime.datetime()
how_long = start_time - datetime.datetime.now()
이처럼 -연산을 이용해 start_time으로부터 how_long까지 얼마나 남았는지 구할 수 있습니다.

------------------------------------------------------------------------------------------------------------

timedelta
timedelta 클래스
시간의 연산을 가능하게 해주는 클래스

hundred_after가 지금으로부터 100일 후, 9시 정각을 값으로 가지는 datetime클래스의 인스턴스가 되도록 만들어 보세요. (단, 정각의 기준은 초 단위까지만 맞으면 됩니다.)

import datetime

hundred_after = datetime.datetime.now().replace(hour=9 ,minute=0,second=0) + datetime.timedelta(days = 100)

print("{}/{}/{}  {}:{}:{}".format(hundred_after.year,hundred_after.month, hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))


timedelta 클래스를 이용하여 시간 연산을 해봅시다.

addtime = datetime.timedelta(days = 10)
datetime.datetime.now() + addtime    # 10일 후
datetime.datetime.now() - addtime    # 10일 전

thedate = datetime.datetime.now().replace(hour = 10, minute=0, second = 0)
          + datetime.timedelta(days = 3)       # 3일 후 10시 정각
