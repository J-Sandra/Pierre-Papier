from random import randint
from tkinter import *

def aug(mon,ton):
    global t,m
    if mon==1 and ton==2:
        t+=1
    elif mon==2 and ton==1:
        m+=1
    elif mon==1 and ton==3:
        m+=1
    elif mon==3 and ton==1:
        t+=1
    elif mon==2 and ton==3:
        t+=1
    elif mon==3 and ton==2:
        m+=1
def jouer(ton):
    global score2,score1,t,m
    mon=randint(1,3)
    if mon==1:
            lab2.configure(image=pierre)
    elif mon==2:
            lab2.configure(image=papier)
    else:
            lab2.configure(image=cisceaux)
    aug(mon,ton)
    score1.configure(text=str(t))
    score2.configure(text=str(m))
def jouer_pierre():
    jouer(1)
    lab1.configure(image=pierre)
def jouer_papier():
    jouer(2)
    lab1.configure(image=papier)
def jouer_cisceaux():
    jouer(3)
    lab1.configure(image=cisceaux)
t=0
m=0
#fenetre
fenetre=Tk()
fenetre.title("pierre papier cisceaux")

#image
pierre=PhotoImage(file="pierre.gif")
papier=PhotoImage(file="papier.gif")
cisceaux=PhotoImage(file="cisceaux.gif")
rien=PhotoImage(file="rien.gif")
#label
text1=Label(fenetre,text="Humain",font=('MS Serif',16))
text1.grid(row=0,column=0)
text2=Label(fenetre,text="Machine",font=('MS Serif',16))
text2.grid(row=0,column=2)
text3=Label(fenetre,text="Cliquez ici pour jouer")
text3.grid(row=3,columnspan=3,pady=5)
score1=Label(fenetre,text="0")
score1.grid(row=1,column=0)
score2=Label(fenetre,text="0")
score2.grid(row=1,column=2)
lab1=Label(fenetre,image=rien)
lab1.grid(row=2,column=0)
lab2=Label(fenetre,image=rien)
lab2.grid(row=2,column=2)
#boutons
bouton1=Button(fenetre,command=jouer_pierre)
bouton1.configure(image=pierre)
bouton1.grid(row=4,column=0,pady=5)
bouton2=Button(fenetre,command=jouer_papier)
bouton2.configure(image=papier)
bouton2.grid(row=4,column=1,pady=5)
bouton3=Button(fenetre,command=jouer_cisceaux)
bouton3.configure(image=cisceaux)
bouton3.grid(row=4,column=2,pady=5)
bouton4=Button(fenetre,text="quitter",command=fenetre.quit)
bouton4.grid(row=6,column=1)
fenetre.mainloop()
