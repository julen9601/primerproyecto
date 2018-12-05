from tkinter import *
from tkinter import ttk
import config
import prueba_browser as pb


raiz =Tk()
raiz.title("Prueba Browser Julen")
raiz.resizable(0,0)
raiz.iconbitmap("D:\pruebas_python\Graficos\marvin.ico")
#raiz.geometry("400x525")
raiz.config(bg="black")

miFrame=Frame()
miFrame.pack(side="right")
miFrame.config(bg="white", width="400",height="525")


#Textos
vu=Label(miFrame, text="Usuario:", fg="Black" )
vc=Label(miFrame, text="Contraseña", fg="Black")

vu.grid(row=0, column=0, sticky="e", pady="6")
vc.grid(row=1,column=0, sticky="e", pady="6")
#Entrys


user=Entry(miFrame)
contra=Entry(miFrame)

user.grid(row=0, column=1, sticky="e", pady="6")
contra.grid(row=1,column=1, sticky="e", pady="6")
contra.config(show="*")

#----------Función añadir texto a config -------------- 
def añadirUserypass():
    c=contra.get()
    u=user.get()

    print(f"hola {u}, tu contraseña es {c}")

    
    

   


#Botones

#Ejecuta la función del archivo prueba_browser
bok=ttk.Button(miFrame, text="execute", command=pb.openbrowser)
bok.grid(row=2, column=1)



#Guarda los datos introducidos como usuario y contraseña en config.
bol=Button(miFrame, text="Save", command=añadirUserypass)
bol.grid(row=2, column=0)

raiz.mainloop()