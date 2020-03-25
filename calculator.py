from tkinter import *

inputs=[]
sublist=[]

def button_click(input):
    e1.insert(END,input)
def on_enter0(e):
    b0['background']='khaki'
def on_leave0(e):
    b0['background'] = 'SystemButtonFace'
def on_enter1(e):
    b1.config(bg='khaki')
def on_leave1(e):
    b1['background'] = 'SystemButtonFace'
def on_enter2(self):
    b2['background']='khaki'
def on_leave2(e):
    b2['background'] = 'SystemButtonFace'
def on_enter3(self):
    b3['background']='khaki'
def on_leave3(e):
    b3['background'] = 'SystemButtonFace'
def on_enter4(self):
    b4.config(bg='khaki')
def on_leave4(e):
    b4['background'] = 'SystemButtonFace'
def on_enter5(self):
    b5.config(bg='khaki')
def on_leave5(e):
    b5['background'] = 'SystemButtonFace'
def on_enter6(self):
    b6.config(bg='khaki')
def on_leave6(e):
    b6['background'] = 'SystemButtonFace'
def on_enter7(self):
    b7.config(bg='khaki')
def on_leave7(e):
    b7['background'] = 'SystemButtonFace'
def on_enter8(self):
    b8.config(bg='khaki')
def on_leave8(e):
    b8['background'] = 'SystemButtonFace'
def on_enter9(self):
    b9.config(bg='khaki')
def on_leave9(e):
    b9['background'] = 'SystemButtonFace'
def on_enter_dot(self):
    b_dot.config(bg='khaki')
def on_leave_dot(e):
    b_dot['background'] = 'SystemButtonFace'
def on_enter_plus(self):
    b_plus.config(bg='khaki')
def on_leave_plus(e):
    b_plus['background'] = 'SystemButtonFace'
def on_enter_minus(self):
    b_minus.config(bg='khaki')
def on_leave_minus(e):
    b_minus['background'] = 'SystemButtonFace'
def on_enter_mul(self):
    b_mul.config(bg='khaki')
def on_leave_mul(e):
    b_mul['background'] = 'SystemButtonFace'
def on_enter_div(self):
    b_div.config(bg='khaki')
def on_leave_div(e):
    b_div['background'] = 'SystemButtonFace'
def on_enter_reset(self):
    b_reset.config(bg='khaki')
def on_leave_reset(e):
    b_reset['background'] = 'SystemButtonFace'
def on_enter_clear(self):
    b_clear.config(bg='khaki')
def on_leave_clear(e):
    b_clear['background'] = 'SystemButtonFace'
def on_enter_equal(self):
    b_equal.config(bg='khaki')
def on_leave_equal(e):
    b_equal['background'] = 'SystemButtonFace'

def action(act):
    no=e1.get()
    e1.delete(0, END)
    e2.config(state=NORMAL)
    e2.insert(END,no)
    e2.insert(END,act)
    e2.config(state=DISABLED)
    if no!='':
        inputs.append(no)
    inputs.append(act)

def clear():
    e1.delete(0,END)
def reset():
    e1.delete(0,END)
    e1.insert(0, "0")
    inputs.clear()
    sublist.clear()
    e2.config(state=NORMAL)
    e2.delete(0,END)
    e2.config(state=DISABLED)
def add(no1,no2):
    return float(no1)+float(no2)
def sub(no1,no2):
    return float(no1) - float(no2)
def mul(no1,no2):
    return float(no1)*float(no2)
def div(no1,no2):
    return float(no1)/float(no2)
def equal():
    action('=')
    inputs.pop(-1)
    while len(inputs)>1:
        sublist.clear()
        for e in range(3):
            x=inputs.pop(0)
            sublist.append(x)
        for key in calculations:
            if key==sublist[1]:
                ans=calculations[key](sublist[0],sublist[2])
                inputs.insert(0,str(ans))

    e1.insert(0,ans)
    inputs.clear()

