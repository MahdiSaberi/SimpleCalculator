from tkinter import*
import webbrowser
#This class specifies which condition to execute
class ff:
    global flag
    global finger

root = Tk()
root.title('Calculator')
e = Entry(root,width=43,borderwidth=10)
e.grid(column=0,row=0,columnspan=3)
#e.pack()
#define that each code what to do
def Button_nums(number):
    e.insert(999,number)

def Button_plus(sign):
    ff.flag = True
    ff.finger = True
    left_number = e.get()
    global l_num
    l_num = int(left_number)
    e.delete(0,END)


def Button_mine(sign):
    ff.flag = False
    ff.finger = True
    left_number = e.get()
    global l_num
    l_num = int(left_number)
    e.delete(0,END)


def Button_mul(sign):
    ff.flag = True
    ff.finger = False
    left_number = e.get()
    global l_num
    l_num = int(left_number)
    e.delete(0,END)

def Button_dev(sign):
    ff.flag = False
    ff.finger = False
    left_number = e.get()
    global l_num
    l_num = int(left_number)
    e.delete(0,END)


def Button_clear(char):
    e.delete(0,END)

def Button_equal(equal):
        right_number = e.get()
        e.delete(0,END)
        if ff.flag == True and ff.finger == True:
            e.insert(0, int(right_number) + int(l_num))
        elif ff.flag == False and ff.finger == True :
            e.insert(0, abs(int(right_number) - int(l_num)))
        elif ff.flag == True and ff.finger == False:
            e.insert(0, int(right_number) * int(l_num))
        elif ff.flag == False and ff.finger == False:
            e.insert(0, int(l_num) / int(right_number))


#Define Buttons
zero = Button(root,text='0',padx=40,pady=20,bg='#58ff33',command=lambda : Button_nums(0))
#zero.pack()
one = Button(root,text='1',padx=40,pady=20,bg='#58ff33',command=lambda : Button_nums(1))
#one.pack()
two = Button(root,text='2',padx=40,pady=20,bg='#58ff33',command=lambda : Button_nums(2))
#two.pack()
three = Button(root,text='3',padx=40,pady=20,bg='#58ff33',command=lambda : Button_nums(3))
#three.pack()
four = Button(root,text='4',padx=40,pady=20,bg='#58ff33',command=lambda : Button_nums(4))
#four.pack()
five = Button(root,text='5',padx=40,pady=20,bg='#58ff33',command=lambda : Button_nums(5))
#five.pack()
six = Button(root,text='6',padx=40,pady=20,bg='#58ff33',command=lambda : Button_nums(6))
#six.pack()
seven = Button(root,text='7',padx=40,pady=20,bg='#58ff33',command=lambda : Button_nums(7))
#seven.pack()
eight = Button(root,text='8',padx=40,pady=20,bg='#58ff33',command=lambda : Button_nums(8))
#eight.pack()
nine = Button(root,text='9',padx=40,pady=20,bg='#58ff33',command=lambda : Button_nums(9))
#nine.pack()

plus = Button(root,text='+',padx=40,pady=20,bg='orange',command=lambda : Button_plus('+'))
mine = Button(root,text='-',padx=40,pady=20,bg='orange',command=lambda : Button_mine('-'))
mul = Button(root,text='x',padx=39,pady=20,bg='orange',command=lambda : Button_mul('x'))
dev = Button(root,text='/',padx=40,pady=20,bg='orange',command=lambda : Button_dev('/'))
equal = Button(root,text='=',padx=40,pady=20,bg='orange',command=lambda : Button_equal(equal))
clear = Button(root,text='Clear',padx=79,pady=20,bg='red',command=lambda : Button_clear(clear))
about = Button(root,text='About us',padx=19,pady=20,bg='pink',command=lambda : Button_nums(webbrowser.open('https://t.me/mahdsaberi')))

#Show Buttons on Screen
one.grid(row=3,column=0)
two.grid(row=3,column=1)
three.grid(row=3,column=2)

four.grid(row=2,column=0)
five.grid(row=2,column=1)
six.grid(row=2,column=2)

seven.grid(row=1,column=0)
eight.grid(row=1,column=1)
nine.grid(row=1,column=2)

zero.grid(row=4,column=0)

plus.grid(row=4,column=1)
mine.grid(row=4,column=2)

clear.grid(row=5,column=0,columnspan=2)
mul.grid(row=5,column=2)
about.grid(row=6,column=0)
equal.grid(row=6,column=1)
dev.grid(row=6,column=2)

root.mainloop()