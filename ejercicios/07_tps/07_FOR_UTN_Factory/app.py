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
        nombre_ingresado = None
        edad_ingresada = None
        genero_ingresado = None
        tecnologia_ingresada = None
        puesto_ingresado = None
        contador_punto_a = 0
        punto_b_nombre = None
        punto_b_edad = 0
        contador_f = 0
        contador_m = 0
        contador_nb = 0
        edad_f_punto_c = 0
        edad_m_punto_c = 0
        edad_nb_punto_c = 0
        contador_py = 0
        contador_js = 0 
        contador_asp = 0


        for postulantes in range(10):
            nombre_ingresado = prompt(title="nombre", prompt="ingrese el nombre del postulante")
            while nombre_ingresado == None or str.isalpha(nombre_ingresado) ==False:
                nombre_ingresado = prompt(title="nombre", prompt="ingrese el nombre del postulante")
            edad_ingresada = prompt(title="edad", prompt="ingrese la edad del postulante")
            while edad_ingresada == None or str.isdigit(edad_ingresada) == False or int(edad_ingresada) < 18:
                edad_ingresada = prompt(title="edad", prompt="ingrese la edad del postulante")
            edad_ingresada = int(edad_ingresada)
            genero_ingresado = prompt(title="genero", prompt="ingrese el genero del postulante(F-M-NB)")
            while genero_ingresado != "F" and genero_ingresado != "M" and genero_ingresado != "NB":
                genero_ingresado = prompt(title="genero", prompt="ingrese un genero valido(F-M-NB)")
            tecnologia_ingresada = prompt(title="tecnologia", prompt="ingrese la tecnologia con la que trabaja(PYTHON - JS - ASP.NET)" )
            while tecnologia_ingresada != "PYTHON" and tecnologia_ingresada != "JS" and tecnologia_ingresada != "ASP.NET":
                tecnologia_ingresada = prompt(title="tecnologia", prompt="ingrese una tecnologia valida(PYTHON - JS - ASP.NET)" )
            puesto_ingresado = prompt(title="puesto", prompt="ingrese el puesto que ocuparia(JR - SSR - SR)")
            while puesto_ingresado != "JR" and puesto_ingresado != "SSR" and puesto_ingresado != "SR":
                puesto_ingresado = prompt(title="puesto", prompt="ingrese un puesto valido(JR - SSR - SR)")
            
            #punto a
            if genero_ingresado == "NB" and edad_ingresada >=25 and edad_ingresada <= 40 and tecnologia_ingresada == "ASP.NET" or tecnologia_ingresada =="JS" and puesto_ingresado == "SSR":
                contador_punto_a  +=1
            #punto b
            if edad_ingresada > punto_b_edad:
                punto_b_edad = edad_ingresada
                punto_b_nombre = nombre_ingresado
            #punto C y e
            match(genero_ingresado):
                case "F":
                    contador_f += 1
                    edad_f_punto_c += edad_ingresada
                case "M":
                    contador_m += 1
                    edad_m_punto_c += edad_ingresada
                case "NB":
                    contador_nb += 1
                    edad_nb_punto_c += edad_ingresada
            #punto d
            match(tecnologia_ingresada):
                case "PYTHON":
                    contador_py +=1
                case "JS":
                    contador_js += 1
                case "ASP.NET":
                    contador_asp +=1
            
        #punto a
        print(f"la cantidad de postulados con esas caracteristicas es igual a {contador_punto_a}")

        #punto b
        print(f"el postulante con menor edad es {punto_b_nombre} con {punto_b_edad} años")

        #punto c
        promedio_f = 0
        promedio_m = 0
        promedio_nb = 0
        if contador_f > 0:
            promedio_f = edad_f_punto_c / contador_f
        if contador_m > 0:
            promedio_m = edad_m_punto_c / contador_m
        if contador_nb >0:
            promedio_nb = edad_nb_punto_c / contador_nb
        print(f"el prpmedio de edades es de {promedio_f} para femeninos, {promedio_m} para masculinos y {promedio_nb} de no binarios")
        #punto d
        if contador_py < contador_js > contador_asp:
            tecnologia = "JS"
        elif contador_js < contador_py > contador_asp:
            tecnologia = "PYTHON"
        elif contador_js < contador_asp > contador_py:
            tecnologia = "ASP.NET"
        else:
            mensaje = "no hay tecnologia con mas numero de postulados"
        mensaje = f"el programa con mas postulados es {tecnologia} "
        print(mensaje)

        #punto e

        porcentaje_f = contador_f *10
        porcentaje_m = contador_m * 10
        porcentaje_nb = contador_nb *10
        print(f"los porcentajes por genero son {porcentaje_nb}% de no binarios, {porcentaje_m}% de masculinos y {porcentaje_f}% de femeninos")


                
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()