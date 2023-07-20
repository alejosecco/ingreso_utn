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
            tecnologia_postulantes.append(tecnologia_ingresada)
            puesto_ingresado = prompt(title="puesto", prompt="ingrese el puesto que ocuparia(JR - SSR - SR)")
            while puesto_ingresado != "JR" and puesto_ingresado != "SSR" and puesto_ingresado != "SR":
                puesto_ingresado = prompt(title="puesto", prompt="ingrese un puesto valido(JR - SSR - SR)")
            puesto_postulantes.append(puesto_ingresado)
        
        #a
        contador_punto_a = 0
        for (genero, edad, lenguaje,puesto) in zip(genero_postulantes, edades_postulantes, tecnologia_postulantes, puesto_postulantes):
            if genero == "NB" and edad >=25 and edad <= 40 and lenguaje == ("ASP.NET" or "JS") and puesto == "Ssr":
                contador_punto_a  +=1
        print(f"la cantidad de postulados con esas caracteristicas es igual a {contador_punto_a}")
                
        #b
        menor_edad = edades_postulantes.index(min(edades_postulantes))
        print(f"el postulante con menor edad es {nombres_postulantes[menor_edad]}")
        #c
        contador_no_binario = []
        contador_masculino = []
        contador_femenino = []
        for (genero,edad) in zip(genero_postulantes, edades_postulantes):
            match (genero):
                case "NB":
                        contador_no_binario.append(edad)
                case "M":
                        contador_masculino.append(edad)
                case "F":
                        contador_femenino.append(edad)
        promedio_no_binario = None
        promedio_masculino = None
        promedio_femenino = None
        try:
            promedio_no_binario = sum(contador_no_binario) / len(contador_no_binario)
        except ZeroDivisionError:
            promedio_no_binario = 0
        try:
            promedio_masculino = sum(contador_masculino) / len(contador_masculino)
        except ZeroDivisionError:
            promedio_masculino = 0
        try:
            promedio_femenino = sum(contador_femenino) / len(contador_femenino)
        except ZeroDivisionError:
            promedio_femenino = 0
        mensaje = "el promedio de edad en los postulantes no binarios es {0}, en masculinos {1} y en femeninos {2}".format(promedio_no_binario, promedio_masculino, promedio_femenino)
        print(mensaje)
        #d
        contador_js = tecnologia_postulantes.count("JS")
        contador_python = tecnologia_postulantes.count("PYTHON")
        contador_asp_net = tecnologia_postulantes.count("ASP.NET")
        tecnologia = None
        if contador_python < contador_js > contador_asp_net:
            tecnologia = "JS"
        elif contador_js < contador_python > contador_asp_net:
            tecnologia = "PYTHON"
        elif contador_js < contador_asp_net > contador_python:
            tecnologia = "ASP.NET"
        else:
            mensaje = "no hay tecnologia con mas numero de postulados"
        mensaje = f"el programa con mas postulados es {tecnologia} "
        print(mensaje)
        #e
        porcentaje_no_binario = len(contador_no_binario) *10
        porcentaje_masculino = len(contador_masculino) * 10
        porcentaje_femenino = len(contador_femenino ) *10
        mensaje = f"los porcentajes por genero son {porcentaje_no_binario}% de no binarios, {porcentaje_masculino}% de masculinos y {porcentaje_femenino}% de femeninos"
        print(mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()