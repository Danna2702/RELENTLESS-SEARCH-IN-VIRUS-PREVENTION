from tkinter import *

root = Tk()
root.title("COVID_19")
root.iconbitmap("virus.ico")

u = IntVar()
d = IntVar()
t = IntVar()
c = IntVar()
si = IntVar()

Label(root,text="COVID_19").pack()

Label(root,text="¿Ha tenido fiebre en la última semana?").pack()
Checkbutton(root, text="si", variable=u, 
            onvalue=2, offvalue=0).pack()
Checkbutton(root, text="no",variable=u, 
            onvalue=1, offvalue=0).pack()

Label(root,text="¿Ha estado en lugares concurridos como centros comerciales o reuniones?").pack()
Checkbutton(root, text="si", variable=d, 
            onvalue=2, offvalue=0).pack()
Checkbutton(root, text="no",variable=d, 
            onvalue=1, offvalue=0).pack()

Label(root,text="¿Se ha sentido enfermo o mal de salud?").pack()
Checkbutton(root, text="si", variable=t, 
            onvalue=2, offvalue=0).pack()
Checkbutton(root, text="no",variable=t, 
            onvalue=1, offvalue=0).pack()

Label(root,text="¿Ha estado en contacto con personas con COVID?").pack()
Checkbutton(root, text="si", variable=c, 
            onvalue=2, offvalue=0).pack()
Checkbutton(root, text="no",variable=c, 
            onvalue=1, offvalue=0).pack()

Label(root,text="¿Ha salido positivo para COVID?").pack()
Checkbutton(root, text="si", variable=si, 
            onvalue=1, offvalue=0).pack()
Checkbutton(root, text="no",variable=si, 
            onvalue=2, offvalue=0).pack()

def calculate (): 
    factor=0
    for i in [u.get(),d.get(),t.get(),c.get(),si.get()]:
        factor+=i
    print(factor)
    if factor >7:
        Label(root,text="Evita salir comunicate con tu servicio de salud").pack()
    else:
        Label(root,text="No hay mucho peligro de tener el virus, ten cuidado con tu salud sigue al siguiente filtro").pack()
    
    def close_window ():
        root.destroy()
    frame = Frame(root)
    frame.pack()
    button = Button (frame, text = "Finalizado.", command = close_window)
    button.pack()
    root.mainloop()

frame = Frame(root)
frame.pack()
button = Button (frame, text = "calculate", command = calculate)
button.pack()

root.mainloop()