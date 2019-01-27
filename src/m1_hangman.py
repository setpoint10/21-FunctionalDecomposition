"""
Hangman.

Authors: Yu Xin and Zhicheng Kai
"""  # DO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random
import rosegraphics as rg

def main():
    # pick_a_word()
    # give_guesses()
    if give_guesses() == 0:
        print('Game over')


def pick_a_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        word = string.split()
        r = random.randrange(0,len(word))
        item = word[r]
        return item

def give_guesses():
    guesses_left=11 - int(input('Choose your difficulty(0~10): '))
    if guesses_left <= 0 or guesses_left> 11:
        print('Can you read the instructions?! type in (0~10)!!')
        print('GG, bro~ You will not be able to pass the game if you cannot read the instruction')
        return 0
    item = pick_a_word()
    # print(item)
    show = []
    for i in range(len(item)):
        show = show + ['*']
    while True:
        guess=input("Your Guess: ")
        print(guess)
        if check_the_word(guess,item)==False:
            guesses_left=guesses_left-1
            print("Remaning Guess(es): ",guesses_left)
            if guesses_left==0:
                print("GG!")
                print(item)
                break
        else:
            a = show_the_true_word(guess,item,show)
            if oh_yeah_thats_good(a,item)==100:
                break

def check_the_word(guess,word):
    if guess in word:
        print("It is in the word! ah!~")
        return True
    else:
        print("You are wrong!")
        return False

def show_the_true_word(guess,item,show):
    if check_the_word(guess,item)==True:
        for k in range(len(item)):
            if item[k] == guess:
                show[k]=guess
    print(show)
    return show

def oh_yeah_thats_good(a,item):
    count = 0
    for k in range(len(item)):
        if a[k] == item[k]:
            count = count +1
    if count == len(item):
        print("oh! yeah! that's! good!!ah~~~~~")
        return 100

main()