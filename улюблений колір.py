from tkinter import * root = Tk()
val = StringVar()
val.set("blue")
def color():
    label.confing(bg = val.get())
blue = Radiobutton(root, text = "Синій", variable = val, value = "blue", command = color)
blue.pack()
label = Label(root, text = "Текст")
label.pack()
