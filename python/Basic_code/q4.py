from random import *

comment = [i for i in range(1,21)]

shuffle(comment)
#sample(comment,3)

reward = list(set(sample(comment,4)))


print("-- 당첨자 발표-- ")
print("치킨 당첨자 : {} ".format(reward[0]))
print("커피 당첨자 : {} ".format(reward[1:]))
print("-- 축하합니다-- ")