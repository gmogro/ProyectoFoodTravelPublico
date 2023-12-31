import tkinter as tk
from tkinter import ttk
import customtkinter
import os
from PIL import Image
from Servicios.servicio_destino_culinario import ServicioDestinoCulinario

class DestinosFrame(customtkinter.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.grid_columnconfigure(0, weight=1)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.destino_large_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "destinosCulinarios.png")), size=(500, 150)) #imagen en el medio de la app
        self.destino_frame_large_image_label = customtkinter.CTkLabel(self, text="", image=self.destino_large_image)
        self.destino_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.frame_table = customtkinter.CTkFrame(self,corner_radius=0)
        self.frame_table.grid(row=1, column=0, sticky="nsew")
        self.frame_table.grid_columnconfigure(0, weight=1)

        self.frame_filter = customtkinter.CTkFrame(self.frame_table,corner_radius=0)
        self.frame_filter.grid(row=0, column=0, sticky="nsew")
        self.filter_input = customtkinter.CTkEntry(self.frame_filter,width=300,placeholder_text="Buscar")
        self.filter_input.grid(row=0,column=0,padx=10,pady=10)
        self.filter_boton = customtkinter.CTkButton(self.frame_filter,text="BUSCAR")
        self.filter_boton.grid(row=0,column=1,padx=10,pady=10)

        self.boton_editar = customtkinter.CTkButton(self.frame_filter,text="EDITAR",fg_color="#02b0db",hover_color="#60d3f0")
        self.boton_eliminar = customtkinter.CTkButton(self.frame_filter,text="ELIMINAR",fg_color="red",hover_color="#e84351")
        self.boton_ver = customtkinter.CTkButton(self.frame_filter,text="VER",fg_color="green",hover_color="#3bed44")
        self.boton_editar.grid(row=0,column=2,padx=10,pady=10)
        self.boton_eliminar.grid(row=0,column=3,padx=10,pady=10)
        self.boton_ver.grid(row=0,column=4,padx=10,pady=10)

        self.create_table()
        self.table.bind("<Double-Button-1>", self.abrir_ventana)

    def create_table(self):
        self.table = ttk.Treeview(self.frame_table, column=("c1", "c2", "c3",
                                "c4", "c5", "c6","c7", "c8", "c9",), show='headings')
        self.table.column("#1", anchor=tk.CENTER)
        self.table.heading("#1", text="Nombre")
        self.table.column("#2", anchor=tk.CENTER)
        self.table.heading("#2", text="Tipo Cocina")
        self.table.column("#3", anchor=tk.CENTER)
        self.table.heading("#3", text="Precio Minimo")
        self.table.column("#4", anchor=tk.CENTER)
        self.table.heading("#4", text="Precio Maximo")
        self.table.column("#5", anchor=tk.CENTER)
        self.table.heading("#5", text="Popularidad")
        self.table.column("#6", anchor=tk.CENTER)
        self.table.heading("#6", text="Disponibilidad")
        self.table.column("#7", anchor=tk.CENTER)
        self.table.heading("#7", text="id_ubicacion")
        self.table.column("#8", anchor=tk.CENTER)
        self.table.heading("#8", text="Tipo Cocina")
        self.table.column("#9", anchor=tk.CENTER)
        self.table.heading("#9", text="Ingredientes")
        self.table.grid(row=1, column=0,padx=20, pady=20,sticky="nsew")

        self.scrollable_frame_horizontal = customtkinter.CTkScrollbar(self.frame_table,width=100,command=self.table.xview,orientation="horizontal")
        self.scrollable_frame_horizontal.grid(row=2, column=0,sticky="ew")
        self.table.configure(xscrollcommand=self.scrollable_frame_horizontal.set)

        self.scrollable_frame_vertical = customtkinter.CTkScrollbar(self.frame_table,command=self.table.yview,orientation="vertical")
        self.scrollable_frame_vertical.grid(row=1, column=1,sticky="ns")
        self.table.configure(xscrollcommand=self.scrollable_frame_vertical.set)
        
        self.insert_table()
    

    def insert_table(self):
        servicio_destinos = ServicioDestinoCulinario()
        destinos = servicio_destinos.get_values()
        
        for destino in destinos:
            print(destino)
            self.table.insert("", tk.END, values=destino)
    
    def abrir_ventana(self,event):
        ventana = customtkinter.CTkToplevel(self)
        ventana.mainloop()