if __name__=='__main__':
    root=Tk()
    root.title("Calculator")
    root.geometry('300x400')
    root.wm_maxsize(width=300,height=400)
    root.wm_minsize(width=300, height=400)
    e1=Entry(root,font=('calibri',15))
    e1.pack(fill=X,padx=10,pady=10)
    e1.insert(0,"0")

    e2 = Entry(root, font=('calibri', 15))
    e2.pack(fill=X, padx=10, pady=10)
    e2.config(state=DISABLED)
    row1 = Frame(root)
    b7 = Button(row1, text="7", padx=5, pady=5,width=5,relief='solid',borderwidth=1,font=(20),command=(lambda:button_click(7)))
    b8 = Button(row1, text="8", padx=5, pady=5,width=5,relief='solid',borderwidth=1,font=(20),command=(lambda:button_click(8)))
    b9 = Button(row1, text="9", padx=5, pady=5,width=5,relief='solid',borderwidth=1,font=(20),command=(lambda:button_click(9)))
    b_plus = Button(row1, text="+", padx=5, pady=5,width=5,relief='solid',borderwidth=1,font=(20),command=(lambda:action("+")))
    row1.pack(side=TOP, padx=5, pady=5)

    b7.pack(side=LEFT)
    b8.pack(side=LEFT)
    b9.pack(side=LEFT)
    b_plus.pack(side=LEFT)

    row2 = Frame(root)
    b4 = Button(row2, text="4", padx=5, pady=5,width=5,font=(20),relief='solid',borderwidth=1,command=(lambda:button_click(4)))
    b5 = Button(row2, text="5", padx=5, pady=5,width=5,font=(20),relief='solid',borderwidth=1,command=(lambda:button_click(5)))
    b6 = Button(row2, text="6", padx=5, pady=5,width=5,font=(20),relief='solid',borderwidth=1,command=(lambda:button_click(6)))
    b_minus = Button(row2, text="-", padx=5, pady=5,width=5,font=(20),relief='solid',borderwidth=1,command=(lambda:action('-')))
    row2.pack(side=TOP, padx=5, pady=5)
    b4.pack(side=LEFT)
    b5.pack(side=LEFT)
    b6.pack(side=LEFT)
    b_minus.pack(side=LEFT)

    row3 = Frame(root)
    b1 = Button(row3, text="1", padx=5, pady=5,width=5,relief='solid',borderwidth=1,font=(20),command=(lambda:button_click(1)))
    b2 = Button(row3, text="2", padx=5, pady=5,width=5,relief='solid',borderwidth=1,font=(20),command=(lambda:button_click(2)))
    b3 = Button(row3, text="3", padx=5, pady=5,width=5,relief='solid',borderwidth=1,font=(20),command=(lambda:button_click(3)))
    b_mul = Button(row3, text="x", padx=5, pady=5,width=5,relief='solid',borderwidth=1,font=(20),command=(lambda:action("*")))
    row3.pack(side=TOP, padx=5, pady=5)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    b3.pack(side=LEFT)
    b_mul.pack(side=LEFT)

    row4 = Frame(root)
    b0 = Button(row4, text="0", padx=5, pady=5,width=5,relief='solid',borderwidth=1,font=(20),command=(lambda:button_click(0)))
    b_dot = Button(row4, text=".", padx=5, pady=5,width=5,relief='solid', borderwidth=1,font=(20),command=(lambda:button_click(".")))
    b_equal = Button(row4, text="=", padx=5 ,pady=5,width=5,relief='solid', borderwidth=1,font=(20),command=equal)
    b_div = Button(row4, text="/", padx=5, pady=5,width=5,relief='solid', borderwidth=1,font=(20),command=(lambda:action("/")))
    row4.pack(side=TOP, padx=5, pady=5)
    b0.pack(side=LEFT)
    b_dot.pack(side=LEFT)
    b_equal.pack(side=LEFT)
    b_div.pack(side=LEFT)

    row5=Frame(root)
    b_clear=Button(row5,text="Clear",font=(15),height=2,width=10,relief='solid',command=clear)
    b_reset = Button(row5, text="Reset",font=(15), height=2,width=10,relief='solid', command=reset)
    row5.pack(side=TOP)
    b_clear.pack(side=LEFT,padx=10,pady=10)
    b_reset.pack(side=RIGHT, padx=10, pady=10)

    b0.bind("<Enter>", on_enter0)
    b0.bind("<Leave>", on_leave0)
    b1.bind("<Enter>", on_enter1)
    b1.bind("<Leave>", on_leave1)
    b2.bind("<Enter>", on_enter2)
    b2.bind("<Leave>", on_leave2)
    b3.bind("<Enter>", on_enter3)
    b3.bind("<Leave>", on_leave3)
    b4.bind("<Enter>", on_enter4)
    b4.bind("<Leave>", on_leave4)
    b5.bind("<Enter>", on_enter5)
    b5.bind("<Leave>", on_leave5)
    b6.bind("<Enter>", on_enter6)
    b6.bind("<Leave>", on_leave6)
    b7.bind("<Enter>", on_enter7)
    b7.bind("<Leave>", on_leave7)
    b8.bind("<Enter>", on_enter8)
    b8.bind("<Leave>", on_leave8)
    b9.bind("<Enter>", on_enter9)
    b9.bind("<Leave>", on_leave9)
    b_plus.bind("<Enter>", on_enter_plus)
    b_plus.bind("<Leave>", on_leave_plus)
    b_minus.bind("<Enter>", on_enter_minus)
    b_minus.bind("<Leave>", on_leave_minus)
    b_mul.bind("<Enter>", on_enter_mul)
    b_mul.bind("<Leave>", on_leave_mul)
    b_div.bind("<Enter>", on_enter_div)
    b_div.bind("<Leave>", on_leave_div)
    b_dot.bind("<Enter>", on_enter_dot)
    b_dot.bind("<Leave>", on_leave_dot)
    b_reset.bind("<Enter>", on_enter_reset)
    b_reset.bind("<Leave>", on_leave_reset)
    b_clear.bind("<Enter>", on_enter_clear)
    b_clear.bind("<Leave>", on_leave_clear)
    b_equal.bind("<Enter>", on_enter_equal)
    b_equal.bind("<Leave>", on_leave_equal)
    calculations = {'+': add, '-': sub, '/': div, '*': mul}
    root.mainloop()
