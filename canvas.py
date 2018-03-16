import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

canvas = tk.Canvas(window, bg='blue', height=300, width=300)
image_file = tk.PhotoImage(file='pig.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
x0, y0, x1, y1= 20, 140, 100, 240
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0+40, y0+40, x1+40, y1+40, fill='red')
arc = canvas.create_arc(x0+80, y0+80, x1+80, y1+80, start=0, extent=180)
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)
canvas.pack()

def moveit():
    canvas.move(rect, 0, 2)

b = tk.Button(window, text='move', command=moveit).pack()


window.mainloop()