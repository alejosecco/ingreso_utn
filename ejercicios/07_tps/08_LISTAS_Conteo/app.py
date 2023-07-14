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
        while (True):
            numero_ingresado =prompt(title="numeros", prompt="ingrese un numero")
            if numero_ingresado == None or numero_ingresado == 0:
                break
            else:
                    self.lista.append(int(numero_ingresado))
        numero_minimo = min(self.lista)
        numero_maximo = max(self.lista)
        negativos = []
        positivos = []
        ceros = []
        for numeros in self.lista:
            if numeros < 0:
                negativos.append(numeros)
            elif numeros > 0:
                positivos.append(numeros)
            else :
                ceros.append(numeros)
        self.maximo_positivos = max(positivos)
        self.minimo_negativos = min(negativos)
        self.suma_negativos = sum(negativos)
        self.suma_positivos = sum(positivos)
        self.cantidad_ceros = len(ceros)
        self.cantidad_positivos = len(positivos)
        self.cantidad_negativos = len(negativos)
        self.promedio_negativos = self.suma_negativos / self.cantidad_negativos
        
                
                
        

    def btn_mostrar_estadisticas_on_click(self):
        mensaje = "la suma de los numeros positivos es {0} con {1} positivos ingresados y el maximo numero positivo en la lista es {2}, la suma de los negativos es {3} con un promedio de {4} y {5} negativos ingresados y el numero mas chico de la lista es {6}. la cantidad de ceros es de {7}.".format(self.suma_positivos,self.cantidad_positivos ,self.maximo_positivos  ,self.suma_negativos,self.promedio_negativos,self.cantidad_negativos,self.minimo_negativos, self.cantidad_ceros)
        alert(title="estadisticas", message= mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
