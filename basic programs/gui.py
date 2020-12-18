from tkinter import *

window=Tk()
window.geometry("500x500")
window.title("My Window")
window.configure(bg="red")


def hello():
    print("button clicked")

button1 = Button(window, text="OK", command=hello)
button2 = Button(window, text="OK", command=hello)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)



window.mainloop()

