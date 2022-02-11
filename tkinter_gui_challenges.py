from tkinter import *
def call():
    msg = Label(window, text = "You pressed the button")
    msg.place(x=30, y=50)
    button["bg"]="blue"
    button["fg"]="white"

window = Tk()
window.title("Pressed title")
window.geometry("200x110")
button = Button(text = "Press me", command = call)
button.place(x=30,y=20,width=120,height=25)
window.mainloop()
