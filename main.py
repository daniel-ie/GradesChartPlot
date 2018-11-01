import Tkinter
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

class Plot():
    def __init__(self, root, data1, data2, nombres, ind, width):
        self.root = root
        self.data1 = data1
        self.data2 = data2
        self.nombres = nombres
        self.ind = ind
        self.width = width
        self.canvas1, self.canvas2 = self.canvas()

    def menu(self):
        page1btn = Tk.Button(self.root, text="Page 1", command=self.page1)
        page2btn = Tk.Button(self.root, text="Page 2", command=self.page2)
        page1btn.pack()
        page2btn.pack()
        
    def page1(self):
        #canvas1, canvas2 = self.canvas()
        self.canvas2.get_tk_widget().pack_forget()
        self.canvas1.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    def page2(self):
        #canvas1, canvas2 = self.canvas()
        self.canvas1.get_tk_widget().pack_forget()
        self.canvas2.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    def canvas(self):
        ##################################################
        f1 = Figure(figsize=(5,4), dpi=100)
        f2 = Figure(figsize=(5,4), dpi=100)
        ax1 = f1.add_subplot(111)
        ax2 = f2.add_subplot(111)

        ax1.set_xlabel("estudiantes")
        ax2.set_xlabel("estudiantes")
        ax1.set_ylabel("notas")
        ax2.set_ylabel("notas")
        ax1.set_xticks(self.ind+self.width/2)
        ax2.set_xticks(self.ind+self.width/2)
        ax1.set_xticklabels(self.nombres) #
        ax2.set_xticklabels(self.nombres) #

        rects1 = ax1.bar(self.ind, self.data1, self.width)
        rects2 = ax2.bar(self.ind, self.data2, self.width)
        canvas1 = FigureCanvasTkAgg(f1, master=root)
        canvas1.show()
        canvas2 = FigureCanvasTkAgg(f2, master=root)
        canvas2.show()
        ##################################################
        return canvas1, canvas2

data1 = (90, 85, 95)       #
data2 = (85, 95, 100)       #
nombres = ['a', 'b', 'c']
ind = numpy.arange(len(data1))  # the x locations for the groups
width = .5
#canvas1, canvas2 = canvas(data1, data2, nombres, ind, width)


root = Tk.Tk()

plot = Plot(root, data1, data2, nombres, ind, width)

plot.menu()

Tk.mainloop()
