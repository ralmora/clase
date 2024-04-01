from tkinter import *

raiz = Tk()

miframe=Frame(raiz)
miframe.pack()

Operacion=""
resultado=0

def suma(num):
    global Operacion
    global resultado
    resultado+=int(num)
    Operacion="suma"
    numeroPantalla.set(resultado)

def resta(num):
    global Operacion
    global resultado
    if resultado == 0:
        resultado = int(num)
    else:
        resultado -= int(num)
    Operacion = "resta"
    numeroPantalla.set(resultado)

def mostrar_resultado():
    global Operacion
    global resultado

    if Operacion == "suma":
        resultado += int(numeroPantalla.get())
    elif Operacion == "resta":
        resultado -= int(numeroPantalla.get())
       
    numeroPantalla.set(resultado)
    Operacion = ""

numeroPantalla=StringVar()

pantalla=Entry(miframe, width=36, bg="#E7E3E3", textvariable=numeroPantalla)
pantalla.grid(row=1, column=0, padx=3, pady=3, columnspan=5)
pantalla.config(background="#2F2F2F", fg="#22BA3F", justify="right")

def numeroPulsaciones(num):
    global Operacion

    if Operacion!="":
        numeroPantalla.set(num)
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

def el_resultado():
    mostrar_resultado()

boton7=Button(miframe, text="7", width=4, command=lambda:numeroPulsaciones("7"))
boton7.grid(row=2, column=0, padx=3, pady=3)
boton8=Button(miframe, text="8", width=4, command=lambda:numeroPulsaciones("8"))
boton8.grid(row=2, column=1, padx=3, pady=3)
boton9=Button(miframe, text="9", width=4, command=lambda:numeroPulsaciones("9"))
boton9.grid(row=2, column=2, padx=3, pady=3)
botonDiv=Button(miframe, text="/", width=4, command=lambda:numeroPulsaciones("/"))
botonDiv.grid(row=2, column=3, padx=3, pady=3)
botonPorc=Button(miframe, text="%", width=4, command=lambda:numeroPulsaciones("%"))
botonPorc.grid(row=2, column=4, padx=3, pady=3)

boton4=Button(miframe, text="4", width=4, command=lambda:numeroPulsaciones("4"))
boton4.grid(row=3, column=0, padx=3, pady=3)
boton5=Button(miframe, text="5", width=4, command=lambda:numeroPulsaciones("5"))
boton5.grid(row=3, column=1, padx=3, pady=3)
boton6=Button(miframe, text="6", width=4, command=lambda:numeroPulsaciones("6"))
boton6.grid(row=3, column=2, padx=3, pady=3)
botonMult=Button(miframe, text="x", width=4, command=lambda:numeroPulsaciones("x"))
botonMult.grid(row=3, column=3, padx=3, pady=3)
botonRes=Button(miframe, text="-", width=4, command=lambda:resta(numeroPantalla.get()))
botonRes.grid(row=3, column=4, padx=3, pady=3)

boton1=Button(miframe, text="1", width=4, command=lambda:numeroPulsaciones("1"))
boton1.grid(row=4, column=0, padx=3, pady=3)
boton2=Button(miframe, text="2", width=4, command=lambda:numeroPulsaciones("2"))
boton2.grid(row=4, column=1, padx=3, pady=3)
boton3=Button(miframe, text="3", width=4, command=lambda:numeroPulsaciones("3"))
boton3.grid(row=4, column=2, padx=3, pady=3, )
botonMin=Button(miframe, text="-", width=4, command=lambda:numeroPulsaciones("-"))
botonMin.grid(row=4, column=3, padx=3, pady=3)
botonEqu=Button(miframe, text="=", width=4, height=3, command=el_resultado)
botonEqu.grid(row=4, column=4, padx=3, pady=3, rowspan=2)

boton0=Button(miframe, text="0", width=11, command=lambda:numeroPulsaciones("0"))
boton0.grid(row=5, column=0, padx=3, pady=3, columnspan=2)
botonComma=Button(miframe, text=",", width=4, command=lambda:numeroPulsaciones(","))
botonComma.grid(row=5, column=2, padx=3, pady=3)
botonSum=Button(miframe, text="+", width=4, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=3, padx=3, pady=3)

raiz.mainloop()

















