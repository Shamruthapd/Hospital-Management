from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk
#import adminpanel

def docdet():
    win=Tk()
    win.title('Doctor Details')
    win.state('zoomed') #full screen
    win.config(bg='pink') #bg

    #IMAGE-background
    

    #Patient ID
    Label(win,width=15,pady=1,text='DOCTOR ID',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=130)
    n1=Entry(bd=4).place(x=630,y=130,width=250)

    #Name
    Label(width=15,pady=1,text='NAME',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=180)
    n2=Entry(bd=4).place(x=630,y=180,width=250)

    #Age
    Label(width=15,pady=1,text='AGE',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=230)
    n3=Entry(bd=4).place(x=630,y=230,width=250)

    #Gender
    Label(width=15,pady=1,text='GENDER',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=280)
    #n5=Entry(bd=4).place(x=630,y=320,width=250)

    gender=StringVar()
    g1=Radiobutton(win,text='Male',variable=gender,value='Male',font='times 15',bg='white')
    g1.select()
    g1.place(x=630,y=280)

    g2=Radiobutton(win,text='Female',variable=gender,value='Female',font='times 15',bg='white')
    g2.deselect()
    g2.place(x=710,y=280)

    g3=Radiobutton(win,text='Others',variable=gender,value='Others',font='times 15',bg='white')
    g3.deselect()
    g3.place(x=810,y=280)

    #Experience
    Label(width=15,pady=1,text='EXPERIENCE',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=330)
    n4=Entry(bd=4).place(x=630,y=330,width=250)

    #Specialist
    Button(width=15,pady=1,text='SPECIALIST',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=380)
    n7=Entry(bd=4).place(x=630,y=380,width=250)

    #Email id
    Label(width=15,pady=1,text='EMAIL ID',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=430)
    n8=Entry(bd=4).place(x=630,y=430,width=250)

    #Phone number
    Label(width=15,pady=1,text='PHONE NO.',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=480)
    n9=Entry(bd=4).place(x=630,y=480,width=250)

    #Back,Add,Update,Delete,Search,Clear

    Button(width=20,pady=10,text='BACK',font=('Times New Roman',14,'bold'),bg='pink',fg='black',border=2).place(x=230,y=590)
    Button(width=20,pady=10,text='DELETE',font=('Times New Roman',14,'bold'),bg='pink',fg='black',border=2).place(x=450,y=590)
    Button(width=20,pady=10,text='SAVE',font=('Times New Roman',14,'bold'),bg='pink',fg='black',border=2).place(x=670,y=590)
    Button(width=20,pady=10,text='CLEAR',font=('Times New Roman',14,'bold'),bg='pink',fg='black',border=2).place(x=890,y=590)

    win.mainloop()

docdet()
