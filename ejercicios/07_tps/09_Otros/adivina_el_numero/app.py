import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random
import time

'''
Adivina el número (v 1.0):
Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón “Verificar”, si el número ingresado es el mismo que el número secreto se dará por terminado
 el juego con un mensaje similar a este: 

“Ganaste en X intentos”.
de no ser igual se debe informar si 
“falta…”  para llegar al número secreto  o si 
“se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.btn_reset = customtkinter.CTkButton(master=self, text="Reiniciar", command=self.btn_reset_on_click)
        self.btn_reset.grid(row=3, pady=20, columnspan=2, sticky="nsew")
        
        self.inicio_juego()
        
    def btn_reset_on_click(self):
        self.inicio_juego()
        

    def btn_mostrar_on_click(self):
        if self.prendido_apagado == True:
            numero_ingresado = int(self.txt_numero.get())
            self.numero_intento += 1
            if numero_ingresado < self.numero_secreto:
                alert(title="numero incorrecto", message="falta…")
            elif numero_ingresado > self.numero_secreto:
                alert(title="numero incorrecto", message="se pasó…")
            else:
                fin_juego = time.time()
                timepo_juego = fin_juego - self.inicio_timepo_juego
                alert(title="numero correcto", message=f"Ganaste en {self.numero_intento} intentos, en {int(timepo_juego)} segundos")
                self.prendido_apagado = False
            
    def inicio_juego(self):
        self.txt_numero.delete(0,100)
        self.numero_secreto = random.randrange(1, 100)
        self.numero_intento = 0
        print(self.numero_secreto)
        self.prendido_apagado = True
        self.inicio_timepo_juego = time.time()


if __name__ == "__main__":
    app = App() 
    app.geometry("300x300")
    app.mainloop()