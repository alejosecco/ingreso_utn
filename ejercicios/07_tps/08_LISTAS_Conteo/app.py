import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        
        while True:
            numero_ingresado = prompt(title="numeros", prompt="ingrese un numero")
            if numero_ingresado != "" and numero_ingresado != None:
                self.lista.append(float(numero_ingresado))
            #elif str.isdecimal(numero_ingresado) == True:
            else:
                break
        
        negativos = []
        positivos = []
        ceros = []
        for numero in self.lista:
            if numero < 0:
                negativos.append(numero)
            elif numero > 0:
                positivos.append(numero)
            else:
                ceros.append(numero)
        
        suma_negativos = sum(negativos)
        suma_positivos = sum(positivos)
        positivos_ingresados = len(positivos)
        negativos_ingresados = len(negativos)
        ceros_ingresados = len(ceros)
        minimos_negativo = min(negativos)
        max_positivo = max(positivos)
        promedio_negativos = suma_negativos / negativos_ingresados
        
        self.mensaje = f"La cantidad de positivos ingresados es {positivos_ingresados}, sumados da un total de {suma_positivos} con {max_positivo} siendo el numero mas grande. La cantidad de negativos ingresados es {negativos_ingresados}, con un total de {suma_negativos} y un promedio de {promedio_negativos}, siendo el {minimos_negativo} el menor numero ingresado. La cantidad de 0 ingresados es {ceros_ingresados}"
        
    def btn_mostrar_estadisticas_on_click(self):
        alert(title="informe general", message= self.mensaje)
    
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
