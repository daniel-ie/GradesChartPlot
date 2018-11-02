import os
import tkinter
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


class Canvas():
    def __init__(self, root, data, nombres, ind, width):
        self.root = root
        self.data = data        
        self.nombres = nombres
        self.ind = ind
        self.width = width
        self.canvas()
        self.canvas = self.canvas()

    def canvas(self):
        f = Figure(figsize=(5,4), dpi=100)     
        ax = f.add_subplot(111)
        
        ax.set_xlabel("estudiantes")        
        ax.set_ylabel("notas")
        ax.set_xticks(self.ind+self.width/2)
        ax.set_xticklabels(self.nombres) #
        rects = ax.bar(self.ind, self.data, self.width)
        canvas = FigureCanvasTkAgg(f, master=root)#self.root)
        canvas.show()
        return canvas



class Pages():
    def __init__(self, canvas):
        self.canvasS = canvas[0]
        self.canvasE = canvas[1]
        self.canvas_clase = canvas[2]

        self.back = back
        self.page0btn = Tk.Button(master=self.back, text="Inicio", command=self.page0)
        self.page1btn = Tk.Button(master=self.back, text="Notas por estudiante", command=self.page1)
        self.page1btn_clase = Tk.Button(master=self.back, text="Notas por clase", command=self.page1_clase)

        self.page2btnE = Tk.Button(master=self.back, text="Español", command=self.pageE)
        self.page2btnS = Tk.Button(master=self.back, text="Sociales", command=self.pageS)
        self.page2btnM= Tk.Button(master=self.back, text="Matematicas", command=self.pageM)
        self.page2btnC = Tk.Button(master=self.back, text="Ciencias", command=self.pageC)

    def page0(self):           # inicio
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()

        self.page0btn.pack_forget()
        self.page2btnE.pack_forget()
        self.page2btnS.pack_forget()          
        self.page2btnM.pack_forget()
        self.page2btnC.pack_forget()
        
        self.back.pack()
        root.title("Graficar notas")
        self.page1btn.pack(fill=Tk.BOTH, expand=1)
        self.page1btn_clase.pack(fill=Tk.BOTH, expand=1)

    def page1(self):          ################### notas por estudiante 
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()

        self.page1btn.pack_forget()
        self.page1btn_clase.pack_forget()

        self.back.pack()
        root.title("Notas por estudiante")
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio
        self.page2btnE.pack(fill=Tk.BOTH, expand=1)  # plot boton de notas de español 
        self.page2btnS.pack(fill=Tk.BOTH, expand=1)  # plot boton de notas de sociales 
        self.page2btnM.pack(fill=Tk.BOTH, expand=1)  # plot boton de notas de matematicas
        self.page2btnC.pack(fill=Tk.BOTH, expand=1)  # plot boton de notas de ciencias
        
    def page1_clase(self):    ################### notas por clase        
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
     
        self.page1btn.pack_forget()
        self.page1btn_clase.pack_forget()

        self.back.pack()
        root.title("Notas por clase")
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio
        self.canvas_clase.get_tk_widget().pack(fill=Tk.BOTH, expand=1) 
        
    def pageE(self):        
        self.page1btn.pack_forget()
        self.canvasS.get_tk_widget().pack_forget()
        self.canvas_clase.get_tk_widget().pack_forget()

        self.back.pack()
        root.title("Notas de español promediadas por estudiante")
        self.canvasE.get_tk_widget().pack(fill=Tk.BOTH, expand=1)       
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio
    def pageS(self):        
        self.page1btn.pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        self.canvas_clase.get_tk_widget().pack_forget()

        self.back.pack()
        root.title("Notas de Sociales promediadas por estudiante")
        self.canvasS.get_tk_widget().pack(fill=Tk.BOTH, expand=1)       
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio

    def pageM(self):        
        self.page1btn.pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasC.get_tk_widget().pack_forget()
        self.canvas_clase.get_tk_widget().pack_forget()

        self.back.pack()
        root.title("Notas de matematicas promediadas por estudiante")
        self.canvasM.get_tk_widget().pack(fill=Tk.BOTH, expand=1)       
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio
        
    def pageC(self):        
        self.page1btn.pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasM.get_tk_widget().pack_forget()
        self.canvas_clase.get_tk_widget().pack_forget()

        self.back.pack()
        root.title("Notas de Ciencias promediadas por estudiante")
        self.canvasC.get_tk_widget().pack(fill=Tk.BOTH, expand=1)       
        self.page0btn.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)   # hacia pagina de inicio


# datos, inicializaciones
i = 0
a = []
data = []
nombres = []
notas_sociales = []
notas_espa_ol = []
notas_mate = []
notas_ciencias = []

clase= ['Sociales', 'Espa_ol', 'Matematicas', 'Ciencias']
prom_clase = []
prom_sociales = 0
prom_espa_ol = 0
prom_mate = 0
prom_ciencias = 0

# Abrir archivo 
f = open('data.txt', 'r')
for line in f.readlines():
    a = line.split()    
    nombres += [a[0]]
    data += [a[1:]]
    i += 1 

# Pasar datos al programa
for i in range(len(data)):
    notas_sociales += [data[i][0]] # notas de sociales 

for i in range(len(data)):
    notas_espa_ol += [data[i][1]]  # notas de español 
    
for i in range(len(data)):
    notas_mate += [data[i][2]]     # notas de matematicas 

for i in range(len(data)):
    notas_ciencias += [data[i][3]] # notas de ciencias 
    
for i in range(len(data)):
    prom_sociales += int(notas_sociales[i])
    prom_espa_ol += int(notas_espa_ol[i])
    prom_mate += int(notas_mate[i])
    prom_ciencias += int(notas_ciencias[i])
prom_clase = [prom_sociales/len(data), prom_espa_ol/len(data), prom_mate/len(data), prom_ciencias/len(data)] # promedios por materia


print(notas_sociales)
print(notas_espa_ol)
print(notas_mate)
print(notas_ciencias)  
print(prom_clase)

# Otros parametros
ind = numpy.arange(len(data))  # ubica la posicion donde se ubicaran los graficos de barras en x
width = .5


# ventana
root = Tk.Tk()
back = Tk.Frame(master=root, width=500, height=500, bg='black')


# graficos de barras
canvasS = Canvas(root, notas_sociales, nombres, ind, width).canvas
canvasE = Canvas(root, notas_espa_ol, nombres, ind, width).canvas
canvasM = Canvas(root, notas_mate, nombres, ind, width).canvas
canvasC = Canvas(root, notas_ciencias, nombres, ind, width).canvas

canvas_clase = Canvas(root, prom_clase, clase, ind, width).canvas
 

canvas = [canvasS, canvasE, canvasM, canvasC, canvas_clase] 
pages = Pages(canvas)

# abre la pagina de inicio en la ventana
pages.page0()


Tk.mainloop()
