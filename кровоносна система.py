import tkinter
window = tkinter.Tk()
window.title("Кровоносна система")
window.mainloop()
def button1_click():
    tkinter.messagebox.showinfo("Відповідь", "Молодець! У тебе добрі знання з біології")
def button2_click():
    tkinter.messagebox.showinfo("Відповідь", "Ти помилився!!!")
button1 = tkinter.Button(window, text = 'Погоджуюсь', command = button1_click)
button1.pack()
button2 = tkinter.Button(window, text = 'Погоджуюсь', command = button2_click)
button2.pack()
