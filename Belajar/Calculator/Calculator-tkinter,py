import tkinter
from tkinter.constants import END

screen = tkinter.Tk()
screen.title("Calculator")

#mendefinisikan input frame
s = tkinter.Entry(screen, width=35 , borderwidth=2)
s.grid(row=0 , column=0,columnspan=50, pady=5)

#click button
def click(num):
    current = s.get()
    s.delete(0, END)
    s.insert(0 , str(current) + str(num))
    
#penjumlahan
def plus():
    global num1
    global operation
    num1 = float(s.get())
    operation = "plus"
    s.delete(0, END)

#pengurangan
def minus():
    global num1
    global operation
    num1 = float(s.get())
    operation = "minus"
    s.delete(0, END)

#perkalian
def multiply():
    global num1
    global operation  
    num1 = float(s.get())
    operation = "multiply"
    s.delete(0, END)

#pembagian
def division():
    global num1
    global operation
    num1 = float(s.get())
    operation = "division"
    s.delete(0, END)

#hasil operasi
def equals():
    num2 = float(s.get())
    s.delete(0, END)
    s.focus_displayof
    #operasi yang dilakukan
    if operation == "plus":
        s.insert(0, num1 + num2)
    if operation == "minus":
        s.insert(0, num1 - num2)
    if operation == "multiply":
        s.insert(0, num1 * num2)
    if operation == "division":
        s.insert(0, num1 / num2)

#hapus semua
def delete():
    s.delete(0, END)

#mendefinisikan tombol dan nomor
button1 = tkinter.Button(screen, text ="1",padx=20, pady=10, command=lambda : click(1))
button2 = tkinter.Button(screen, text ="2",padx=20, pady=10, command=lambda : click(2))
button3 = tkinter.Button(screen, text ="3",padx=20, pady=10, command=lambda : click(3))
button4 = tkinter.Button(screen, text ="4",padx=20, pady=10, command=lambda : click(4))
button5 = tkinter.Button(screen, text ="5",padx=20, pady=10, command=lambda : click(5))
button6 = tkinter.Button(screen, text ="6",padx=20, pady=10, command=lambda : click(6))
button7 = tkinter.Button(screen, text ="7",padx=20, pady=10, command=lambda : click(7))
button8 = tkinter.Button(screen, text ="8",padx=20, pady=10, command=lambda : click(8))
button9 = tkinter.Button(screen, text ="9",padx=20, pady=10, command=lambda : click(9))
button0 = tkinter.Button(screen, text ="0",padx=20, pady=10, command=lambda : click(0))

#mendefinisikan tombol operasi 
buttonPlus = tkinter.Button(screen, text ="+",padx=18.5, pady=10, command=lambda : plus())
buttonMinus = tkinter.Button(screen, text ="-",padx=20, pady=10, command=lambda : minus())
buttonMultiply = tkinter.Button(screen, text ="X",padx=19, pady=10, command=lambda : multiply())
buttonDivision = tkinter.Button(screen, text =":",padx=20.5, pady=10, command=lambda : division())
buttonEquals = tkinter.Button(screen, text ="=",padx=19, pady=10, command=lambda : equals())
buttonDel = tkinter.Button(screen, text ="C",padx=19, pady=10, command=lambda : delete())

#menampilkan tombol pada baris 1
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
buttonDivision.grid(row=1, column=3)

#menampilkan tombol pada baris 2
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
buttonMultiply.grid(row=2, column=3)

#menampilkan tombol pada baris 3
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
buttonMinus.grid(row=3, column=3)

#menampilkan tombol pada baris 4
buttonDel.grid(row=4, column=0)
button0.grid(row=4, column=1)
buttonEquals.grid(row=4, column=2)
buttonPlus.grid(row=4, column=3)

#menjalabkan program
screen.mainloop()
