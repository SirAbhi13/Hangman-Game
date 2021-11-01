import pygame
import random
import math

#pygame setup
pygame.init()
WIDTH, HEIGHT = 1200,900
dis = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('HANGMAN GAME!')

#button variables

RADIUS = 30
GAP = 20
letters = []
startx = round((WIDTH - (RADIUS *2 + GAP)*13)/2)
starty = 700
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS *2 +GAP) * (i%13))
    y = starty + ((i//13)* (GAP + RADIUS * 2))
    letters.append([x , y, chr(A+i), True])



#fonts
LETTER_FONT = pygame.font.SysFont('verdana', 40)
WORD_FONT = pygame.font.SysFont('verdana', 60)
TITLE_FONT = pygame.font.SysFont('verdana', 70)

#images
items = []
for i in range(7):
    load_image = pygame.image.load("image" + str(i) + ".png") 
    items.append(load_image)

    
# game variables
hangman_status =0 
words = ["ANIMATION", "BUTTERFLY", "PYTHON", "PYGAME", "MATHEMATICS", "DEVELOPMENT", "BIRTHDAY"]
word = random.choice(words)
guessed = []

#colour variables
WHITE = (255,255,255)
BLACK = (0,0,0)



def draw():
    #background colour
    dis.fill(WHITE)
    
    # draw title
    text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    dis.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    dis.blit(text, (400, 200))
    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        pygame.draw.circle(dis, BLACK, (x, y), RADIUS, 3)
        text = LETTER_FONT.render(ltr, 1 , BLACK)
        dis.blit(text, (x- text.get_width()/2 , y - text.get_height()/2))

    dis.blit(items[hangman_status], (50,100))  
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    dis.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    dis.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status
    #game loop
    FPS = 100
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
            
        draw()        
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("You Won!")
            break

        if hangman_status == 6:
            display_message("You LOST!")
            break
while True:
    main()
    pygame.quit()
