import pygame
import random
import sys
from pygame.locals import *

pygame.init()

# Keeps game going until set to false by user
running = True

# Screen size
LENGTH = 1221
WIDTH = 1024

# Font of the words
Font = pygame.font.SysFont('comicsans', 30)

# Colors
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GREY = (105, 105, 105)
WHITE = (255, 255, 255)

# Opens the words list
f = open("words.txt", "r")

# Initializes the arrays used

# list of all 5 letter words according to the text file
words = []

# The list of words the user guesses
userWords = []

# The list of words the user guesses but in a 1D array of characters
userWordsArray = []

# The winning word stored as an array of charecters
winningWord = []


def ReadFile():
    for x in range(0, 5757):
        words.append(f.read(6))


ReadFile()


def ChooseRandomWord():
    chooseWord = random.choice(words)
    print(chooseWord)
    return chooseWord


winning = ChooseRandomWord()

# Puts the winning word into an array of single characters
for x in range(len(winning) - 1):
    winningWord.append(winning[x])


# This allows the user to guess words. Should only be called once before checking the users guess
def UserTurn():
    thisTurn = input("Enter your 5 letter word here: ")
    if findLen(thisTurn) != 5:
        print("Enter a FIVE letter word")
    else:
        userWords.append(thisTurn)


# Finds the length of a string
def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter


# Function to find if the letter is in the wrong spot, but still in the word
def YellowLetterFunction(userLetter):
    for k in range(len(winningWord)):
        if winningWord[k] == userLetter:
            return True


# Turns the word into an array of letters

def turnWordIntoArray():
    numberOfWords = int(len(userWordsArray) / 5)
    print(numberOfWords)
    for y in range(5):
        thisWord = userWords[numberOfWords]
        userWordsArray.append(thisWord[y])


def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                return


showOnScreenWord = []


def GetUserWord():
    print("Enter Function")
    enterClick = False

    while not enterClick:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a:
                    showOnScreenWord.append("A")
                if event.key == pygame.K_b:
                    showOnScreenWord.append("B")
                if event.key == pygame.K_c:
                    showOnScreenWord.append("C")
                if event.key == pygame.K_d:
                    showOnScreenWord.append("D")
                if event.key == pygame.K_e:
                    showOnScreenWord.append("E")
                if event.key == pygame.K_f:
                    showOnScreenWord.append("F")
                if event.key == pygame.K_g:
                    showOnScreenWord.append("G")
                if event.key == pygame.K_h:
                    showOnScreenWord.append("H")
                if event.key == pygame.K_i:
                    showOnScreenWord.append("I")
                if event.key == pygame.K_j:
                    showOnScreenWord.append("J")
                if event.key == pygame.K_k:
                    showOnScreenWord.append("K")
                if event.key == pygame.K_l:
                    showOnScreenWord.append("L")
                if event.key == pygame.K_m:
                    showOnScreenWord.append("M")
                if event.key == pygame.K_n:
                    showOnScreenWord.append("n")
                if event.key == pygame.K_o:
                    showOnScreenWord.append("o")
                if event.key == pygame.K_p:
                    showOnScreenWord.append("p")
                if event.key == pygame.K_q:
                    showOnScreenWord.append("q")
                if event.key == pygame.K_r:
                    showOnScreenWord.append("r")
                if event.key == pygame.K_s:
                    showOnScreenWord.append("s")
                if event.key == pygame.K_t:
                    showOnScreenWord.append("t")
                if event.key == pygame.K_u:
                    showOnScreenWord.append("u")
                if event.key == pygame.K_v:
                    showOnScreenWord.append("v")
                if event.key == pygame.K_w:
                    showOnScreenWord.append("w")
                if event.key == pygame.K_x:
                    showOnScreenWord.append("x")
                if event.key == pygame.K_y:
                    showOnScreenWord.append("y")
                if event.key == pygame.K_z:
                    showOnScreenWord.append("z")
                if event.key == pygame.K_RETURN:
                    print(len(showOnScreenWord))
                    if len(showOnScreenWord) == 5:
                        # TODO
                        #Turn the arry into a word and append it to the userWords list
                        #userWords.appen(showOnScreenWord)
                        break;
                        enterClick = True
                    else:
                        print("That is not a valid word")
        PrintWordsToScreen()
        pygame.display.flip()

    # print(showOnScreenWord)
    print("Exit Function")



# Checks and prints the words to the screen
def PrintWordsToScreen():
    for x in range(len(showOnScreenWord)):
            # if the letter is in the right spot it shows it as green
            if winningWord[x] == showOnScreenWord[(x % 5) + int(x/5)]:
                letter = Font.render(showOnScreenWord[(x % 5) + int(x/5)], False, WHITE, GREEN)
                letter = pygame.transform.scale(letter, [157, 157])
                screen.blit(letter, [(int(x/5) * 197) + 40, ((x % 5) * 197) + 40])

            elif YellowLetterFunction(showOnScreenWord[(x % 5) + int(x/5)]):
                letter = Font.render(showOnScreenWord[(x % 5) + int(x/5)], False, WHITE, YELLOW)
                letter = pygame.transform.scale(letter, [157, 157])
                screen.blit(letter, [(int(x/5) * 197) + 40, ((x % 5) * 197) + 40])

            # If the letter is not in the word it makes the letter grey
            else:
                letter = Font.render(showOnScreenWord[(x % 5) + int(x/5)], False, WHITE, GREY)
                letter = pygame.transform.scale(letter, [157, 157])
                screen.blit(letter, [(int(x/5) * 197) + 40, ((x % 5) * 197) + 40])


screen = pygame.display.set_mode([WIDTH, LENGTH])

# Run until the user asks to quit
while running:
    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    GetUserWord()
    UserTurn()
    turnWordIntoArray()

    # Checks if the user wants to quit the game
    #
    #
    # TODO user key strokes for all letters!!
    #
    #


    pygame.display.flip()

pygame.quit()
