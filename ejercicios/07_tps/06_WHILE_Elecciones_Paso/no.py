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
        nombre_postulante = []
        edad_postulantes = []
        votos_postulados = []
        #if nombre_ingresado == "" or nombre_ingresado == None:
                #break
        while True:        
            nombre_ingresado = prompt(title="nombre", prompt="ingrese el nombre del postulante")
            while nombre_ingresado == None or str.isalpha(nombre_ingresado) == False:
                nombre_ingresado = prompt(title="nombre", prompt="ingrese un nombre valido")
            nombre_postulante.append(nombre_ingresado)
            edad_ingresada = prompt(title="edad", prompt="ingrese la edad del postulante")
            while  edad_ingresada == None or str.isdigit(edad_ingresada) == False or int(edad_ingresada) < 25:
                edad_ingresada = prompt(title="edad", prompt="ingrese una edad valida del postulante")
            edad_postulantes.append(int(edad_ingresada))
            votos_ingresados = prompt(title="votos", prompt="ingrese los votos obtenidos por el postulante")
            while votos_ingresados == None or str.isdigit(votos_ingresados) == False or int(votos_ingresados) <= 0:
                votos_ingresados = prompt(title="votos", prompt="ingrese los votos obtenidos por el postulante")
            votos_postulados.append(int(votos_ingresados))
            continuar = question (title="continuar", message= "desea ingresar otro candidato?")
            if continuar == True:
                continue
            else:
                break
        
        
        cantidad_postulados = len(nombre_postulante)
        promedio_edad = sum(edad_postulantes) / cantidad_postulados
        votos_emitidos = sum(votos_postulados)
        menos_votos = min(votos_postulados)
        mas_votos = max(votos_postulados)
        index_menos_votos = votos_postulados.index(menos_votos)
        index_mas_votos = votos_postulados.index(mas_votos)
        #a
        mensaje_mas_votos = f"{nombre_postulante[index_mas_votos]} fue el candidato con menos vatos"
        print(mensaje_mas_votos)
        #b
        mensaje_menos_votos = "{0} fue el candidato de menor edad con {1} años".format(nombre_postulante[index_menos_votos], edad_postulantes[index_menos_votos])
        print(mensaje_menos_votos)
        #c
        print(f"el promedio de las edades de los candidatos es {promedio_edad}")
        #d
        print(f"la cantidad de votos emitidos fueron {votos_emitidos}")
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
