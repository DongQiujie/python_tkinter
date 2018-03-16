
# coding: utf-8

# ### 这是一个可以点选的按钮

# In[ ]:


import tkinter as tk

window = tk.Tk()
window.title('testWindow')
window.geometry('400x200')


var = tk.StringVar()
label = tk.Label(window,text='please select the button',bg='yellow',width=30)
label.pack()


def print_selection():
    label.config(text='you slect   '+var.get())
    
    
radiobutton_1 = tk.Radiobutton(window,text='Option A',variable=var,value='A',command=print_selection)
#当我们点击这个按钮时，就会将value的值传给variable，也就是将'A'传给var
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(window,text='Option B',variable=var,value='B',command=print_selection)
radiobutton_2.pack()
radiobutton_3 = tk.Radiobutton(window,text='Option C',variable=var,value='C',command=print_selection)
radiobutton_3.pack()


window.mainloop()

