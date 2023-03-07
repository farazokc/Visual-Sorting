import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

import tkinter as tk


x = np.arange(0, 10, 1)
y = np.arange(0, 10, 1)

root = tk.Tk()
fig1, ax = plt.subplots()

canvas1 = FigureCanvasTkAgg(fig1, master=root)
# canvas1.show()
canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1.0)

# ax = fig1.add_subplot(111)
ax.plot(x, y)
canvas1.draw()

root.mainloop()

root2 = tk.Toplevel()
fig2, ax2 = plt.subplots()

canvas2 = FigureCanvasTkAgg(fig2, master=root2)
# canvas2.show() # TODO: show has been depreciated
canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1.0)

# ax = fig2.add_subplot(111)
ax2.plot(x, 2 * y)
canvas2.draw()

# root.mainloop()
root2.mainloop()
