
# coding: utf-8

# In[ ]:


import tkinter as tk

window = tk.Tk()
window.title('testWindow')
window.geometry('400x150')


label = tk.Label(window,text='please select the button',bg='yellow',width=30)
label.pack()


def print_selection():
    if(var_1.get()==1)&(var_2.get()==0):
        label.config(text='I love only   Python!!!')
    elif(var_1.get()==0)&(var_2.get()==1):
        label.config(text='I love only   C++!!!')
    elif(var_1.get()==0)&(var_2.get()==0):
        label.config(text='I do not love either!!!')
    else:
        label.config(text='I love both!!!')


var_1 = tk.IntVar()
var_2 = tk.IntVar()
checkbutton_1 = tk.Checkbutton(window,text='Python',variable=var_1,onvalue = 1,offvalue = 0,command = print_selection)
#当我们选择这个button时，就会将onvalue=1传到variable，即这里的var_1，而var_1上面定义了为tk.IntVar
checkbutton_1.pack()
checkbutton_2 = tk.Checkbutton(window,text='C++',variable=var_2,onvalue = 1,offvalue = 0,command = print_selection)
checkbutton_2.pack()


window.mainloop()

