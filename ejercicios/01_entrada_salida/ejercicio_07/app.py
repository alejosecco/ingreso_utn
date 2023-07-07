import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: alejo
apellido: secco
---
Ejercicio: entrada_salida_07
---
Enunciado:
Al presionar el botón  que corresponde a cada operación (suma, resta, multiplicación, y división), 
se deberán obtener los valores contenidos en las cajas de texto (txtOperadorA y txtOperadorB), 
transformarlos en números enteros, realizar dicha operación y luego mostrar el resultado 
de la misma utilizando el Dialog Alert. Ej: "El resultado de la …… es: 755"  
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_restar = customtkinter.CTkButton(master=self, text="Restar", command=self.btn_restar_on_click)
        self.btn_restar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.btn_multiplicar = customtkinter.CTkButton(master=self, text="Multiplicar", command=self.btn_multiplicar_on_click)
        self.btn_multiplicar.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_dividir = customtkinter.CTkButton(master=self, text="Dividir", command=self.btn_dividir_on_click)
        self.btn_dividir.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_sumar_on_click(self):
        operadorA = int(self.txt_operador_a.get())
        operadorB = int(self.txt_operador_a.get())
        resultadosuma = operadorA + operadorB
        mensaje = "el resultado es: {0}".format(resultadosuma)
        alert(title="nose", message= mensaje )  
             
    def btn_restar_on_click(self):
        operadorA = int(self.txt_operador_a.get())
        operadorB = int(self.txt_operador_a.get())
        resultadoresta = operadorA - operadorB
        mensaje2 = "el resultado es: {0}".format(resultadoresta)
        alert(title="nose", message= mensaje2 )

    def btn_multiplicar_on_click(self):
        operadorA = int(self.txt_operador_a.get())
        operadorB = int(self.txt_operador_a.get())
        resultadomulti = operadorA * operadorB
        mensaje3 = "el resultado es: {0}".format(resultadomulti)
        alert(title="nose", message= mensaje3 )

    def btn_dividir_on_click(self):
        operadorA = int(self.txt_operador_a.get())
        operadorB = int(self.txt_operador_b.get())
        resultadodivi = operadorA / operadorB
        mensaje4 = "el resultado es: {0}".format(resultadodivi)
        alert(title="nose", message= mensaje4 )
        
if __name__ == "__main__":
    app = App()
    app.mainloop()