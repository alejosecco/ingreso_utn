'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        nombre_mas_votos = None
        mas_votos = None
        nombre_menos_votos = None
        menos_votos = None  
        total_votos = 0
        contador_candidatos = 0
        total_edad = 0 
        bandera_primer_ingreso = True
        while True:
            nombre_ingresado = prompt(title="nombre", prompt="ingrese el nombre del postulante")
            while nombre_ingresado == None or str.isalpha(nombre_ingresado) == False:
                nombre_ingresado = prompt(title="nombre", prompt="ingrese un nombre valido")
            edad_ingresada = prompt(title="edad", prompt="ingrese la edad del postulante")
            while  edad_ingresada == None or str.isdigit(edad_ingresada) == False or int(edad_ingresada) < 25:
                edad_ingresada = prompt(title="edad", prompt="ingrese una edad valida del postulante")
            edad_ingresada = int(edad_ingresada)
            votos_ingresados = prompt(title="votos", prompt="ingrese los votos obtenidos por el postulante")
            while votos_ingresados == None or str.isdigit(votos_ingresados) == False or int(votos_ingresados) <= 0:
                votos_ingresados = prompt(title="votos", prompt="ingrese los votos obtenidos por el postulante")
            votos_ingresados = int(votos_ingresados)
            #punto a
            if bandera_primer_ingreso == True:
                mas_votos = votos_ingresados
                nombre_mas_votos = nombre_ingresado
                menos_votos = votos_ingresados
                nombre_menos_votos = nombre_ingresado
                bandera_primer_ingreso = False
            elif votos_ingresados > mas_votos:
                mas_votos = votos_ingresados
                nombre_mas_votos = nombre_ingresado
            #punto b
            elif votos_ingresados < menos_votos:
                menos_votos = votos_ingresados
                nombre_menos_votos = nombre_ingresado
            #punto c
            total_edad += edad_ingresada
            contador_candidatos += 1
            #punto d
            total_votos += votos_ingresados
            #===============
            continuar = question (title="continuar", message= "desea ingresar otro candidato?")
            if continuar == True:
                continue
            else:
                break
        #punto a 
        print(f"el candidato con mas votos fue {nombre_mas_votos} con un total de {mas_votos}")
        #punto b
        print(f"el candidato con menos votos fue {nombre_menos_votos} con un total de {menos_votos}")
        #punto c
        promedio_edad = total_edad / contador_candidatos
        print(f"el promedio de edades de los candidatos fue {promedio_edad}")
        #punto d
        print(f"el total de votos emitidos fue {total_votos}")
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
