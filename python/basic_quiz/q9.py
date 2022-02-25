from ctypes.wintypes import MSG
from socket import MsgFlag


class SoldOutError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

chicken = 10
waiting = 1

try:
    while True:
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken : 
            print("재료가 부족하여 주문에 실패하였습니다")
        
        elif not isinstance(order,int) or order < 1:
            raise ValueError

        else:
            print("[대기번호 {}] {}마리 주문이 완료되었습니다."\
                .format(waiting,order))
            chicken-=order
            waiting+=1
        if  chicken == 0 :
            raise SoldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
except ValueError:
    print("잘못된 값을 입력하였습니다.")

except SoldOutError as err:
    print(err)

finally : print("이용해주셔서 감사합니다.")
#except Exception as err: