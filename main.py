#I am making a text typing game
#Type To Burn
import pygame
import random
import time

def getWords():
    f = open('wordList.txt')
    dictionary = f.read().split('\n')
    return dictionary

def randWord(wordList):
    ind = random.randrange(0,len(wordList)-1)
    return wordList[ind]

def main():
    #create screen
    screen = pygame.display.set_mode((960,740))
    image = pygame.image.load("burnSprite.png")
    #screen.blit(image,(64,64))
    hitPts = 0
    text = ''
    badText = ''
    font = pygame.font.Font(None, 32)
    inputBox = pygame.Rect(340,400,240,32)
    healthBar = pygame.Rect(250,600,400,75)
    curHealth =  pygame.Rect(250,600,400-(hitPts*20),75)
    wordList = getWords()
    score = 0
    scoreTxt = "Score: " + str(score)
    word = randWord(wordList)
    running = True

    while running:
        if hitPts == 20:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                i = len(text) + len(badText)
                if event.key == pygame.K_RETURN:
                    if word == text+badText:
                        text = ''
                        badText = ''
                        word = randWord(wordList)
                        score += 1
                        if hitPts > 0:
                            hitPts -= 2
                    else:
                        hitPts += 4
                        screen.fill((145, 15, 15))
                        pygame.display.flip()
                        time.sleep(.05)

                elif event.key == pygame.K_BACKSPACE:
                    if len(badText) > 0:
                        badText = badText[:-1]
                    else:
                        text = text[:-1]
                else:
                    if i >= len(word):
                        badText += event.unicode
                        hitPts += 1
                    elif len(badText) > 0:
                        badText += event.unicode
                        hitPts += 1
                    elif event.unicode != word[i]:
                        badText += event.unicode
                        hitPts += 1
                    else:
                        text += event.unicode

        screen.fill((255,255,255))
        pygame.draw.rect(screen, pygame.Color('black'), inputBox, 2)
        scoreTxt = "Score: " + str(score)
        curHealth =  pygame.Rect(250,600,400-(hitPts*20),75)
        scoreBox = font.render(scoreTxt, True, pygame.Color('black'))
        screen.blit(scoreBox, (800, 50))
        targetWord = font.render(word, True, pygame.Color('Red'))
        screen.blit(targetWord, (200,200))
        badTextBox = font.render(badText, True, pygame.Color('Darkred'))
        goodTextBox = font.render(text, True, pygame.Color('black'))
        screen.blit(goodTextBox, (inputBox.x+5, inputBox.y+5))
        pygame.draw.rect(screen, pygame.Color('Darkred'), healthBar)
        pygame.draw.rect(screen, pygame.Color('Green'), curHealth)
        screen.blit(badTextBox, (goodTextBox.get_width()+inputBox.x+5, inputBox.y+5))
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
