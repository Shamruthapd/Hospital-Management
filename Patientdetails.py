from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk
from tkcalendar import DateEntry


def patdet():
    win=Tk()
    win.title('Patient Details')
    win.state('zoomed') #full screen
    
    #IMAGE-background

    img4=PhotoImage(file="D:\\Project-CSC\\bg3 - Copy.png")
    s=Label(win,image=img4)
    s.place(x=0,y=0)

    #Patient ID
    Label(win,width=15,pady=1,text='PATIENT ID',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=120)
    n1=Entry(bd=4).place(x=630,y=120,width=250)

    #Name
    Label(width=15,pady=1,text='NAME',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=170)
    n2=Entry(bd=4).place(x=630,y=170,width=250)

    #D.O.B
    Label(width=15,pady=1,text='D.O.B',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=220)
    #n3=Entry(bd=4).place(x=630,y=220,width=250)
    cal=DateEntry(win,selectmode='day',date_pattern='dd/mm/yyyy',state='readonly').place(x=630,y=222,width=250,height=27)
    #cal.pack(row=1,column=1,padx=15)
    #cal.pack(padx=15)


    #Age
    Label(width=15,pady=1,text='AGE',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=270)
    n4=Entry(bd=4).place(x=630,y=270,width=250)

    #Gender
    Button(width=15,pady=1,text='GENDER',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=320)
    #n5=Entry(bd=4).place(x=630,y=320,width=250)

    gender=StringVar()
    g1=Radiobutton(win,text='Male',variable=gender,value='Male',font='times 15',bg='white')
    g1.select()
    g1.place(x=630,y=320)

    g2=Radiobutton(win,text='Female',variable=gender,value='Female',font='times 15',bg='white')
    g2.deselect()
    g2.place(x=710,y=320)

    g3=Radiobutton(win,text='Others',variable=gender,value='Others',font='times 15',bg='white')
    g3.deselect()
    g3.place(x=810,y=320)

    #Blood Group
    Label(width=15,pady=1,text='BLOOD GROUP',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=370)
    #n6=Entry(bd=4).place(x=630,y=380,width=250)

    cb=ttk.Combobox(win,width=38,state='readonly')
    cb['values']=('A+ve','B+ve','O+ve','AB+ve','A-ve','B-ve','AB-ve','Others')
    cb.set(cb['values'][0])
    #cb.pack(pady=30)
    cb.place(x=630,y=370,height=27)

    #Email ID
    Button(width=15,pady=1,text='EMAIL ID',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=420)
    n7=Entry(bd=4).place(x=630,y=420,width=250)

    #Address
    Label(width=15,pady=1,text='ADDRESS',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=470)
    n8=Entry(bd=4).place(x=630,y=470,width=250)

    #Phone number
    Label(width=15,pady=1,text='PHONE NO.',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=520)
    n9=Entry(bd=4).place(x=630,y=520,width=250)

    #Back,Add,Update,Delete,Search,Clear

    Button(width=20,pady=10,text='BACK',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2).place(x=30,y=590)
    Button(width=20,pady=10,text='ADD',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2).place(x=240,y=590)
    Button(width=20,pady=10,text='UPDATE',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2).place(x=440,y=590)
    Button(width=20,pady=10,text='DELETE',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2).place(x=640,y=590)
    Button(width=20,pady=10,text='SEARCH',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2).place(x=840,y=590)
    Button(width=20,pady=10,text='CLEAR',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2).place(x=1030,y=590)

    win.mainloop()

#patdet()
