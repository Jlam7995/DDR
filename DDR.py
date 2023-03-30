# import keyboard
# from tkinter import *
import curses
from curses import wrapper
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
  #temporarily commenting out the empties
  for x in range(0,4):
    beatmap.append([0,0,0,0])
  for x in range(0,10):
    beatmap.append(beats())
  return beatmap

def main(stdscr):
  bm = beatmap()
  bm.reverse()
  #disables blinking cursor
  curses.curs_set(0)
  rows = []
  for x in bm:
    row = " ".join(map(str, x))
    rows.append(row)
    #print(row)
    #print("foo")
    y = 0
    while y<len(rows):
      if y % 10 == 9: 
        print (rows[y])
      y+=1
    #stdscr.addstr(0,0,row)
    #stdscr.refresh()
    #print(x, end='\r')
    #time.sleep(1)

wrapper(main)

#stdscr = curses.initscr()
#main(stdscr)

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