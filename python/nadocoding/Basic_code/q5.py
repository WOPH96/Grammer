from random import *

customer = [randint(5,51) for i in range(50)]

# print(customer)

for i in range(50) :
    print("[{}] {}번째 손님 (소요시간 : {}분)".format("O" if 5<= customer[i]<=15 else " ",i+1 ,customer[i]))