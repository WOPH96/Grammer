# class ==> 붕어빵
# class Unit:
#     def __init__(self,name,hp,damage): #생성자, 객체가 호출될 때 매번 생성됨
#         self.name = name #self.()의 ()부분 == 멤버 변수
#         self.hp = hp
#         self.damage = damage
#         print("{} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {}, 공격력 {}".format(self.hp,self.damage))

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank1 = Unit("탱크",150,35)
# wraith1 = Unit("레이스",80,5)

# wraith2 = Unit("빼앗은 레이스",80,5)
# wraith2.clocking = True #파이썬은 외부에서 멤버변수 확장가능

# if wraith2.clocking == True:
#     print("{}는 클로킹상태".format(wraith2.name))



class Unit:
    def __init__(self,name,hp,speed): #생성자, 객체가 호출될 때 매번 생성됨
        self.name = name #self.()의 ()부분 == 멤버 변수
        self.hp = hp
        self.speed = speed
        
    def move(self, direction):
        print("[지상 이동 유닛] {} : {} 방향으로 이동합니다 [속도: {}]"\
            .format(self.name,direction,self.speed))

class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage
    
    def attack(self, direction):
        print("{} : {} 방향으로 적군 공격, 공격력 {}".format(\
            self.name, direction, self.damage))

    def hit(self, damaged):
        print("{} : 적군에게 {} 피해 입음".format(\
            self.name, damaged))
        self.hp -= damaged
        print("남은 체력 : {}".format(self.hp if self.hp>=0 else 0))
        if(self.hp <= 0):
            print("파괴되었습니다.")

# firebat1 = AttackUnit("파이어뱃",50,16)

# firebat1.attack("1시")

# firebat1.hit(25)
# firebat1.hit(30)


#드랍쉽 = 공격기능 없음.

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, direction):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]"\
            .format( name, direction, self.flying_speed))


class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage,flying_speed)
        Flyable.__init__(self, flying_speed)

    def move(self,direction):
        print("[공중 비행 유닛] ",end="")
        self.fly(self.name,direction)

# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name,"3시")

# vulture = AttackUnit("벌처",200,3,10)
# vulture.move("1시")
# battlecruiser = FlyableAttackUnit("배틀크루저",1000,5,3)
# battlecruiser.move("5시")

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0) # self는 안한다!!
        self.location = location

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")