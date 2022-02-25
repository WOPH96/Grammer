#신조어 퀴즈

class Word:
    def __init__(self,new_Word,eg1,eg2,sol):
        self.new_Word = new_Word
        self.eg1 = eg1
        self.eg2 = eg2
        self.sol = sol

    def show_question(self):
        print(f"\"{self.new_Word}\"의 뜻은?")
        print(f"1. {self.eg1}")
        print(f"2. {self.eg2}")
        self.check_answer()
    
    def check_answer(self):
        answer = int(input("=> "))
        if answer == self.sol :
            print("정답입니다.")
        else : 
            print("틀렸습니다.")

word = Word("얼죽아","얼어죽어도 아이스아메리카노","얼굴만은 죽어도 아기피부",1)
word.show_question()
