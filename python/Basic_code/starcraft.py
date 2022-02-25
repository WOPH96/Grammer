from random import *

class Unit:
    def __init__(self,name,hp,speed): #생성자, 객체가 호출될 때 매번 생성됨
        self.name = name #self.()의 ()부분 == 멤버 변수
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다.".format(self.name))
        
    def move(self, direction):
        print("[지상 이동 유닛] {} : {} 방향으로 이동합니다 [속도: {}]"\
            .format(self.name,direction,self.speed))

    def hit(self, damaged):
        print("{} : 적군에게 {} 피해 입음".format(\
            self.name, damaged),end="\t")
        self.hp -= damaged
        print("남은 체력 : {}".format(self.hp if self.hp>=0 else 0))
        if(self.hp <= 0):
            print("파괴되었습니다.")

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, direction):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
            .format( name, direction, self.flying_speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage
    
    def attack(self, direction):
        print("{} : {} 방향으로 적군 공격, 공격력 {}".format(\
            self.name, direction, self.damage))

class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage,flying_speed)
        Flyable.__init__(self, flying_speed)

    def move(self,direction):
        print("[공중 비행 유닛] ",end="")
        self.fly(self.name,direction)

#마린
class Marine(AttackUnit):
    def __init__(self):
        super().__init__("마린", 40, speed=1, damage=5)
    
    #스팀팩: 일정시간동안 이동 및 공격 속도 증가, 체력 10감소

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.[현재 체력 : {}]".format(self.name,self.hp))

class Tank(AttackUnit):
    #시즈모드 : 탱크 고정, 높은 파워 공격
    seize_developed = False

    def __init__(self):
        super().__init__("탱크",150,speed=1,damage=35)
        self.seize_mode = False
        self.default_speed = self.speed

    def set_seize_mode(self):
        if Tank.seize_developed == False:  # 코딩 스킬인듯 
            return
        
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다".format(self.name))
            self.damage *=2
            self.speed = 0
            self.seize_mode = True
        else:
            print("{} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.speed = self.default_speed
            self.seize_mode = False

class Wraith(FlyableAttackUnit):
    #클로킹 모드 있음:
    clocking_developed = False

    def __init__(self):
        super().__init__("레이스",80,20,5)
        self.clocked = False # 처음만들땐 해제상태

    def clocking(self):
        if self.clocking_developed == False:
            return
        if self.clocked == False:
            print("{} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocked= True
        else:
            print("{} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked= False


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player]님이 게임에서 퇴장하셨습니다.")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

#유닛 일괄 관리

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)


for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
Wraith.clocking_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")
print("[알림] 레이스 클로킹모드 개발이 완료되었습니다.")

#공격 모드 준비 (마린: 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")
        

for unit in attack_units:
    unit.hit(randint(5,21)) # 공격은 랜덤으로 받음 (5~20)

game_over()


