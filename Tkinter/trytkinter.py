#udemy üzerinden alınan kurs içeriği
import tkinter

#screen
screen = tkinter.Tk()
screen.title("Tkinter")
screen.minsize(300 , 300)

#label
myLabel = tkinter.Label(text="this is a lable")
myLabel.pack()

#button
def click_button():
    userInput= myEntry.get
    print(userInput)
myButton = tkinter.Button(text="This is a button" , command=click_button)
myButton.pack()

#entry
myEntry = tkinter.Entry(width=20)
myEntry.pack()


screen.mainloop()