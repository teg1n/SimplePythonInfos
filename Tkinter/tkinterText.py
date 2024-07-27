#udemy üzerinden alınan kurs içeriği
from tkinter import *

screen = Tk()
screen.title("Hello !")
screen.minsize(600 , 600)

label = Label(text="Say 'Hello' to my label")
label.config(bg="blue", fg="white")
label.pack()

def click_button():
    print("button clicked")

button = Button(text="Click" , command=click_button)
button.pack

text = Text(width=30 , height=5  )

text.focus
text.pack()

#scale
def scale_select(value):
    print(value)
scale= Scale(from_=0 , to=100 , command=scale_select)
scale.pack()

#spinboc
def spinbox_select():
    print(spinbox.get())
spinbox = Spinbox(from_=0 , to= 100) 
spinbox.pack()

#checkbutton
checkbutton = Checkbutton(text="Check")
checkbutton.pack()

#radio button

def radio_selected():
    print(radio_checked_state.get())
radio_checked_state = IntVar()

radio_button= Radiobutton(text="1. option", value=10, variable=radio_checked_state)
radio_button2= Radiobutton(text="2. option", value=20, variable=radio_checked_state)
radio_button.pack()
radio_button2.pack()


mainloop()

