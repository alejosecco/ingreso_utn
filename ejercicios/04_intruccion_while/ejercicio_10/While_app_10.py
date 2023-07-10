import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero_negativos = []
        numero_positivos = []
        ceros = []
        numero_ingresado = prompt(title="nose", prompt="ingrese un numero")
        while numero_ingresado != None:
            if numero_ingresado !=None:
                numero_ingresado = int(numero_ingresado)
                if numero_ingresado < 0:
                    numero_negativos.append(numero_ingresado)
                elif numero_ingresado > 0:
                    numero_positivos.append(numero_ingresado)
                elif numero_ingresado == 0:
                    ceros.append(numero_ingresado)
            numero_ingresado = prompt(title="nose", prompt="ingrese un numero")
                

        suma_negativos = sum(numero_negativos)
        suma_positivos = sum(numero_positivos)
        cantidad_de_numeros_positivos = len(numero_positivos)
        cantidad_de_numeros_negativos = len(numero_negativos)
        cantidad_0 = len(ceros)
        diferencia_numeros_positivos_negativos = cantidad_de_numeros_positivos - cantidad_de_numeros_negativos
        mensaje_suma = "la suma de los negativos es igual a {0}, la suma de los positivos es igual a {1}".format(suma_negativos, suma_positivos)
        mensaje_cantidad_numeros = "la cantidad de numeros ingresados es {0} numeros negativos, {1} numeros positivos y {2} ceros.".format(cantidad_de_numeros_negativos, cantidad_de_numeros_positivos,ceros)
        mensaje_diferencia_positivos_negativos = f"la diferencia entre los numeros positivos y los numeros negativos ingresados es de {diferencia_numeros_positivos_negativos}"
        alert(title="suma", message= mensaje_suma)
        alert(title="cantidad de nuemros", message= mensaje_cantidad_numeros)
        alert(title="diferencia", message=mensaje_diferencia_positivos_negativos)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
