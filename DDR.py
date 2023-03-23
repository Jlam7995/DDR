# import keyboard
# from tkinter import *
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


for x in range(0,10):
    = beats()


if __name__ == '__main__':
        # print('First line', end='\r')
        # print('Second line', end='\r')
        print('< ^ v >', end='\r')
        print('< ^ v  ', end='\r')
        print('foo')
        sleep(1)

# tk = Tk()
# tk.title("DDR Game")
# tk.resizable(0,0)
# tk.wm_attributes("-topmost", 1)
# canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
# canvas.pack()
# tk.update()

# print("< ^ v >")
# while True:
#     if keyboard.is_pressed("left arrow"):
#         print("Left Arrow Pressed")
#         break