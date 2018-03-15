
# coding: utf-8

# ### 首先先写一个Label的小demo

# In[ ]:


import tkinter as tk

window = tk.Tk()
window.title('testWindow')
window.geometry('400x200')

l = tk.Label(window,text='This is a text with tkinter.',bg='blue',font=('Arial',12),width=20,heigh=2)
l.pack()

window.mainloop()


# 接下来我们添加上Button操作|

# In[ ]:


import tkinter as tk

window = tk.Tk()
window.title('testWindow')
window.geometry('400x200')


var = tk.StringVar()
l = tk.Label(window,textvariable=var,bg='blue',font=('Arial',12),width=20,heigh=2)
l.pack()


on_click = False
def Click():
    global on_click
    if on_click == False:
        on_click = True
        var.set('This is a text with tkinter.') 
    else:
        on_click = False
        var.set('')


b = tk.Button(window,text='Click',width=15,heigh=2,command=Click)
b.pack()


window.mainloop()

