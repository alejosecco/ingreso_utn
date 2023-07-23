import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

A) Al presionar el botón ‘Agregar' se debera cargar el nombre* y el precio** en sus respectivas listas.

* SOLO LETRAS MAYUSCULAS (A-Z)
** Enteros positivos

Si existe error al validar indicarlo mediante un Alert, cambiar el fondo del campo de texto con error
Si se cargo  coctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI AMBOS SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los articulos, sus precios y su posicion en la lista (por terminal)

C) Informar 
    1- Articulo mas caro
    2- Articulo mas barato
    3- Precio promedio
    4- Articulos que son mas caros que el promedio
    5- Articulos que son mas baratos que el promedio




'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.txt_nombre_articulo = customtkinter.CTkEntry(
            master=self, placeholder_text="Nombre Articulo")
        self.txt_nombre_articulo.grid(row=0, padx=20, pady=20)

        self.txt_precio_articulo = customtkinter.CTkEntry(
            master=self, placeholder_text="Precio")
        self.txt_precio_articulo.grid(row=1, padx=20, pady=20)

        self.btn_agregar = customtkinter.CTkButton(
            master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.btn_informar = customtkinter.CTkButton(
            master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20,
                               columnspan=2, sticky="nsew")

        self.lista_nombre_articulo = ['TV', 'LICUADORA']
        self.lista_precio_articulo = [1000, 200]

    def btn_agregar_on_click(self):
        bandera_nombre = False
        bandera_precio = False
        nombre_ingresado = self.txt_nombre_articulo.get()
        precio_ingresado = self.txt_precio_articulo.get()
        for letra in nombre_ingresado:
            if letra < "A" or letra > "Z":
                    bandera_nombre = False
                    break
            else:
                bandera_nombre = True
        if bandera_nombre == True:
            alert("nombre valido", "el nombre ingresado es valido")
        else:
            alert("nombre invalido", "el nombre ingresado no cumple con lo solicitado")
        if precio_ingresado != None and str.isnumeric(precio_ingresado) == True:
            alert("precio valido", "el precio ingresado es valido")
            precio_ingresado = int(precio_ingresado)
            bandera_precio =True
        else:
            alert("precio invalido", "el precio ingresado no es valido")
        if bandera_nombre == True and bandera_precio == True:
            self.lista_nombre_articulo.append(nombre_ingresado)
            self.lista_precio_articulo.append(precio_ingresado)
            alert("validacion", "datos cargados correctamente")

    def btn_mostrar_on_click(self):
        for (nombre,precio,index) in zip(self.lista_nombre_articulo, self.lista_precio_articulo, range(len(self.lista_precio_articulo))):
            print(f"producto: {nombre} {precio}$, posicion: {index}")

    def btn_informar_on_click(self):
        producto_mas_caro_index = self.lista_precio_articulo.index(max(self.lista_precio_articulo))
        nombre_producto_mas_caro = self.lista_nombre_articulo[producto_mas_caro_index]
        precio_producto_mas_caro = self.lista_precio_articulo[producto_mas_caro_index]
        print(f"el producto mas caro es {nombre_producto_mas_caro} con un precio de {precio_producto_mas_caro}$")
        producto_mas_barato_index = self.lista_precio_articulo.index(min(self.lista_precio_articulo))
        nombre_producto_mas_barato = self.lista_nombre_articulo[producto_mas_barato_index]
        precio_producto_mas_barato = self.lista_precio_articulo[producto_mas_barato_index]
        print(f"el precuto mas barato es {nombre_producto_mas_barato} con un precio de {precio_producto_mas_barato}$")
        promedio_precios = sum(self.lista_precio_articulo) / len(self.lista_nombre_articulo)
        print(f"el precio promedio de los productos es de {promedio_precios}$")
        articulos_mas_caros = []
        articulos_mas_baratos = []
        for (nombre,precio) in zip(self.lista_nombre_articulo, self.lista_precio_articulo):
            if precio > promedio_precios:
                articulos_mas_caros.append(nombre)
            elif precio < promedio_precios:
                articulos_mas_baratos.append(nombre)
        print(f"los productos mas caros que el promedio son {articulos_mas_caros} y los mas baratos que el promedio son {articulos_mas_baratos}")
                


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
