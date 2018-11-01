import Tkinter
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
        canvas = FigureCanvasTkAgg(f, master=self.root)
        #canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        canvas.show()
        return canvas


class Pages():
    def __init__(self, canvasS, canvasE, canvasS_clase, canvasE_clase):#, canvasS, canvasE):
        self.canvasS = canvasS
        self.canvasE = canvasE
        self.canvasS_clase = canvasS_clase
        self.canvasE_clase = canvasE_clase
        self.page0btn = Tk.Button(root, text="Inicio", command=self.page0)
        self.page1btn = Tk.Button(root, text="Notas por estudiante", command=self.page1)
        self.page1btn_clase = Tk.Button(root, text="Notas por clase", command=self.page1_clase)

        self.page2btnE = Tk.Button(root, text="Español", command=self.pageE)
        self.page2btnS = Tk.Button(root, text="Sociales", command=self.pageS)

        self.page2btnE_clase = Tk.Button(root, text="Español", command=self.pageE_clase)
        self.page2btnS_clase = Tk.Button(root, text="Sociales", command=self.pageS_clase)

    def page0(self):           # inicio
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        self.page0btn.pack_forget()
        self.page2btnE.pack_forget()
        self.page2btnS.pack_forget()        

        self.page1btn.pack()
        self.page1btn_clase.pack()

    def page1(self):        
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        self.canvasS_clase.get_tk_widget().pack_forget()
        self.canvasE_clase.get_tk_widget().pack_forget()        
        #self.page0btn.pack_forget()
        self.page1btn_clase.pack_forget()

        self.page0btn.pack()   # hacia pagina de inicio
        self.page2btnE.pack()  # plot de notas de español 
        self.page2btnS.pack()  # plot de notas de sociales 

    def page1_clase(self):        
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        self.canvasS_clase.get_tk_widget().pack_forget()
        self.canvasE_clase.get_tk_widget().pack_forget()        
        #self.page0btn.pack_forget()
        self.page1btn.pack_forget()

        self.page0btn.pack()   # hacia pagina de inicio
        self.page2btnE_clase.pack()  # plot de notas de español 
        self.page2btnS_clase.pack()  # plot de notas de sociales 

        
    def pageE(self):        
        self.page1btn.pack_forget()
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasS_clase.get_tk_widget().pack_forget()
        self.canvasE_clase.get_tk_widget().pack_forget()        
        
        self.canvasE.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)       
        self.page0btn.pack()   # hacia pagina de inicio
    def pageS(self):        
        self.page1btn.pack_forget()
        self.canvasE.get_tk_widget().pack_forget()
        self.canvasS_clase.get_tk_widget().pack_forget()
        self.canvasE_clase.get_tk_widget().pack_forget()        
        
        self.canvasS.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)       
        self.page0btn.pack()   # hacia pagina de inicio

    def pageE_clase(self):
        self.page1btn.pack_forget()
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()        
        self.canvasS_clase.get_tk_widget().pack_forget()
        
        self.canvasE_clase.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)       
        self.page0btn.pack()   # hacia pagina de inicio
    def pageS_clase(self):        
        self.page1btn.pack_forget()
        self.canvasS.get_tk_widget().pack_forget()
        self.canvasE.get_tk_widget().pack_forget()        
        self.canvasE_clase.get_tk_widget().pack_forget()

        self.canvasS_clase.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)       
        self.page0btn.pack()   # hacia pagina de inicio


data = (90, 85, 95)       #
data2 = (100, 80, 90)       #
data3 = (95, 80, 90)       #
data4 = (90, 85, 100)       #

nombres = ['a', 'b', 'c']
ind = numpy.arange(len(data))  # the x locations for the groups
width = .5


root = Tk.Tk()
#Text(root,width=60,height=40)

canvasS = Canvas(root, data, nombres, ind, width)
canvasE = Canvas(root, data2, nombres, ind, width)

canvasS_clase = Canvas(root, data3, nombres, ind, width)
canvasE_clase = Canvas(root, data4, nombres, ind, width)

pages = Pages(canvasS.canvas, canvasE.canvas, canvasS_clase.canvas, canvasE_clase.canvas)

pages.page0()


#canvas1.menu()
#canvas2.menu()

Tk.mainloop()
