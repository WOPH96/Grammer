#hangman game

from random import *

words = ["apple","banana","orange"]
word = choice(words)


print("answer = ",word)

letters = "" #지금까지 입력받은 모든 알파벳

while True:
    done = True
    print()
    for w in word:
        if w in letters:
            print(w,end=" ")
        else:
            print("_",end=" ")
            done = False
    print()
    
    if done:
        print("Succed!!")
        break

    letter = input("Input letter > ")

    if letter not in letters:
        letters += letter

    if letter in word:
        print("Correct!")
    else:
        print("Wrong.")
    

    

