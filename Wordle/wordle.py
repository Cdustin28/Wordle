import pygame
import random
import sys
import time
import requests


# The gameMode and chose by the player in the menu
gameMode = ""
currentPlayerRow = -1

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
RED = (255,40,40)






#TODO
def CheckProfile():
    profile = open("profile.txt", "r")
    return profile.readlines()

myDict = {}
listOfLists = []
profilesList = CheckProfile()
for line in profilesList:
    listOfLists.append(line.split(" "))
print(listOfLists)


# Initializes the arrays used

# list of all 5-letter words according to the text file
words = []

# The list of words the user guesses
userWords = []

# The list of words the user guesses but in a 1D array of characters
userWordsArray = []

# The winning word stored as an array of characters
winningWord = []

# If the player wins or not
gameOver = False


# Opens the words list
def ReadFile():
    f = open("words.txt", "r")
    for x in range(0, 5757):
        words.append(f.read(6))


ReadFile()


# Use an API to implement
def RealWord(word):
    wordAPI = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    wordAPI = wordAPI + word
    response = requests.get(wordAPI)
    return response.status_code == 200


def PlayerWin():
    global gameOver
    if numberOfGreen == 5:
        gameOver = True




def ChooseRandomWord():
    chooseWord = random.choice(words)
    chooseWord = chooseWord.upper()
    return chooseWord


winning = ChooseRandomWord()
print(winning)

# Puts the winning word into an array of single characters
for x in range(len(winning) - 1):
    winningWord.append(winning[x])


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


showOnScreenWord = []
hardMode = []


def HardMode():
    print(hardMode)
    if gameMode == "Easy":
        return True
    if gameMode == "Hard":
        for letter in hardMode:
            if letter not in showOnScreenWord:
                return False
    return True


def TurnArrayIntoWord(array):
    newWord = ""
    for r in range(5):
        newWord = newWord + array[r]
    print(newWord)
    return newWord

def GetUserWord():
    enterClick = False
    newWord = ""
    while(len(userWords) < 6):
        if gameOver:
            print("You Won!!")
            break

        while not enterClick:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:

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
                        showOnScreenWord.append("N")
                    if event.key == pygame.K_o:
                        showOnScreenWord.append("O")
                    if event.key == pygame.K_p:
                        showOnScreenWord.append("P")
                    if event.key == pygame.K_q:
                        showOnScreenWord.append("Q")
                    if event.key == pygame.K_r:
                        showOnScreenWord.append("R")
                    if event.key == pygame.K_s:
                        showOnScreenWord.append("S")
                    if event.key == pygame.K_t:
                        showOnScreenWord.append("T")
                    if event.key == pygame.K_u:
                        showOnScreenWord.append("U")
                    if event.key == pygame.K_v:
                        showOnScreenWord.append("V")
                    if event.key == pygame.K_w:
                        showOnScreenWord.append("W")
                    if event.key == pygame.K_x:
                        showOnScreenWord.append("X")
                    if event.key == pygame.K_y:
                        showOnScreenWord.append("Y")
                    if event.key == pygame.K_z:
                        showOnScreenWord.append("Z")
                    if event.key == pygame.K_BACKSPACE and len(showOnScreenWord) > 0:
                        showOnScreenWord.pop(len(showOnScreenWord) - 1)
                    if len(showOnScreenWord) == 6:
                        showOnScreenWord.pop(5)

                    if event.key == pygame.K_RETURN:
                        if len(showOnScreenWord) == 5 and HardMode() and RealWord(TurnArrayIntoWord(showOnScreenWord)):

                            for r in range(len(showOnScreenWord)):
                                userWordsArray.append(showOnScreenWord[r])
                                newWord = newWord + showOnScreenWord[r]
                            enterClick = True

                            break;
                        else:
                            print("That is not a valid word")
            screen.fill((100, 100, 100))
            PrintWordsToScreen()
            ColorWords()
            pygame.display.update()
        userWords.append(newWord)
        print(userWords)
        print(userWordsArray)
        ColorWords()



        showOnScreenWord.clear()
        newWord = ""
        enterClick = False


def PrintWordsToScreen():

   for x in range(len(showOnScreenWord)):
        letter = Font.render(showOnScreenWord[x % 5], False, WHITE, GREY)
        letter = pygame.transform.scale(letter, [157, 157])

        screen.blit(letter, [((x % 5) * 197) + 40, (len(userWords) * 197) + 40])


# Checks and prints the words to the screen
def ColorWords():
    global numberOfGreen
    numberOfGreen = 0
    for x in range(len(userWordsArray)):
        # If the letter is in the right spot it shows it as green
        if winningWord[x%5] == userWordsArray[x]:
            letter = Font.render(userWordsArray[x], False, WHITE, GREEN)
            letter = pygame.transform.scale(letter, [157, 157])
            screen.blit(letter, [((x % 5) * 197) + 40, (int(x / 5) * 197) + 40])
            if userWordsArray[x] not in hardMode:
                hardMode.append(userWordsArray[x])
            numberOfGreen += 1

        elif YellowLetterFunction(userWordsArray[x]):
            letter = Font.render(userWordsArray[x], False, WHITE, YELLOW)
            letter = pygame.transform.scale(letter, [157, 157])
            screen.blit(letter, [((x % 5) * 197) + 40, (int(x / 5) * 197) + 40])
            if userWordsArray[x] not in hardMode:
                hardMode.append(userWordsArray[x])
            numberOfGreen = 0

        # If the letter is not in the word it makes the letter grey
        else:
            letter = Font.render(userWordsArray[x], False, WHITE, GREY)
            letter = pygame.transform.scale(letter, [157, 157])
            screen.blit(letter, [((x % 5) * 197) + 40, (int(x / 5) * 197) + 40])
            numberOfGreen = 0

    PlayerWin()
    numberOfGreen = 0
    pygame.display.update()


