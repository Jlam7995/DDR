import pygame
import random
import time
from time import sleep

def beats():
  list = [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)]
  while list.count(1) > 2:
    change = random.randint(0, list.count(1)-1)
    #so if change is 3, that's only if all are 1s
    #if change is 2, then if the 3rd isn't, the 4th has to be
    while (list[change] != 1):
      change += 1
    list[change] = 0
  return list

def beatmap():
  beatmap = []
  for x in range(0,23):
    beatmap.append([0,0,0,0])
  for x in range(0,432):
    beatmap.append(beats())
  for x in range(0,4):
    beatmap.append([0,0,0,0])
  beatmap.reverse()
  return beatmap

def printsprite(i, j):
  blank = pygame.image.load("images/blank.png").convert_alpha()
  blank = pygame.transform.scale(blank, (25, 25))
  hold = pygame.image.load("images/arrow-emptier.png")
  hold = pygame.transform.scale(hold, (115, 25))
  left = pygame.image.load("images/arrow-left.png").convert_alpha()
  left = pygame.transform.scale(left, (25, 25))
  up = pygame.image.load("images/arrow-up.png").convert_alpha()
  up = pygame.transform.scale(up, (25, 25))
  down = pygame.image.load("images/arrow-down.png").convert_alpha()
  down = pygame.transform.scale(down, (25, 25))
  right = pygame.image.load("images/arrow-right.png").convert_alpha()
  right = pygame.transform.scale(right, (25, 25))
  screen.blit(hold, (0, 400))
  pygame.display.flip()
  if bm[i][j] == 1:
    if j == 0:
      screen.blit(left, ((j * 30), 400 + (i - n) * 30))
    elif j == 1:
      screen.blit(down, ((j * 30), 400 + (i - n) * 30))
    elif j == 2:
      screen.blit(up, ((j * 30), 400 + (i - n) * 30))
    elif j == 3:
      screen.blit(right, ((j * 30), 400 + (i - n) * 30))
  else:
    #print("red")
    screen.blit(blank, ((j * 30), 400 + (i - n) * 30))

pygame.init()
screen = pygame.display.set_mode((720, 480))
#implicitly creates surface to blit to
pygame.display.set_caption('DDR')
clock = pygame.time.Clock()
running = True
dt = 0

#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#trying to display arrows based on whether it is a 0 or 1 in the beatmap
#displaying them as sprites
#and figure out if pygame can detect multiple inputs at the same time

pygame.mixer.music.load("Love_Story_8Bit.mp3")
bm = beatmap()
x = True
running = True
begin = True
while running or x == False:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
  
  interval = .5
  score = 0
  n = len(bm)-1
  #for setup as global variable
  check = [0, 0, 0, 0]
  mybigfont = pygame.font.SysFont("monospace", 25)
  mybigbigfont = pygame.font.SysFont("monospace", 100)
  myfont = pygame.font.SysFont("monospace", 10)
  blue = (70, 130, 180)
  if begin == True:
    start = time.time()
    gamestart = mybigfont.render("To start the game, press enter", 1, blue)
    screen.blit(gamestart, (40, 40))
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RETURN:
        screen.fill((0,0,0))
        pygame.mixer.music.play()
        #HM idk why it's 8, but it works lol
        while n > 8 or x == False:
          restart = myfont.render("To restart the game, press r", 1, blue)
          screen.blit(restart, (500, 400))
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                check[0] = 1
              elif event.key == pygame.K_DOWN:
                check[1] = 1
              elif event.key == pygame.K_UP:
                check[2] = 1
              elif event.key == pygame.K_RIGHT:
                check[3] = 1
              if event.key == pygame.K_r:
                score = 0
                screen.fill((0,0,0))
                n = len(bm) -1
                x = False
                break
                #breaks me out of if2
            if x == False:
              break
              #breaks me out of for
          if x == False:
            x = True
            break
            #breaks me out of while n
          if time.time()-start>=interval:
            if bm[n] == check:
              score +=1
            #print(score)
            pygame.draw.rect(screen,(0, 0, 0),pygame.Rect(580, 440, 140, 40))
            scoring = myfont.render("Score: " + str(score), 1, blue)
            screen.blit(scoring, (580, 440))
            n -= 1
            #print (time.time()-start)
            for i in range(n, n-10, -1):
              for j in range (4):
                printsprite(i,j)
              pygame.display.flip()
            start = time.time()
            #to clear value for checking score
            check = [0, 0, 0, 0] 
            screen.fill((0,0,0))
        if n == 8:
          #running = False
          begin = False
          gameend = mybigfont.render("To restart the game, press enter", 1, blue)
          score = mybigbigfont.render("Score: " + str(score), 1, blue)
          screen.fill((0,0,0))
          screen.blit(gameend, (40, 40))
          screen.blit(score, (160, 160))
  
  #need to get rid of all the if breaks, there's too many
  #maybe put everything in a function so i can return instead
  #made arrows into arrows. Have placeholder. Does not look ideal but works
  #maybe handmake beatmap
  
  #screen.blit(arrows, (0, 0))
  #pygame.display.flip()

  #pygame.draw.circle(screen, "red", player_pos, 40)
  #pygame.draw.polygon(screen, "red", ((0, 50), (0, 100), (100, 100), (100, 150), (150, 75), (100, 0), (100, 50)))


pygame.quit()
quit()

#don't know how to draw a caret :P


