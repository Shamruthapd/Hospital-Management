from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def hospital():  
    global button_mode
    win=Tk()
    win.title('Global Health Hospital')
    win.state('zoomed') #full screen
    #win.config(bg='pink') #bg

    #IMAGE-background
    img=PhotoImage(file="D:\\Project-CSC\\cscproj - Copy.png")
    q=Label(win,image=img)
    q.place(x=0,y=0)
    img2=PhotoImage(file="D:\\Project-CSC\\plus symbol.png")
    p=Label(win,image=img2)
    p.place(x=240,y=10)

    def signin(): 
        username=user.get()
        password=code.get()
        if username=='Shamrutha' and password=='Project@12':
            messagebox.showinfo('Information','Login Successfull')
            win.destroy()
            import adminpanel
            adminpanel.adminpage()
                        
        elif username!='Shamrutha' or password!='Project@12':
            messagebox.showinfo('Invalid','Enter correct username and password')
            
    frame=Frame(win,width=300,height=300,bg='white')
    frame.place(x=800,y=200)

    heading=Label(frame,text='Sign in',fg='black',bg='white',font=('Teletype',23))
    heading.place(x=100,y=15)

    def on_enter(e):
        user.delete(0,'end')
        
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
            
    user=Entry(frame,width=22,fg='black',border=0,font=('Teletype',11))
    user.place(x=40,y=75)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=245,height=2,bg='black').place(x=25,y=103)

    def on_enter(e):
        if code.get()=='Password':
            code.delete(0,'end')
            code.config(show='•')
            eyebutton.config(image=closeeye)
            
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
            code.config(show='')

    code=Entry(frame,width=22,fg='black',border=0,font=('Teletype',11))
    code.place(x=40,y=160)
    code.insert(0,'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    #Password eye button
    button_mode=True
    def show():       
        global button_mode
        if button_mode==True:
            eyebutton.config(image=openeye,activebackground='white')
            code.config(show='')
            button_mode=False
        else:
            if code.get()!='Password':
                eyebutton.config(image=closeeye,activebackground='white')
                code.config(show='•')
                button_mode=True

    openeye=PhotoImage(file='D:\\Project-CSC\\openeye.png')
    closeeye=PhotoImage(file='D:\\Project-CSC\\closeeye.png')
    eyebutton=Button(frame,image=closeeye,bg='#375174',bd=0,command=show)
    eyebutton.place(x=220,y=160)

    Frame(frame,width=245,height=2,bg='black').place(x=25,y=187)
    Button(frame,width=35,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=25,y=220)

    win.mainloop()

hospital()

