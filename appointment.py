from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk
from tkcalendar import DateEntry
import adminpanel


def app(win):
    win.title('Appointment')
    #BG
    img=PhotoImage(file="D:\\Project-CSC\\abg - Copy.png")
    q=Label(win,image=img)
    q.place(x=0,y=0)
    Label(win,width=20,pady=4,text='APPOINTMENT',font=('Times New Roman',30,'bold'),bg='#BFDDD1',fg='black',border=0).place(x=350,y=50)

    #Name
    Label(win,width=20,pady=4,text='NAME',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=160)
    Entry(bd=4).place(x=630,y=160,width=250,height=30)

    #Age
    Label(win,width=20,pady=4,text='AGE',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=210)
    Entry(bd=4).place(x=630,y=210,width=250,height=30)

    #Date of Appointment
    Label(win,width=20,pady=4,text='DATE',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=260)
    #Entry(bd=4).place(x=630,y=260,width=250,height=30)
    cal=DateEntry(win,selectmode='day',date_pattern='dd/mm/yyyy',state='readonly').place(x=630,y=260,width=250,height=30)

    #Appointment No
    Label(win,width=26,height=2,text='APPOINTMENT NUMBER',font=('Times New Roman',10,'bold'),bg='white',fg='black',border=0).place(x=320,y=310)
    Entry(bd=4).place(x=630,y=310,width=250,height=30)

    #Gender
    Label(win,width=20,pady=4,text='GENDER',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=360)
    
    gender=StringVar(value='abcd')
    g1=Radiobutton(win,text='Male',variable=gender,value='Male',font='times 15',bg='#BFDDD1')
    g1.select()
    g1.place(x=630,y=360)

    g2=Radiobutton(win,text='Female',variable=gender,value='Female',font='times 15',bg='#BFDDD1')
    g2.deselect()
    g2.place(x=710,y=360)

    g3=Radiobutton(win,text='Others',variable=gender,value='Others',font='times 15',bg='#BFDDD1')
    g3.deselect()
    g3.place(x=810,y=360)

    #Symptoms
    Label(win,width=20,pady=4,text='SYMPTOMS',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=410)
    Entry(bd=4).place(x=630,y=410,width=250,height=30)

    #Specialisation
    Label(win,width=20,pady=4,text='SPECIALISATION',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=460)
    ap=ttk.Combobox(win,width=38,state='readonly')
    ap['values']=('General','Pediatrician','Dermatologist','Ophthalmologist','Cardiologist','Neurologist','ENT Specialist','Radiologist')
    ap.set('Choose your Specialist')
    ap.place(x=630,y=460,width=250,height=30)

    #Mobile No 
    Label(win,width=20,pady=4,text='MOBILE NUMBER',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=510)
    Entry(bd=4).place(x=630,y=510,width=250,height=30)

    #Buttons

    Button(width=20,pady=10,text='BACK',font=('Times New Roman',14,'bold'),bg='#92BAAC',fg='black',border=2,command=adminpanel.admin).place(x=290,y=590)
    Button(width=20,pady=10,text='SAVE',font=('Times New Roman',14,'bold'),bg='#92BAAC',fg='black',border=2).place(x=490,y=590)
    Button(width=20,pady=10,text='CLEAR',font=('Times New Roman',14,'bold'),bg='#92BAAC',fg='black',border=2).place(x=690,y=590)
    #Button(width=20,pady=10,text='BACK',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2).place(x=30,y=590)

    win.mainloop()
