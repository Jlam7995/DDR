import keyboard
#from tkinter import *
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
  bm = []
  #temporarily commenting out the empties
  for x in range(0,4):
    bm.append([0,0,0,0])
  for x in range(0,10):
    bm.append(beats())
  bm.reverse()
  beatmap = []
  for x in bm:
    row = " ".join(map(str, x))
    #joins into list
    beatmap.append(row)
  #up till now, the entire beatmap is now a list of strings
  return beatmap

def main(stdscr):
  bm = beatmap()
  #disables blinking cursor
  curses.curs_set(0)
  #reverse direction to print in
  for i in range(len(bm)-10, -1, -1):
    stdscr.addstr(0,0,"\n".join(bm[i:i+10]))
    #stdscr.addstr(0,0,"foo\nbar")
    #print(x, end='\r')
    time.sleep(1)
    stdscr.refresh()

  #detecting keypresses
  while True:
    if keyboard.is_pressed("left"):
      print ('You pressed the left arrow')
    if keyboard.is_pressed("right"):
      print ('You pressed the right arrow')
    if keyboard.is_pressed("down"):
      print ('You pressed the down arrow')
    if keyboard.is_pressed("up"):
      print ('You pressed the up arrow')
    if keyboard.is_pressed("m"):
      break

wrapper(main)

stdscr = curses.initscr()
main(stdscr)

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