screen = pygame.display.set_mode([WIDTH, LENGTH])
playersName = ""


def Menu():
    username = Font.render("Type your username", False, WHITE, GREY)
    username = pygame.transform.scale(username, [944, 250])
    wordle = Font.render("WORDLE", False, WHITE, GREY)
    wordle = pygame.transform.scale(wordle, [944, 250])
    easy = Font.render("Easy Mode", False, WHITE, GREY)
    easy = pygame.transform.scale(easy, [600, 250])
    hard = Font.render("Hard Mode", False, WHITE, GREY)
    hard = pygame.transform.scale(hard, [600, 250])
    global playersName
    enteredUsername = []
    notClicked = True
    global gameMode
    screen.blit(username, [40, 100])
    pygame.display.update()
    while (notClicked):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    enteredUsername.append("A")
                if event.key == pygame.K_b:
                    enteredUsername.append("B")
                if event.key == pygame.K_c:
                    enteredUsername.append("C")
                if event.key == pygame.K_d:
                    enteredUsername.append("D")
                if event.key == pygame.K_e:
                    enteredUsername.append("E")
                if event.key == pygame.K_f:
                    enteredUsername.append("F")
                if event.key == pygame.K_g:
                    enteredUsername.append("G")
                if event.key == pygame.K_h:
                    enteredUsername.append("H")
                if event.key == pygame.K_i:
                    enteredUsername.append("I")
                if event.key == pygame.K_j:
                    enteredUsername.append("J")
                if event.key == pygame.K_k:
                    enteredUsername.append("K")
                if event.key == pygame.K_l:
                    enteredUsername.append("L")
                if event.key == pygame.K_m:
                    enteredUsername.append("M")
                if event.key == pygame.K_n:
                    enteredUsername.append("N")
                if event.key == pygame.K_o:
                    enteredUsername.append("O")
                if event.key == pygame.K_p:
                    enteredUsername.append("P")
                if event.key == pygame.K_q:
                    enteredUsername.append("Q")
                if event.key == pygame.K_r:
                    enteredUsername.append("R")
                if event.key == pygame.K_s:
                    enteredUsername.append("S")
                if event.key == pygame.K_t:
                    enteredUsername.append("T")
                if event.key == pygame.K_u:
                    enteredUsername.append("U")
                if event.key == pygame.K_v:
                    enteredUsername.append("V")
                if event.key == pygame.K_w:
                    enteredUsername.append("W")
                if event.key == pygame.K_x:
                    enteredUsername.append("X")
                if event.key == pygame.K_y:
                    enteredUsername.append("Y")
                if event.key == pygame.K_z:
                    enteredUsername.append("Z")
                if event.key == pygame.K_RETURN:
                    for r in range(len(enteredUsername)):
                        playersName = playersName + enteredUsername[r]

                    notClicked = False
            if playersName != "":
                newProfile = open("profile.txt", "a")
                writeIt = True
                for p in range(len(listOfLists)):
                    if listOfLists[p][0] == playersName:

                        writeIt = False

                if writeIt:
                    newProfile.write("\n" + playersName)
                playersName = ""




    screen.blit(wordle, [40, 100])
    screen.blit(easy, [200, 600])
    screen.blit(hard, [200, 900])
    pygame.display.update()
    notClicked = True


    while(notClicked):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos[0])
                if pos[0] >= 200 and pos[0] <= 800 and pos[1] >= 600 and pos[1] <= 850:
                    notClicked = False
                    gameMode = "Easy"

                if pos[0] >= 200 and pos[0] <= 800 and pos[1] >= 900 and pos[1] <= 1150:
                    notClicked = False
                    gameMode = "Hard"




def DisplayDidWin():
    screen.fill((100, 100, 100))
    winner = Font.render("You Win", False, WHITE, GREEN)
    winner = pygame.transform.scale(winner, [600, 250])
    loser = Font.render("You Lose", False, WHITE, RED)
    loser = pygame.transform.scale(loser, [600, 250])

    if gameOver:
        while (True):
            screen.blit(winner, [200, 400])
            pygame.display.update()
            time.sleep(0.5)
            screen.fill((100, 100, 100))
            pygame.display.update()
            time.sleep(0.5)
            for event in pygame.event.get():

                screen.fill((100, 100, 100))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    return
    else:
        while True:
            screen.blit(loser, [200, 400])
            pygame.display.update()
            time.sleep(1)
            screen.fill((100, 100, 100))
            pygame.display.update()
            time.sleep(1)
            screen.fill((100, 100, 100))
            for event in pygame.event.get():

                screen.fill((100, 100, 100))
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    return



# Run until the user asks to quit
while running:

    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    Menu()
    print("Game Mode:" + gameMode)
    GetUserWord()

    winning = ChooseRandomWord()
    print(winning)
    winningWord.clear()
    userWords.clear()
    userWordsArray.clear()
    DisplayDidWin()
    print(winningWord)


    for x in range(len(winning) - 1):
        winningWord.append(winning[x])

    gameOver = False


    pygame.display.flip()


pygame.quit()
