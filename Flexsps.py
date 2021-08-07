import tkinter
from tkinter import*
from tkinter.font import Font
from tkinter import messagebox
import pyttsx3
import time
import cv2
import random as r



window=Tk()
window.title("Flex SPS")
window.geometry('600x650')
window.resizable(width='false',height='false')
window.config(bg='#00008B')
window.iconbitmap('.icon\\SPSicon.ico')

engine=pyttsx3.init()

rate=engine.getProperty('rate')
engine.setProperty('rate',160)

volume=engine.getProperty('volume')
engine.setProperty('volume',1.0)

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


Name=""

def is_Mess():
    global Name
    Name = nameEntr.get()
    #print(Name)
    #print(len(Name))

    if (len(Name) >= 1):
        if (len(Name)) >= 4:
            entError.config(text="Let's Play "+Name,fg='#F4C430')
            engine.say("Hey. hello "+ Name )
            engine.say("I am Flex. Hit the start button to play with me.")
            engine.runAndWait()
        else:
            messagebox.showerror('Name Error','Enter the Correct Name!!!')
            entError.config(text="Enter the Correct Name!!!",fg='red')
    else:
        messagebox.showerror('Name Error', 'Enter the your Name first!!!')
        entError.config(text="Enter the your Name firs!!!", fg='red')

def is_game():
    if (len(Name) >=1 ):
        if (len(Name) >=4):
            while True:
                gamlis = ["Stone", "Paper", "Scissor"]
                time.sleep(3)
                for i in gamlis:
                    engine.say(i)
                    engine.runAndWait()
                saveError.config(text=gamlis)

                stone = ".img1\\stone.png"
                paper = ".img2\\paper.png"
                sicessor = ".img3\\sicessor.png"

                comdis = r.choice([stone, paper, sicessor])

                time.sleep(2)

                img = cv2.imread(comdis)

                #print(comdis)
                cv2.imshow("Computer Answer", img)


                exc = cv2.waitKey(1) & 0XFF
                if exc == ord('c'):
                    break
            cv2.destroyAllWindows()
            nameEntr.delete(0,END)
            copyInfor.config(text="Have a greate day by Flex World...")
        else:
            messagebox.showerror('Name Error','Enter the correct name and save it!!!')
    else:
        messagebox.showerror('Name Error', 'Enter the  Name first and save it!!!')




titLab=Label(window,text="Welcome to Flex World",fg='white',bg='#00008B',font=("times",25,"bold","italic"),relief="raised")
titLab.pack(fill=X)

namLab=Label(window,text='Enter your Name:',fg='white',bg='#00008B',pady=30,font=('times',19,'bold','italic'))
namLab.pack(fill=X)

nameEntr=StringVar()
nameEntr=Entry(window,textvariable=nameEntr,width=20,fg='#00008B',font=("jost",15,'bold','roman'),selectbackground='#00008B')
nameEntr.pack()

padLab=Label(window,bg='#00008B',pady=5)
padLab.pack()

texSave=Button(window,text='Save...',fg='blue',bg='white',font=("arial",15,'bold','roman'),activebackground='blue',activeforeground='white',command=is_Mess)
texSave.pack()

entError=Label(window,text="",fg='#F4C430',bg='#00008B',pady=20,font=("arial",15,'bold','roman'))
entError.pack()

texStart=Button(window,text='Start...',fg='blue',bg='white',font=("arial",15,'bold','roman'),activebackground='blue',activeforeground='white',command=is_game)
texStart.pack()

saveError=Label(window,text="",fg='#F4C430',bg='#00008B',pady=100,font=("arial",30,'bold','roman'))
saveError.pack()


copyInfor=Label(window,text="Flex World",fg='white',bg='Black',pady=10,font=("times",15,'bold','italic'),relief="raised")
copyInfor.pack(side='bottom',fill=X)

window.mainloop()
