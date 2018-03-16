
# coding: utf-8

# In[ ]:


import tkinter as tk

window = tk.Tk()
window.title('testWindow')
window.geometry('400x200')


label = tk.Label(window,text='please select the button',bg='yellow',width=30)
label.pack()


def print_selection(var):#这里直接使用var，因为scale会默认将拖动条值传进此函数
    label.config(text='you slect   '+var)


scale = tk.Scale(window,label='haul this scale',from_=5,to=11,orient=tk.HORIZONTAL,length=200,showvalue=1,tickinterval=2,resolution=0.01,command=print_selection)
#这里orient是定义方向是横向还是竖向的，length长度是像素不是字符长度，showcalue定义是否在拖动条上显示选择的值0-False，1-Ture，
#tickinterval是刻度间隔，resolution是选择的精度整数-1.一位小数-0.1，两位小数-0.01
scale.pack()


window.mainloop()

