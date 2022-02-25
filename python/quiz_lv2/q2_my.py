#hangman game

from random import *

def printf(idx, answer):
    for i in range(len(answer)):
        if i in idx:
            print(answer[i]+" ",end="")
        else:
            print("_ ",end="")

answers = ["apple","banana","orange"]

answer = sample(answers,1)[0]
print (answer)
idx = set()
while len(idx) != len(answer) :
    
    printf(idx,answer)
    letter = input("\nInput letter > ")

    cnt = 0
    cORw = 0
    for spell in answer :
        if letter == spell:
            idx.add(cnt)
            cORw +=1
        cnt+=1    
    print("Correct" if cORw>0 else "Wrong")
    cnt=0
    cORw=0

printf(idx,answer)
print("\nSucceed")




     

