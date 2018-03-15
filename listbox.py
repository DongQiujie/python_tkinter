
# coding: utf-8

# In[ ]:


import tkinter as tk

window = tk.Tk()
window.title('testWindow')
window.geometry('400x300')


var_1 = tk.StringVar()
label = tk.Label(window,textvariable=var_1,bg='yellow',width=10)
label.pack()


def print_selection():
    value = listbox.get(listbox.curselection())  #取出我们光标在listbox里选择的值
    var_1.set(value)

button_1 = tk.Button(window,text='print selection',width=15,heigh=2,command=print_selection)
button_1.pack()


var_2 = tk.StringVar()
var_2.set((1991,1992,1993,1994,1995,1996))  
listbox = tk.Listbox(window,listvar=var_2)
list_items = [2000,2001,2002]
for item in list_items:
    listbox.insert('end',item)
#或者使用索引位置插入
listbox.insert(1,'first')
listbox.insert(2,'second')
#当我们需要删除某项时
listbox.delete(2)
listbox.pack()


window.mainloop()

