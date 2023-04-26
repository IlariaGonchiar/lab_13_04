import tkinter
window = tkinter.Tk()
window.title
window.mainloop
from tkinter import TOP, BOTTOM, LEFT, RIGHT
button1 = tkinter.Button(window, text = 'Червоний', width = 10, height = 5, bg = 'red')
button1.pack(side = TOP)
button2 = tkinter.Button(window, text = 'Синій', width = 10, height = 5, bg = 'blue')
button2.pack(side = TOP)
button3 = tkinter.Button(window, text = 'Чорний', width = 10, height = 5, bg = 'black')
button3.pack(side = BOTTOM)
button4 = tkinter.Button(window, text = 'Зелений', width = 10, height = 5, bg = 'green')
button4.pack(side = RIGHT)
