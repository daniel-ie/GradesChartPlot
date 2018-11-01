import Tkinter
import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

def menu(root):
    page1btn = Tk.Button(root, text="Page 1", command=page1)
    page2btn = Tk.Button(root, text="Page 2", command=page2)
    page1btn.pack()
    page2btn.pack()


def page1():
    canvas2.get_tk_widget().pack_forget()
    canvas1.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def page2():
    canvas1.get_tk_widget().pack_forget()
    canvas2.get_tk_widget().pack()


root = Tk.Tk()

menu(root)



##################################################
f = Figure(figsize=(5,4), dpi=100)
ax = f.add_subplot(111)

data = (90, 85, 95)       #
ind = numpy.arange(len(data))  # the x locations for the groups
width = .5

ax.set_xlabel("estudiantes")
ax.set_ylabel("notas")
ax.set_xticks(ind+width/2)
ax.set_xticklabels(['a', 'b', 'c']) #

rects1 = ax.bar(ind, data, width)
canvas2 = FigureCanvasTkAgg(f, master=root)
canvas2.show()
##################################################

##################################################
g = Figure(figsize=(5,4), dpi=100)
ax1 = g.add_subplot(111)

data = (85, 95, 80)       #
ind = numpy.arange(len(data))  # the x locations for the groups
width = .5

ax1.set_xlabel("estudiantes")
ax1.set_ylabel("notas")
ax1.set_xticks(ind+width/2)
ax1.set_xticklabels(['a', 'b', 'c']) #

rects1 = ax1.bar(ind, data, width)
##################################################

canvas1 = FigureCanvasTkAgg(g, master=root)
canvas1.show()


Tk.mainloop()
