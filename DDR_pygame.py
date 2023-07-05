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
  for x in range(0,4):
    beatmap.append([0,0,0,0])
  for x in range(0,6):
    beatmap.append(beats())
  for x in range(0,10):
    beatmap.append([0,0,0,0])
  beatmap.reverse()
  return beatmap

pygame.init()
screen = pygame.display.set_mode((1280, 720))
#implicitly creates surfact to blit to
pygame.display.set_caption('DDR')
clock = pygame.time.Clock()
running = True
dt = 0

#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#trying to display arrows based on whether it is a 0 or 1 in the beatmap
#displaying them as sprites
#and figure out if pygame can detect multiple inputs at the same time

start = time.time()

bm = beatmap()
for p in range(len(bm)):
  print(bm[p])

while running:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
  interval = 1
  #printed a sprite
  red = pygame.image.load("images/red.png")
  red = pygame.transform.scale(red, (25, 25))
  green = pygame.image.load("images/green.png")
  green = pygame.transform.scale(green, (25, 25))
  green2 = pygame.transform.scale(green, (100, 100))
  #HM idk why it's 8
  for n in range(len(bm)-1, 8, -1):
    screen.fill("black")
    if time.time()-start>=interval:
      for i in range(n, n-10, -1):
        screen.blit(green2, (0,0))
        print("\n\n")
        for j in range (4):
          print ("bm[",i,"][",j,"]: ",bm[i][j])
          if bm[i][j] == 1:
            #print("green")
            screen.blit(green, ((j * 40), 400 + (i - n) * 30))
          else:
            #print("red")
            screen.blit(red, ((j * 40), 400 + (i - n) * 30))
        #pygame.time.delay(500)
        print("N: ", n)
        for p in range(len(bm)):
          print(bm[p])
        pygame.display.flip()
      start = time.time()
  
  #when interval is outside for loop, it cycles through all the arrows, but way too quickly
  #when interval is inside for loop, it does not cycle through, bc the for loop keeps going


  #arrows = pygame.image.load("images/arrows.jpg")
  
  #screen.blit(arrows, (0, 0))
  #pygame.display.flip()

  #pygame.draw.circle(screen, "red", player_pos, 40)
  #pygame.draw.polygon(screen, "red", ((0, 50), (0, 100), (100, 100), (100, 150), (150, 75), (100, 0), (100, 50)))

  # keys = pygame.key.get_pressed()
  # if keys[pygame.K_UP]:
  #     print("UP")
  # if keys[pygame.K_DOWN]:
  #     print("DOWN")
  # if keys[pygame.K_LEFT]:
  #     print("LEFT")
  # if keys[pygame.K_RIGHT]:
  #     print("RIGHT")

  # dt = clock.tick(60) / 1000 
  


pygame.quit()
quit()

#don't know how to draw a caret :P


