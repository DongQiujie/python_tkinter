
# coding: utf-8

# In[ ]:


import tkinter as tk

window = tk.Tk()
window.title('testWindow')
window.geometry('400x300')


e = tk.Entry(window,show=None)   #如果想显示为*的形式，则show="*
e.pack()


def insert_point():
    var = e.get()
    text.insert('insert',var)

    
def insert_end():
    var = e.get()
    text.insert('end',var)


def insert_specific():
    var = e.get()
    text.insert(1.3,var)        #将字符串插入到第一行，第三位，要注意它是从第零位开始的
    

#将字符串插入到鼠标点击的位置
button_1 = tk.Button(window,text='insert point',width=15,heigh=2,command=insert_point)
button_1.pack()


#将字符串插入到已有字符串最后
button_2 = tk.Button(window,text='insert end',width=15,heigh=2,command=insert_end)
button_2.pack()


#将字符串插入到特定的位置
button_3 = tk.Button(window,text='insert specific',width=15,heigh=2,command=insert_specific)
button_3.pack()


text = tk.Text(window,heigh=2)
text.pack()


window.mainloop()

