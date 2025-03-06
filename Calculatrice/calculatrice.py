
from tkinter import *

calc=Tk()

def operation(event):
    equation=var.get()
    operateurs=["+","-","×","÷"]
    nombres=[]
    resultat = 0
    j = 0
    if equation[-1]=="%" and "×"in equation:
        try:
            nombres=equation[:-1].split("×")
        except:
            return var.set("MA ERROR")
        else:
            resultat=1

            for i in nombres:
                    resultat*=float(i)
            resultat /= 100

        var.set(resultat)
    elif equation[-1]=="%" and"×" not in equation:
        return var.set(float(equation[:-1])/100)

    else:
        var.set(resultat)

    if "+" in equation and "-" in equation:
        for i in equation:
            if i == "+" or i == "-":
                j += 1
        temp1 = []
        if "+" in equation:
            nombre = equation.split("+")
        for i in nombre:
            if "-" in i:
                temp = i.split("-")
                temp1 += temp
            else:
                temp1.append(i)
        for e in operateurs:
            if e in equation[0]:
                temp1.remove("")
                temp1.insert(0, 0)
        for s in equation:
            if s == "+" or s == "-":
                break
        if s == "+":
            try:
                resultat = float(temp1[0]) + float(temp1[1])
            except:
                var.set("MA ERROR")
        if s == "-":
            try:
                resultat = float(temp1[0]) - float(temp1[1])
            except:
                var.set("MA ERROR")
        i = 2

        for x in range(equation.index(s) + 1, len(equation)):
            if equation[x] == "+" and i <= j:
                try:
                    resultat += float(temp1[i])
                except:
                    var.set("MA ERROR")
                i += 1
            if equation[x] == "-" and i <= j:
                try:
                    resultat -= float(temp1[i])
                except:
                    var.set("MA ERROR")
                i += 1
        var.set(resultat)

    else:
        for i in operateurs :
            if i in equation:
                nombres=equation.split(i)
                break
        for e in operateurs:
            if e in equation[0]:
                nombres.remove("")
                nombres.insert(0, 0)

        if i=="+":
            for j in nombres:
                try:
                    resultat+=float(j)
                except:
                    var.set("MA ERROR")
                else:
                   var.set(resultat)

        if i=="-":
            for j in nombres[1:]:
                resultat = float(nombres[0])
                try:
                    resultat -= float(j)
                except:
                    var.set("MA ERROR")
                else:
                    var.set(resultat)

        if i=="×" and "%" not in equation:
            resultat=1
            try:
                for j in nombres:
                    resultat*=float(j)
            except:
                var.set("MA ERROR")
            return var.set(resultat)

        if i=="÷" and len(nombres)>1:

            resultat = float(nombres[0])

            for j in nombres[1:]:
                try:
                    resultat /= float(j)
                except:
                    return var.set("MA ERROR")
            return var.set(resultat)


class touches():
    def __init__(self,nom,ligne,colone):
        self.nom=nom
        self.x=ligne
        self.y=colone
    def forme(self):
        boutton=Button(calc,width=7,height=2,text=self.nom,font=10)
        boutton.grid(row=self.x,column=self.y,pady=5,padx=6.45)
        def afficher(event):
            entry.insert(END,self.nom)
        boutton.bind("<Button-1>",afficher)

def effacer(event):
    var.set('')


def delete(event):
    donnees=var.get()
    var.set(donnees[:-1])








calc.title("Calculatrice")
#Dimentions
calc.geometry("300x500+450+100")
calc.minsize(width=400,height=480)
calc.maxsize(width=400,height=480)
var=StringVar()
entry=Entry(calc,textvariable=var,width=35,font=10)
entry.bind("<Return>",operation)
entry.grid(ipady=20,pady=20,padx=1.5,row=0,columnspan=4)
#ligne 1

btn_effacer=Button(calc,width=7,height=2,text="effacer",font=10)
btn_effacer.grid(row=1,column=0,pady=5,padx=5)
btn_effacer.bind("<Button-1>",effacer)
btnp=touches("+",1,1)
btnp.forme()
btnm=touches("-",1,2)
btnm.forme()
btn_del=Button(calc,width=7,height=2,text="del",font=10)
btn_del.grid(row=1,column=3,pady=5,padx=5)
btn_del.bind("<Button-1>",delete)


#btn7=touches("7",1,2)
#ligne 2
btn9=touches("9",2,0)
btn9.forme()
btn8=touches("8",2,1)
btn8.forme()
btn7=touches("7",2,2)
btn7.forme()
btnx=touches("×",2,3)
btnx.forme()
#ligne3
btn6=touches("6",3,0)
btn6.forme()
btn5=touches("5",3,1)
btn5.forme()
btn4=touches("4",3,2)
btn4.forme()
btnd=touches("÷",3,3)
btnd.forme()
#ligne 4
btn3=touches("3",4,0)
btn3.forme()
btn2=touches("2",4,1)
btn2.forme()
btn1=touches("1",4,2)
btn1.forme()

#ligne 5
btnv=touches(".",5,0)
btnv.forme()
btn0=touches("0",5,1)
btnpourcent=touches("%",5,2)
btnpourcent.forme()
btn0.forme()

btn=Button(calc,width=7,height=5,text="=",font=10)
btn.grid(row=4,column=3,pady=5,rowspan=2)
btn.bind("<Button-1>",operation)

calc.mainloop()



