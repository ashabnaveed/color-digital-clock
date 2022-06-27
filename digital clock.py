from tkinter import * 
from tkinter.ttk import *
from time import strftime

draw = Tk()
draw.title('Clock')



def color():
  global string
  string = strftime('%H:%M:%S %p')
  m = string.translate({ord('A'): None})
  x = m.translate({ord('P'): None})
  y =(x.translate({ord('M'): None}))
  z = (y.translate({ord(':'): None}))
  a = (z.translate({ord(' '): None}))
  global colour
  colour = str('#'+a)
  background = colour

color()

def time():
    global lbl
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(draw, font = ('calibri', 40, 'bold'),
            background = colour,
            foreground = 'white')
    
time()

lbl.pack(anchor = 'center')

print(colour)

draw.mainloop()


