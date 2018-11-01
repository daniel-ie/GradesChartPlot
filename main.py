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
        canvas.show()
        return canvas

#class Pages():
#    def __init__(self, canvas):
#        self.canvas = canvas
        
#    def menu(self):
#        page1btn = Tk.Button(self.root, text="Page 1", command=self.page1)
#        page2btn = Tk.Button(self.root, text="Page 2", command=self.page2)
#        page1btn.pack()
#        page2btn.pack()

#    def page1(self):
        #canvas1, canvas2 = self.canvas()
#        self.canvas2.get_tk_widget().pack_forget()
#        self.canvas1.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#    def page2(self):
        #canvas1, canvas2 = self.canvas()
#        self.canvas1.get_tk_widget().pack_forget()
#        self.canvas2.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

class Pages():
    def __init__(self, canvas):
        self.canvas = canvas
        self.page0btn = Tk.Button(root, text="Page 0", command=self.page0)
        self.page1btn = Tk.Button(root, text="Page 1", command=self.page1)
        
    def page0(self):
        self.canvas.get_tk_widget().pack_forget()
        self.page0btn.pack_forget()

        self.page1btn.pack()

    def page1(self):        
        self.page1btn.pack_forget()
        
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.page0btn.pack()
        


data = (90, 85, 95)       #
nombres = ['a', 'b', 'c']
ind = numpy.arange(len(data))  # the x locations for the groups
width = .5


root = Tk.Tk()

canvas1 = Canvas(root, data, nombres, ind, width)
canvas2 = Canvas(root, data, nombres, ind, width)

pages = Pages(canvas1.canvas)

pages.page0()


#canvas1.menu()
#canvas2.menu()

Tk.mainloop()
