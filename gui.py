import tkinter
from tkinter import messagebox
from tkinter import *

def student():
    Label(root,text="C/C++程序设计").grid(row=0)
    Label(root,text="Python程序设计").grid(row=1)
    Label(root,text="Java程序设计").grid(row=2)
    entry1=Entry(root)
    entry2=Entry(root)
    entry3=Entry(root)
    entry1.grid(row=0,column=1)
    entry2.grid(row=1,column=1)
    entry3.grid(row=2,column=1)
    entry1.insert(10,0)
    entry2.insert(10,0)
    entry3.insert(10,0)
    Label(root,text="平均成绩").grid(row=4)
    entry5=Entry(root)
    entry5.grid(row=4,column=1)
    def printInfo():
        a=int(entry1.get())
        b=int(entry2.get())
        c=int(entry3.get())
        ave=(a+b+c)/3
        entry5.insert(10,ave)
    Button(root,text="计算平均成绩",command=printInfo).grid(row=3,column=1,padx=5,
                                                           pady=5,sticky=W)
  
        
if __name__=="__main__":
    root=tkinter.Tk()
    root.title("学生成绩统计")
    root.geometry=("600x450")
    student()
    root.mainloop()

