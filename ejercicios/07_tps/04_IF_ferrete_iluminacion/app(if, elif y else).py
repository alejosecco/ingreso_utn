import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        cantidad_lamparas = int(self.combobox_cantidad.get())
        marca_lamparas = self.combobox_marca.get()
        precio = int(self.combobox_cantidad.get()) * 800
        mensaje = "el precio por la compra de {0} lamparas de la marca {1} es ".format(cantidad_lamparas, marca_lamparas)
        
        if cantidad_lamparas >= 6:
            precio = precio * 0.5
        elif cantidad_lamparas == 5:
            if marca_lamparas == "ArgentinaLuz":
                    precio = precio *0.60
            else:
                    precio = precio *0.70
        elif cantidad_lamparas == 4:
            if marca_lamparas == "FelipeLamparas" or marca_lamparas == "ArgentinaLuz":
                    precio = precio * 0.75
            else:
                    precio = precio * 0.80
        elif cantidad_lamparas == 3:
            if marca_lamparas == "ArgentinaLuz":
                    precio = precio * 0.85
            elif marca_lamparas == "FelipeLamparas":
                    precio = precio * 0.90
            else:
                precio = precio * 0.95

        if precio > 4000:
                precio = precio * 0.95
        alert(title="precio final", message= mensaje + f"{precio}$")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()