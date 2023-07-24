import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x400")
frame = ttk.LabelFrame(root,text="frame")
frame.grid(row=0,column=0,rowspan=2,columnspan=2,pady=20,padx=20)
button = tk.Button(frame, text=f"Botón")
button.pack(pady=20)
root.mainloop()

