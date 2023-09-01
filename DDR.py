import pygame
import random
import time
from time import sleep

def beats(i):
  list = [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)]
  if i == 0:
    while list.count(1) > 2:
      change = random.randint(0, list.count(1)-1)
      #so if change is 3, that's only if all are 1s
      #if change is 2, then if the 3rd isn't, the 4th has to be
      while (list[change] != 1):
        change += 1
      list[change] = 0
  elif i == 1:
    while list.count(1) > 1:
      change = random.randint(0, list.count(1)-1)
      #so if change is 3, that's only if all are 1s
      #if change is 2, then if the 3rd isn't, the 4th has to be
      while (list[change] != 1):
        change += 1
      list[change] = 0
  return list

def beatmap(i):
  beatmap = []
  #need 24 blank beats
  for x in range(0,24):
    beatmap.append([0,0,0,0])
  #for testing
  #for x in range(0,5):
    #beatmap.append([1,1,1,1])
  for x in range(0,432):
    beatmap.append(beats(i))
  for x in range(0,4):
    beatmap.append([0,0,0,0])
  beatmap.reverse()
  return beatmap

def printsprite(i, j):
  blank = pygame.image.load("images/blank.png").convert_alpha()
  blank = pygame.transform.scale(blank, (75, 75))
  empty = pygame.image.load("images/arrow-emptier.png")
  empty = pygame.transform.scale(empty, (300, 100))
  left = pygame.image.load("images/arrow-left.png").convert_alpha()
  left = pygame.transform.scale(left, (80, 100))
  up = pygame.image.load("images/arrow-up.png").convert_alpha()
  up = pygame.transform.scale(up, (80, 100))
  down = pygame.image.load("images/arrow-down.png").convert_alpha()
  down = pygame.transform.scale(down, (80, 100))
  right = pygame.image.load("images/arrow-right.png").convert_alpha()
  right = pygame.transform.scale(right, (80, 100))
  screen.blit(empty, (0, 600))
  if bm[i][j] == 1:
    if j == 0:
      screen.blit(left, ((j * 75), 600 + (i - n) * 75))
    elif j == 1:
      screen.blit(down, ((j * 75), 600 + (i - n) * 75))
    elif j == 2:
      screen.blit(up, ((j * 75), 600 + (i - n) * 75))
    elif j == 3:
      screen.blit(right, ((j * 75), 600 + (i - n) * 75))
  else:
    screen.blit(blank, ((j * 75), 600 + (i - n) * 75))

pygame.init()
screen = pygame.display.set_mode((1080, 720))
#implicitly creates surface to blit to
pygame.display.set_caption('DDR')
running = True

pygame.mixer.music.load("Love_Story_8Bit.mp3")
x = True
running = True
begin = True
while running or x == False:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
  interval = .5
  #I hate this interval. something is wrong. maybe around .4
  score = 0
  #for setup as global variable
  check = [0, 0, 0, 0]
  mybigfont = pygame.font.SysFont("monospace", 50)
  titlefont = pygame.font.SysFont("monospace", 200)
  myfont = pygame.font.SysFont("monospace", 25)
  blue = (70, 130, 180)
  red = (255, 8, 0)
  green = (0, 255, 0)
  if begin == True:
    start = time.time()
    title = titlefont.render("DDR", 1, green)
    gamestart = mybigfont.render("To start the game:", 1, blue)
    screen.blit(title, (400, 0))
    screen.blit(gamestart, (40, 300))
    offset = 0.3
    start2 = start + offset
  gameeasy = mybigfont.render("Easy mode: press e", 1, blue)
  gamehard = mybigfont.render("Hard mode: press h", 1, blue)
  screen.blit(gameeasy, (40, 340))
  screen.blit(gamehard, (40, 380))
  miss = mybigfont.render("Miss", 1, red)
  hit = mybigfont.render("Hit", 1, green)
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_e or event.key == pygame.K_h:
        if event.key == pygame.K_e:
          bm = beatmap(1)
        elif event.key == pygame.K_h:
          bm = beatmap(0)
        n = len(bm)-1
        screen.fill((0,0,0))
        pygame.mixer.music.play()
        #HM idk why it's 6, but it works lol
        while n > 6 or x == False:
          restart = myfont.render("To restart the game, press r", 1, blue)
          screen.blit(restart, (40, 40))
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_LEFT:
                check[0] = 1
                print("left")
              elif event.key == pygame.K_DOWN:
                check[1] = 1
                print("down")
              elif event.key == pygame.K_UP:
                check[2] = 1
                print("up")
              elif event.key == pygame.K_RIGHT:
                check[3] = 1
                print("right")
              if event.key == pygame.K_r:
                score = 0
                screen.fill((0,0,0))
                n = len(bm) -1
                x = False
                pygame.mixer.music.stop()
                break
                #breaks me out of if2
            #print(time.time()-start)
            if x == False:
              break
              #breaks me out of for
          if x == False:
            x = True
            break
            #breaks me out of while n
          if time.time()-start>=interval: 
            n -= 1
            screen.fill((0,0,0))
            for i in range(n, n-8, -1):
              for j in range (4):
                printsprite(i,j)
            start = time.time()
          if time.time()-start2>=interval: 
            print("should be" + str(bm[n]))
            print("pressing" + str(check))
            if bm[n] == check:
              score +=1
              screen.blit(hit, (580, 60))
            else:
              screen.blit(miss, (580, 60))
            pygame.draw.rect(screen,(0, 0, 0),pygame.Rect(580, 440, 140, 40))
            scoring = myfont.render("Score: " + str(score), 1, blue)
            screen.blit(scoring, (580, 440))
            pygame.display.flip()
            start2 = start + offset
            #to clear value for checking score
            check = [0, 0, 0, 0] 
        if n == 6:
          #running = False
          begin = False
          gameend = mybigfont.render("To restart the game, press enter", 1, blue)
          score = titlefont.render("Score: " + str(score), 1, blue)
          screen.fill((0,0,0))
          screen.blit(gameend, (40, 40))
          screen.blit(score, (160, 160))
  
  #need to get rid of all the if breaks, there's too many
  #maybe put everything in a function so i can return instead
  #made arrows into arrows. Have placeholder. Does not look ideal but works

  #extra credit
  #maybe handmake beatmap
  #maybe save high scores - local
  #combo?

pygame.quit()
quit()