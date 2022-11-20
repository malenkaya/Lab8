from tkinter import *
root = Tk()
 
c = Canvas(root, width=1000, height=1000, bg='black')
c.pack()
 
c.create_line(250, 50, 250, 210, width=2, fill='white')

c.create_oval(150, 110, 250, 210, width=2,  outline='white')

c.create_line(300, 110, 300, 210, width=2, fill='white')

c.create_line(300, 55, 300, 60, width=2, fill='white')

c.create_oval(350, 50, 350, 210, width=2,  outline='white')

c.create_line(400, 110, 440, 210, width=2, fill='white')

c.create_line(480, 110, 415, 280, width=2, fill='white')

c.create_oval(600, 110, 500, 210, width=2,  outline='white')

c.create_line(600, 110, 600, 210, width=2, fill='white')

# c.create_line(100, 180, 100, 60, fill='green',
#                 width=5, arrow=LAST, dash=(10,2),
#                 activefill='lightgreen',
#                 arrowshape="10 20 10")
 
root.mainloop()