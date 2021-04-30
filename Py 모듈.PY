모듈 사용하기

Math(수학모듈)

import math
r = 10
파이 = 2 * math.pi * r
print(파이)

------------------------------------------------------------------------------------------------------------
Random(랜덤모듈)

from random import*
import random

Hlist = []

for i in range(45):
    Hlist.append(i+1)

print(Hlist)
lotto = random.sample(Hlist, 6)
lotto.sort()
print(lotto)

------------------------------------------------------------------------------------------------------------

lotto2 = random.sample(range(1,46), 6)
lotto2.sort()
print(lotto2)