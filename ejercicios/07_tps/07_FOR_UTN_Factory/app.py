'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        nombres_postulantes = []
        edades_postulantes = []
        genero_postulantes = []
        tecnologia_postulantes = []
        puesto_postulantes = []
        for postulantes in range(10):
            nombre_ingresado = prompt(title="nombre", prompt="ingrese el nombre del postulante")
            nombres_postulantes.append(nombre_ingresado)
            edad_ingresada = prompt(title="edad", prompt="ingrese la edad del postulante")
            while str.isdigit(edad_ingresada) == False or int(edad_ingresada) < 18:
                edad_ingresada = prompt(title="edad", prompt="ingrese la edad del postulante")
            edades_postulantes.append(int(edad_ingresada))
            genero_ingresado = prompt(title="genero", prompt="ingrese el genero del postulante(F-M-NB)")
            while genero_ingresado != "F" and genero_ingresado != "M" and genero_ingresado != "NB":
                genero_ingresado = prompt(title="genero", prompt="ingrese un genero valido(F-M-NB)")
            genero_postulantes.append(genero_ingresado)
            tecnologia_ingresada = prompt(title="tecnologia", prompt="ingrese la tecnologia con la que trabaja(PYTHON - JS - ASP.NET)" )
            while tecnologia_ingresada != "PYTHON" and tecnologia_ingresada != "JS" and tecnologia_ingresada != "ASP.NET":
                tecnologia_ingresada = prompt(title="tecnologia", prompt="ingrese una tecnologia valida(PYTHON - JS - ASP.NET)" )
            puesto_ingresado = prompt(title="puesto", prompt="ingrese el puesto que ocuparia(Jr - Ssr - Sr)")
            while puesto_ingresado != "Jr" and puesto_ingresado != "Ssr" and puesto_ingresado != "Sr":
                puesto_ingresado = prompt(title="puesto", prompt="ingrese un puesto valido(Jr - Ssr - Sr)")
            puesto_postulantes.append(puesto_ingresado)
        
        #a
        no_binario_index = []
        for gen in range(genero_postulantes):
            if gen == "NB":
                no_binario_index.append(gen)
                
        #b
        menor_edad = edades_postulantes.index(min(edades_postulantes))
        print(f"el postulante con menor edad es {nombres_postulantes[menor_edad]}")
        #c
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
