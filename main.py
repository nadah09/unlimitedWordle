from english_words import english_words_set
from termcolor import colored
import random

words = {i.lower() for i in english_words_set if len(i) == 5}

def play():
    word = random.sample(words, 1)[0].lower()
    #print(word)
    print("Welcome to Wordle!")
    count = 0
    while True:
        if count == 6:
            print("Game over!")
            return
        inp = input()
        if len(inp) != 5 or inp not in words:
            print("Enter a five letter word!")
            continue
        else:
            count += 1
            colors = ['white']*5
            seen = set()
            if inp.lower() == word:
                print(colored(inp, 'green'))
                return
            for i in range(len(inp)):
                if inp[i] == word[i]:
                    colors[i] = 'green'
                    seen.add(inp[i])
            for i in range(len(inp)):
                if inp[i] in word and colors[i] == 'white' and inp[i] not in seen:
                    colors[i] = 'yellow'
            print("".join([colored(inp[i], colors[i]) for i in range(len(inp))]))



if __name__ == "__main__":
    play()