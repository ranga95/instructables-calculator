try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox
def proces():
    try:
        number1=Entry.get(E1)
        number2=Entry.get(E2)
        operator=Entry.get(E3)
        number1=int(number1)
        number2=int(number2)
        if operator =="+":
            answer=number1+number2
        if operator =="-":
            answer=number1-number2
        if operator=="*":
            answer=number1*number2
        if operator=="/":
            answer=number1/number2
        Entry.insert(E4,0,answer)
        print(answer)
    except ValueError:
        messagebox.showinfo("Atenció!","Introdueix valors vàlids")
mywindow = Tk()
mywindow.title("CALCULATOR")

mywindow.geometry("270x180")
mywindow.resizable(False,False)

L1 = Label(mywindow, text="És l'hora de calcular!",).grid(row=0,column=1)
L2 = Label(mywindow, text="Número 1",).grid(row=1,column=0)
L3 = Label(mywindow, text="Número 2",).grid(row=2,column=0)
L4 = Label(mywindow, text="Operació",).grid(row=3,column=0)
L4 = Label(mywindow, text="Resultat",).grid(row=4,column=0,pady=2)
E1 = Entry(mywindow, bd =5)
E1.grid(row=1,column=1)
E2 = Entry(mywindow, bd =5)
E2.grid(row=2,column=1)
E3 = Entry(mywindow, bd =5)
E3.grid(row=3,column=1)
E4 = Entry(mywindow, bd =5)
E4.grid(row=4,column=1)
B=Button(mywindow, text ="Solucionar",command = proces).grid(row=5,column=1,pady=5)
mywindow.mainloop()