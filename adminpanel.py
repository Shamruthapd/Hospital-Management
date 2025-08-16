from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from datetime import datetime
import decimal
from datetime import timedelta

def adminpage():
    
    win=Tk()
    win.title('Admin Panel')
    win.state('zoomed')

    #---------------VIEW APPOINTMENT CODE--------------------
    
    def viewapp():
        root = tk.Tk()
        root.title("Appointment Details")
        root.state('zoomed')
        tk.Label(root, width=20, pady=4, text='APPOINTMENTS', font=('Times New Roman', 30, 'bold'), fg='black', border=0).place(x=500, y=20)

        main_frame = tk.Frame(root)
        main_frame.pack(padx=10, pady=40)


        def buttn1_page():
            def fetch_data():
                selected_date = a1.get()
                query = f"SELECT Appointment_no, Name, Specialisation, Appointment_time FROM appointment WHERE  Date_of_appointment = '{selected_date}'"
                
                try:
                    cursor.execute(query)
                    data = cursor.fetchall()
                    display_data(data)
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error accessing database: {err}")

            # Function to display data in a tabular form
            def display_data(data):
                # Clear previous data in the treeview
                for row in tree.get_children():
                    tree.delete(row)

                # Insert new data into the treeview
                for record in data:
                    tree.insert("", "end", values=record)

            

            # Create and place widgets
            date_label = tk.Label(main_frame, text="Enter Date:",font=('Times New Roman',13,'bold'))
            date_label.pack(pady=10)
            a1 = DateEntry(main_frame, selectmode='day',font=('Times New Roman',13,'bold'), date_pattern='yyyy-mm-dd', state='readonly')
            a1.pack(pady=10)


            fetch_button = tk.Button(main_frame, text="Search",font=('Times New Roman',13,'bold'), command=fetch_data)
            fetch_button.pack(pady=10)

            # Create treeview for displaying data
            columns = ("Appointment No ", " Name ", "Specialisation", "Appointment Time")
            tree = ttk.Treeview(main_frame, columns=columns, show="headings")

            # Set column headings
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=270)

            tree.pack(pady=50)

        def buttn2_page():
            def fetch_data():
                # Get date and doctor ID from entry boxes
                selected_date = a1.get()
                doctor_id = doctor_id_entry.get()

                # Query to retrieve data from the database
                query = f"SELECT Appointment_no,Name, Age,Gender,Symptoms FROM appointment WHERE Date_of_appointment = %s AND  Doctor_ID = %s;"

                cursor.execute(query, (selected_date, doctor_id))
                data = cursor.fetchall()

                # Display data in the table
                display_data(data)

            def display_data(data):
                # Clear previous data
                for row in tree.get_children():
                    tree.delete(row)

                # Display data in the table
                for record in data:
                    tree.insert("", "end", values=record)


            date_label = tk.Label(main_frame, text="Enter Date:",font=('Times New Roman',13,'bold'))
            date_label.pack()
            a1 = DateEntry(main_frame, selectmode='day',font=('Times New Roman',13,'bold'), date_pattern='yyyy-mm-dd', state='readonly')
            a1.pack( pady=10)

            doctor_id_label = tk.Label(main_frame, text="Doctor ID:",font=('Times New Roman',13,'bold'))
            doctor_id_label.pack()

            doctor_id_entry = tk.Entry(main_frame,font=('Times New Roman',13,'bold'))
            doctor_id_entry.pack()

            search_button = tk.Button(main_frame, text="Search",font=('Times New Roman',13,'bold'), command=fetch_data)
            search_button.pack()

            # Table setup
            columns=("Appointment No", "Name", "Age", "Gender", " Symptoms")
            tree = ttk.Treeview(main_frame, columns=columns, show="headings")

            # Set column headings
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=220)

            tree.pack(pady=50)
            
        def delete_pages():
            for Frame in main_frame.winfo_children():
                Frame.destroy()
            
        def hide_indicators():
            buttn1_indicate.config(bg='pink')
            buttn2_indicate.config(bg='pink')
            
        def indicate(lb,page):
            hide_indicators()
            lb.config(bg="black")
            delete_pages()
            page()

        # Create Treeview with scrollbar
        frame = tk.Frame(root,bg='pink')

        buttn1=tk.Button(frame,text='BY DATE',font=('Bold',15),fg='black',bd=0,bg='pink',command=lambda:indicate(buttn1_indicate,buttn1_page))
        buttn1.place(x=10,y=100)
        buttn1_indicate=tk.Label(frame,text='',bg='white')
        buttn1_indicate.place(x=3,y=100,width=5,height=45)

        buttn2=tk.Button(frame,text='BY DOCTOR',font=('Bold',15),fg='black',bd=0,bg='pink',command=lambda:indicate(buttn2_indicate,buttn2_page))
        buttn2.place(x=10,y=300)
        buttn2_indicate=tk.Label(frame,text='',bg='white')
        buttn2_indicate.place(x=3,y=300,width=5,height=45)


        frame.pack(side=tk.LEFT)
        frame.pack_propagate(False)
        frame.configure(width=150,height=768)

        main_frame=tk.Frame(root,highlightbackground='black',highlightthickness=2)

        main_frame.pack(side=tk.LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(height=768,width=1366)

        root.mainloop()

    #--------------------------------------- BOOK APPOINTMENT CODE-------------------------------------------   
    def app(win):
        win.title('Appointment')
        
        #BG
        global img4
        img4=PhotoImage(file="D:\\Project-CSC\\abg - Copy.png")
        q=Label(win,image=img4)
        q.place(x=0,y=0)
        Label(win,width=20,pady=4,text='APPOINTMENT',font=('Times New Roman',30,'bold'),bg='#BFDDD1',fg='black',border=0).place(x=350,y=50)

        #key check
        def correct(inp):
            
            if inp.isdigit() or inp=='':
                return True
            else:
                return False
        
        #Appointment No    
        Label(win,width=26,height=2,text='APPOINTMENT NUMBER',font=('Times New Roman',10,'bold'),bg='white',fg='black',border=0).place(x=320,y=140)
        a1=Entry(bd=4)
        a1.place(x=630,y=140,width=250,height=30)
        q='SELECT  Appointment_No from appointment order by Appointment_No'
        cursor.execute(q) 
        m=cursor.fetchall()
        j=m[-1]
        j_str = j[0]
        n_id = (j_str + 1)
        a1.insert(0, n_id)
        reg=win.register(correct)
        a1.config(validate='key',validatecommand=(reg,'%P'))

        def alph(inp):
            if all(char.isalpha() or char == '.' for char in inp) or inp == '':
                return True
            else:
                return False

        #Name
        Label(win,width=20,pady=4,text='NAME',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=190)
        a2=Entry(win,bd=4)
        a2.place(x=630,y=190,width=250,height=30)
        reg=win.register(alph)
        a2.config(validate='key',validatecommand=(reg,'%P'))

        #Age
        Label(win,width=20,pady=4,text='AGE',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=240)
        a3=Entry(win,bd=4)
        a3.place(x=630,y=240,width=250,height=30)
        reg=win.register(correct)
        a3.config(validate='key',validatecommand=(reg,'%P'))

        #Date of Appointment
        Label(win,width=26,height=2,text='DATE OF APPOINTMENT',font=('Times New Roman',10,'bold'),bg='white',fg='black',border=0).place(x=320,y=290)
        a4=DateEntry(win,selectmode='day',date_pattern='yyyy-mm-dd',state='readonly',mindate=date.today())
        a4.place(x=630,y=290,width=250,height=30)
        
        #Gender
        Label(win,width=20,pady=4,text='GENDER',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=340)
        
        gender=StringVar(value='abcd')
        g1=Radiobutton(win,text='Male',variable=gender,value='Male',font='times 15',bg='#BFDDD1')
        g1.select()
        g1.place(x=630,y=340)

        g2=Radiobutton(win,text='Female',variable=gender,value='Female',font='times 15',bg='#BFDDD1')
        g2.deselect()
        g2.place(x=710,y=340)

        g3=Radiobutton(win,text='Others',variable=gender,value='Others',font='times 15',bg='#BFDDD1')
        g3.deselect()
        g3.place(x=810,y=340)

        #Mobile No
        def phno(inp):
            if inp.isdigit() and len(a5.get())<10 or inp=='':
                return True
            else:
                return False
            
        Label(win,width=20,pady=4,text='MOBILE NUMBER',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=390)
        a5=Entry(bd=4)
        a5.place(x=630,y=390,width=250,height=30)
        reg=win.register(phno)
        a5.config(validate='key',validatecommand=(reg,'%P'))

        #Symptoms    
        Label(win,width=20,pady=4,text='SYMPTOMS',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=440)
        a6=Entry(bd=4)
        a6.place(x=630,y=440,width=250,height=30)
        reg=win.register(alph)
        a6.config(validate='key',validatecommand=(reg,'%P'))
    
        #Specialisation
        Label(win,width=20,pady=4,text='SPECIALISATION',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=490)
        a7=ttk.Combobox(win,width=38,state='readonly')
        a7['values']=('General','Pediatrician','Dermatologist','Ophthalmologist','Cardiologist','Neurologist','ENT Specialist','Radiologist')
        a7.set('Choose your Specialist')
        a7.place(x=630,y=490,width=250,height=30)

        #Appointment time
        Label(win,width=20,pady=4,text='APPOINTMENT TIME',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=320,y=540)
        a8=ttk.Combobox(win,width=38,state='readonly')
        
        a8.place(x=630,y=540,width=250,height=30)
        def update(*args):
            s= a7.get()
            q='select available_time from doctor_details where specialization=%s'
            cursor.execute(q,(s,))
            r=cursor.fetchall()
            times=[]
            for i in r:
                for j in i:
                    times.append(j)
            a8['values'] = times
            a8.set('Choose Appointment Time')

        a7.bind("<<ComboboxSelected>>", update)
        update()
        
        def clear():
            
            a1.delete(0, "end")
            a2.delete(0,'end')
            a3.delete(0,'end')
            a4=DateEntry(win,selectmode='day',date_pattern='yyyy-mm-dd',state='readonly')
            a4.place(x=630,y=290,width=250,height=30)
            g1.select()
            a5.delete(0,'end')
            a6.delete(0,'end')
            a7.set('Choose your Specialist')
            #a7.delete(0,'end')
            a8['values'] = []
            a8.set('Choose Appointment Time')
            
        def save():
            
            a=a1.get()
            b=a2.get()
            c=a3.get()
            d=a4.get()
            e=gender.get()
            f=a5.get()
            g=a6.get()
            h=a7.get()
            i=a8.get()

            if b=='' and c=='' and f=='' and g=='':
                messagebox.showinfo('Invalid','Enter all details')
            else:
                app_info = (a,b,c,d,e,f,g,h,i)
                q="INSERT INTO appointment( Appointment_no,Name,Age,Date_of_appointment,Gender,Mobile_Number,Symptoms,Specialisation,Appointment_time) VALUES ('{}','{}', '{}', '{}', '{}','{}', '{}', '{}','{}')".format(a,b,c,d,e,f,g,h,i)
                cursor.execute(q) # Executing the SQL query
                con.commit()
                q='UPDATE appointment AS a JOIN doctor_details AS d ON a.Specialisation = d.Specialization AND a.Appointment_Time = d.Available_Time SET a.Doctor_ID = d.Doctor_ID'
                cursor.execute(q) # Executing the SQL query
                con.commit()

                messagebox.showinfo("Information", "Saved Successfully")

        def cancel():

            Appointment_no = a1.get()
            q='select * from appointment WHERE  Appointment_No = %s'
            cursor.execute(q,(Appointment_no,))
            r=cursor.fetchone()
            if r is None:
                messagebox.showinfo('Invalid','Appointment not found!')
            else:
                confirmation = messagebox.askquestion("Confirmation", "Are you sure you want to cancel the appointment?")
                if confirmation == 'yes':
                    query = 'DELETE FROM Appointment WHERE Appointment_no=%s'
                    cursor.execute(query, (Appointment_no,))
                    con.commit()
                    messagebox.showinfo('', 'Appointment Cancelled')            

        #Buttons
        Button(width=20,pady=10,text='BACK',font=('Times New Roman',14,'bold'),bg='#92BAAC',fg='black',border=2,command=admin).place(x=200,y=590)
        Button(width=20,pady=10,text='SAVE',font=('Times New Roman',14,'bold'),bg='#92BAAC',fg='black',border=2,command=save).place(x=400,y=590)
        Button(width=20,pady=10,text='CANCEL',font=('Times New Roman',14,'bold'),bg='#92BAAC',fg='black',border=2,command=cancel).place(x=600,y=590)
        Button(width=20,pady=10,text='CLEAR',font=('Times New Roman',14,'bold'),bg='#92BAAC',fg='black',border=2,command=clear).place(x=800,y=590)


        
    #--------------------------------------------------BILL CODE------------------------------------------------------------------------------
    
    def bill(win):
        
        win.title('Bill')
        #IMAGE-background
        global img5
        img5=PhotoImage(file='D:\\Project-CSC\\bg5.png')
        j=Label(win,image=img5)
        j.place(x=0,y=0)
        
        #key check
        def correct(inp):
            
            if inp.isdigit() or inp=='':
                return True
            else:
                return False
            
        #BILL NO. 
        Label(win,width=15,pady=1,text='BILL NO.',font=('Times New Roman',13,'bold'),bg='white',fg='black',border=0).place(x=440,y=120)
        b1=Entry(bd=4,font=('Times New Roman',13,'bold'))
        b1.place(x=640,y=120,width=250)
        q='SELECT BillNo from bill_table'
        cursor.execute(q) 
        m=cursor.fetchall()
        j=m[-1]
        j_str = j[0]
        n_id = (j_str + 1)
        
        b1.config(state='normal')
        b1.delete(0, 'end')
        b1.insert(0, n_id)
        reg=win.register(correct)
        b1.config(validate='key',validatecommand=(reg,'%P'))
        
        
        def pid(inp):
            if inp.isalnum() or inp=='':
                return True
            else:
                return False
        #PATIENT ID
        Label(width=15,pady=1,text='PATIENT ID',font=('Times New Roman',13,'bold'),bg='white',fg='black',border=0).place(x=440,y=170)
        b2=Entry(bd=4,font=('Times New Roman',13,'bold'))
        b2.place(x=640,y=170,width=250)
        reg=win.register(pid)
        b2.config(validate='key',validatecommand=(reg,'%P'))
        
        #DATE
        Label(win,width=15,pady=1,text='DATE',font=('Times New Roman',13,'bold'),bg='white',fg='black',border=0).place(x=440,y=220)
        b3=DateEntry(win,selectmode='day',date_pattern='yyyy-mm-dd',state='readonly',font=('Times New Roman',13,'bold'),maxdate=date.today())
        b3.place(x=640,y=220,width=250,height=30)

        #NAME
        def name(inp):
            if all(char.isalpha() or char == '.' for char in inp) or inp == '':
                return True
            else:
                return False
            
        Label(width=15,pady=1,text='NAME',font=('Times New Roman',13,'bold'),bg='white',fg='black',border=0).place(x=440,y=270)
        b4=Entry(bd=4,font=('Times New Roman',13,'bold'))
        b4.place(x=640,y=270,width=250)
        reg=win.register(name)
        b4.config(validate='key',validatecommand=(reg,'%P'))

        #AGE
        Label(width=15,pady=1,text='AGE',font=('Times New Roman',13,'bold'),bg='white',fg='black',border=0).place(x=440,y=320)
        b5=Entry(bd=4,font=('Times New Roman',13,'bold'))
        b5.place(x=640,y=320,width=250)
        reg=win.register(correct)
        b5.config(validate='key',validatecommand=(reg,'%P'))

        #GENDER
        Label(width=15,pady=1,text='GENDER',font=('Times New Roman',13,'bold'),bg='white',fg='black',border=0).place(x=440,y=370)

        gender=StringVar(value='abcd')
        g1=Radiobutton(win,text='Male',variable=gender,value='Male',font=('Times New Roman',13,'bold'),bg='#FF98B6')
        g1.select()
        g1.place(x=640,y=370)

        g2=Radiobutton(win,text='Female',variable=gender,value='Female',font=('Times New Roman',13,'bold'),bg='#FF98B6')
        g2.deselect()
        g2.place(x=720,y=370)

        g3=Radiobutton(win,text='Others',variable=gender,value='Others',font=('Times New Roman',13,'bold'),bg='#FF98B6')
        g3.deselect()
        g3.place(x=810,y=370)

        #CONSULTING FEE
        Label(width=15,pady=1,text='CONSULTING FEE',font=('Times New Roman',13,'bold'),bg='white',fg='black',border=0).place(x=440,y=420)
        b6=Entry(bd=4,font=('Times New Roman',13,'bold'))
        b6.place(x=640,y=420,width=250)
        reg=win.register(correct)
        b6.config(validate='key',validatecommand=(reg,'%P'))

        #MEDICINE FEE
        Label(width=15,pady=1,text='MEDICINE FEE',font=('Times New Roman',13,'bold'),bg='white',fg='black',border=0).place(x=440,y=470)
        b7=Entry(bd=4,font=('Times New Roman',13,'bold'))
        b7.place(x=640,y=470,width=250)
        reg=win.register(correct)
        b7.config(validate='key',validatecommand=(reg,'%P'))

        #TOTAL
        Label(width=15,pady=1,text='TOTAL',font=('Times New Roman',13,'bold'),bg='white',fg='black',border=0).place(x=440,y=520)
        b8=Entry(bd=4,font=('Times New Roman',13,'bold'))    
        b8.place(x=640,y=520,width=250)
        b8.config(state='disabled')

        def clear():
            
            global b9
            b1.config(state='normal')
            b1.delete(0,'end')
            b1.insert(0,n_id)
            b2.delete(0,'end')
            b9=DateEntry(win,selectmode='day',date_pattern='yyyy-mm-dd',state='readonly',font=('Times New Roman',13,'bold'))
            b9.place(x=640,y=220,width=250,height=30)
            b4.config(state='normal')
            b4.delete(0,'end')
            b5.config(state='normal')
            b5.delete(0,'end')
            b5.config(state='disabled')
            b6.delete(0, "end")
            b7.delete(0,'end')
            b8.config(state='normal')
            b8.delete(0,'end')
            b8.config(state='disabled')
            
        def total():
            
            cf=b6.get()
            mf=b7.get()
            if cf!='' and mf!='':
                s=float(cf)+float(mf)
                tot=s+ (0.05*s)
                b8.config(state='normal')
                b8.delete(0,'end')
                t="%.2f" % tot
                b8.insert(0,t)
                b8.config(state='disabled')
            else:
                messagebox.showinfo('Invalid','Enter consultation and medicinal fee')

        def save():
            
            a=b1.get()
            b=b2.get()
            c=b3.get()
            d=b4.get()
            e=b5.get()
            f=gender.get()
            g=b6.get()
            h=b7.get()
            i=b8.get()
            q="SELECT patientid FROM bill_table "
            cursor.execute(q)
            j=cursor.fetchall()
            if b in j:
                messagebox.showinfo('Invalid','Bill already existing')
            elif a=='' or b=='' or c=='' or d=='' or e=='' or f=='' or g=='' or h=='' or i=='':
                messagebox.showinfo('Invalid','Enter all details')
            else:
                bill_info = (a,b,c,d,e,f,g,h,i)
                q="INSERT INTO BILL_TABLE (BillNo,PatientID,Date,Name, Age,Gender,ConsultingFee, MedicineFee, Total) VALUES ({},'{}','{}', '{}', {}, '{}',{}, {}, {})".format(a,b,c,d,e,f,g,h,i)
                cursor.execute(q) # Executing the SQL query
                con.commit()
                messagebox.showinfo('Information','Successfully Saved')

        def search():
            
                b2.config(state='disabled')
                clear()
                b1.delete(0, 'end')
                b2.config(state='normal')
                patient_id = b2.get()
                # Execute the SQL query to search for a patient
                query = "SELECT * FROM Patient_details WHERE Patient_Id=%s"
                data = (patient_id,)
                cursor.execute(query, data)
                result = cursor.fetchone()
                q="SELECT billno,ConsultingFee, MedicineFee ,Total FROM bill_table WHERE PatientId=%s"
                cursor.execute(q,(patient_id,))
                j=cursor.fetchone()
                if result:
                    b1.insert(0,j[0])
                    b1.config(state='disabled')
                    b4.insert(0, result[1])
                    b4.config(state='disabled')
                    b5.config(state='normal')
                    b5.delete(0,'end')
                    b5.insert(0, result[3])
                    b5.config(state='disabled')
                    d = result[2].strftime('%Y-%m-%d')
                    b9.set_date(d)
                    
                    if result[4]=='Male':
                        g1.select()
                        g2.deselect()
                        g3.deselect()
                        gender.set('Male')
                    elif result[4]=='Female':
                        g1.deselect()
                        g2.select()
                        g3.deselect()
                        gender.set('Female')
                    else:
                        g1.select()
                        g2.deselect()
                        g3.select()
                        gender.set('Others')
                else:
                    messagebox.showinfo("Invalid", "Patient not found")

        def bill_prnt():
            
            patient_id = b2.get()
            q="SELECT * FROM bill_table WHERE PatientId=%s"
            cursor.execute(q,(patient_id,))
            data=cursor.fetchone()
            
            if data==None:
                messagebox.showinfo("Invalid", "Patient not found")
            else:
                win2 = Toplevel()  
                win2.title('Final Bill')
                win2.state('zoomed')

                img7 = PhotoImage(file="D:\\Project-CSC\\billprnt.png")
                s = Label(win2, image=img7)
                s.place(x=0, y=0)

                Label(win2,width=10,pady=3,text=date.today(),font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=100,y=200)
                t= datetime.now().time()
                ft = t.strftime("%I:%M:%S %p")
                Label(win2,width=10,pady=3,text=ft,font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=150,y=265)
                
                
                p=decimal.Decimal('0.05')
                s=(data[6] + data[7]) * p
                Label(win2,width=2,pady=3,text=data[0],font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=135,y=235)
                Label(win2,width=8,pady=3,text=data[3],font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=470,y=200)
                Label(win2,width=2,pady=3,text=data[4],font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=460,y=235)
                Label(win2,width=8,pady=3,text=data[5],font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=485,y=265)
                Label(win2,width=8,pady=3,text=data[6],font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=700,y=370)
                Label(win2,width=8,pady=3,text=data[7],font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=700,y=420)
                Label(win2,width=8,pady=3,text=data[6]+data[7],font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=700,y=575)
                Label(win2,width=8,pady=3,text=s,font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=900,y=575)
                Label(win2,width=8,pady=3,text=data[8],font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=1100,y=575)

                q="SELECT email,phone_no FROM patient_details WHERE Patient_Id=%s"
                cursor.execute(q,(patient_id,))
                data=cursor.fetchone()
                Label(win2,width=20,pady=3,text=data[0],font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=890,y=200)
                Label(win2,width=15,pady=3,text=data[1],font=('Times New Roman',18),bg='white',fg='black',border=0).place(x=940,y=235)

                win2.mainloop()            
                        
        Button(width=20,pady=10,text='BACK',font=('Times New Roman',14,'bold'),bg='#F985A8',fg='black',border=2,command=admin).place(x=50,y=590)
        Button(width=20,pady=10,text='CLEAR',font=('Times New Roman',14,'bold'),bg='#F985A8',fg='black',border=2,command=clear).place(x=250,y=590)
        Button(width=20,pady=10,text='SUBMIT',font=('Times New Roman',14,'bold'),bg='#F985A8',fg='black',border=2,command=save).place(x=450,y=590)
        Button(width=20,pady=10,text='SEARCH',font=('Times New Roman',14,'bold'),bg='#F985A8',fg='black',border=2,command=search).place(x=650,y=590)
        Button(width=20,pady=10,text='TOTAL',font=('Times New Roman',14,'bold'),bg='#F985A8',fg='black',border=2,command=total).place(x=850,y=590)
        Button(width=18,pady=10,text='PRINT',font=('Times New Roman',14,'bold'),bg='#F985A8',fg='black',border=2,command=bill_prnt).place(x=1050,y=590)



    #-------------------------------------PATIENT DETAILS CODE-----------------------------------------
    def patient_dt(win):
    
        win.title('Patient Details')
        
        #IMAGE-background
        global img6
        img6=PhotoImage(file="D:\\Project-CSC\\bg3 - Copy.png")
        s=Label(win,image=img6)
        s.place(x=0,y=0)
           
        #Patient ID
        q='SELECT Patient_Id from Patient_details'
        cursor.execute(q) 
        m=cursor.fetchall()
        j=m[-1]
        j_str = j[0]  # Extract the string value
        numeric_part = int(j_str[1:])  # Extract the numeric part
        n_id = 'P{:03d}'.format(numeric_part + 1) 
        
        def pid(inp):
            if inp.isalnum() or inp=='':
                return True
            else:
                return False
            
        Label(win,width=15,pady=1,text='PATIENT ID',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=120)
        n1=Entry(win,bd=4)
        n1.place(x=630,y=120,width=250)
        n1.config(state='normal')
        n1.delete(0, 'end')
        n1.insert(0, n_id)
        
        #Name
        def name(inp):
            if all(char.isalpha() or char == '.' for char in inp) or inp == '':
                return True
            else:
                return False
            
        Label(width=15,pady=1,text='NAME',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=170)
        n2=Entry(bd=4)
        n2.place(x=630,y=170,width=250)
        reg=win.register(name)
        n2.config(validate='key',validatecommand=(reg,'%P'))

        def calculate_age(event=None):
            
            dob = n3.get_date()
            # Calculate age in years and months
            today = date.today()
            age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

            if age_years < 1:
                age_months = (today.year - dob.year) * 12 + today.month - dob.month
                age = f"{age_months} months"
            else:
                age = str(age_years)

            # Update the Entry widget with the calculated age
            n4.config(state='normal')
            n4.delete(0, 'end')
            n4.insert(0, age)
            n4.config(state='disabled')

        #D.O.B
        Label(width=15,pady=1,text='D.O.B',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=220)
        n3=DateEntry(win,selectmode='day',date_pattern='yyyy-mm-dd',state='readonly',maxdate=date.today())
        n3.place(x=630,y=222,width=250,height=27)
        n3.bind("<<DateEntrySelected>>", calculate_age)
        
        #Age
        Label(width=15,pady=1,text='AGE',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=270)
        n4=Entry(bd=4)
        n4.place(x=630,y=270,width=250)
        n4.config(state='disabled')
        
        #Gender
        Label(width=15,pady=1,text='GENDER',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=320)

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
        n6=ttk.Combobox(win,width=38,state='readonly')
        n6['values']=('Choose your blood group','A+ve','B+ve','O+ve','AB+ve','A-ve','B-ve','AB-ve','Others')
        n6.set(n6['values'][0])
        n6.place(x=630,y=370,height=27)

        #Email ID
        Label(width=15,pady=1,text='EMAIL ID',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=420)
        n7=Entry(win,bd=4)
        n7.place(x=630,y=420,width=250)

        #Address
        Label(width=15,pady=1,text='ADDRESS',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=470)
        n8=Entry(win,bd=4)
        n8.place(x=630,y=465,width=250,height=40)

        #Phone number
        def phno(inp):
            if inp.isdigit() and len(n9.get())<10 or inp=='':
                return True
            else:
                return False
   
        Label(width=15,pady=1,text='PHONE NO.',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=530)
        n9=Entry(bd=4)
        n9.place(x=630,y=530,width=250)
        reg=win.register(phno)
        n9.config(validate='key',validatecommand=(reg,'%P'))
        
        def update():
            
            a=n1.get()
            b=n2.get()
            c=n3.get()
            d=n4.get()
            e=gender.get()
            f=n6.get()
            g=n7.get()
            h=n8.get()
            i=n9.get()
            
            if b!='':
                q = 'UPDATE Patient_details SET Name = %s WHERE Patient_Id = %s'
                cursor.execute(q,(b, a))
            if c!='' and d!='':
                q='UPDATE Patient_details SET DOB_Date=%s ,Age=%s WHERE Patient_Id=%s'
                cursor.execute(q,(c,d, a))     
            if e!='':
                q='UPDATE Patient_details SET Gender=%s WHERE Patient_Id=%s'
                cursor.execute(q,(e, a))
            if f in ('A+ve','B+ve','O+ve','AB+ve','A-ve','B-ve','AB-ve','Others'):
                q='UPDATE Patient_details SET  Blood_group=%s WHERE Patient_Id=%s'
                cursor.execute(q,(f, a))
            if g!='':
                q='UPDATE Patient_details SET  Email=%s WHERE Patient_Id=%s'
                cursor.execute(q,(g, a))
            if h!='':
                q='UPDATE Patient_details SET  Address=%s WHERE Patient_Id=%s'
                cursor.execute(q,(h, a))
            if i!='':
                q='UPDATE Patient_details SET  Phone_No=%s WHERE Patient_Id=%s'
                cursor.execute(q,(i, a))
            con.commit()
            q='select * from Patient_details WHERE Patient_Id = %s'
            cursor.execute(q,(a,))
            r=cursor.fetchone()
            if r is None:
                messagebox.showinfo('Invalid','Patient not existing')
            else:
                messagebox.showinfo('','Successfully Updated')

        def delete():

            a=n1.get()
            q='select * from Patient_details WHERE Patient_Id = %s'
            cursor.execute(q,(a,))
            r=cursor.fetchone()
            if r is None:
                messagebox.showinfo('Invalid','Patient not existing')
            else:
                confirmation = messagebox.askquestion("Confirmation", "Are you sure you want to delete?")
                if confirmation == 'yes':
                    q='DELETE FROM Patient_details WHERE Patient_Id=%s'
                    cursor.execute(q,(a,))
                    con.commit()
                    messagebox.showinfo('','Successfully Deleted')

        def clear():
            
            global n10
            n1.delete(0, "end")
            n2.delete(0,'end')
            n10=DateEntry(win,selectmode='day',date_pattern='yyyy-mm-dd',state='readonly')
            n10.place(x=630,y=222,width=250,height=27)
            n4.config(state='normal')
            n4.delete(0,'end')
            n4.config(state='disabled')
            g2.select()
            gender.set('Male')
            n6.set(n6['values'][0])
            n7.delete(0,'end')
            n8.delete(0,'end')
            n9.delete(0,'end')
            
        def search():
                
                patient_id = n1.get()
                clear()
                query = "SELECT * FROM Patient_details WHERE Patient_Id=%s"
                data = (patient_id,)
                cursor.execute(query, data)
                result = cursor.fetchone()
                if result:
                    n1.insert(0, result[0])
                    n2.insert(0, result[1])
                    n4.config(state='normal')
                    n4.delete(0,'end')
                    n4.insert(0, result[3])
                    n4.config(state='disabled')
                    n6.set( result[5])
                    n7.insert(0, result[6])
                    n8.insert(0, result[7])
                    n9.insert(0, result[8])
                    d = result[2].strftime('%Y-%m-%d')
                    n10.set_date(d)

                    if result[4]=='Male':
                        g1.select()
                        g2.deselect()
                        g3.deselect()
                        gender.set('Male')
                    elif result[4]=='Female':
                        g1.deselect()
                        g2.select()
                        g3.deselect()
                        gender.set('Female')
                    else:
                        g1.select()
                        g2.deselect()
                        g3.select()
                        gender.set('Others')
                    
                else:
                    messagebox.showinfo("Invalid", "Patient not found")
     
        
        def save():
            
            a=n1.get()
            b=n2.get()
            c=n3.get()
            d=n4.get()
            e=gender.get()
            f=n6.get()
            g=n7.get()
            h=n8.get()
            i=n9.get()
            
            if b=='' and d=='' and g=='' and h=='' and i=='':
                messagebox.showinfo("Invalid", "Enter all details")
            else:
                pat_info = (a,b,c,d,e,f,g,h,i)
                # SQL query to insert data into the table
                q="INSERT INTO Patient_details(Patient_Id,Name,DOB_Date,Age,Gender,Blood_group,Email,Address,Phone_No) VALUES ('{}','{}', '{}', '{}', '{}','{}', '{}', '{}',{})".format(a,b,c,d,e,f,g,h,i)
                cursor.execute(q) # Executing the SQL query
                con.commit()
                messagebox.showinfo("Information", "Saved Successfully")
 
        Button(width=20,pady=10,text='BACK',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2,command=admin).place(x=30,y=590)
        Button(width=20,pady=10,text='SAVE',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2,command=save).place(x=240,y=590)
        Button(width=20,pady=10,text='UPDATE',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2,command=update).place(x=440,y=590)
        Button(width=20,pady=10,text='DELETE',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2,command=delete).place(x=640,y=590)
        Button(width=20,pady=10,text='SEARCH',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2,command=search).place(x=840,y=590)
        Button(width=20,pady=10,text='CLEAR',font=('Times New Roman',14,'bold'),bg='light blue',fg='black',border=2,command=clear).place(x=1030,y=590)
                  

    #------------------------------------DOCTOR DETAILS CODE---------------------------------------
    def doctor(win):
        
        win.title('Doctor Details')
        win.state('zoomed') #full screen

        #IMAGE-background
        global img7
        img7=PhotoImage(file="D:\\Project-CSC\\bg6.png")
        s=Label(win,image=img7)
        s.place(x=0,y=0)

        #entrybox validation
        def correct(inp):
            if inp.isdigit() or inp=='':
                return True
            else:
                return False
            
        #Doctor ID
        q='SELECT Doctor_ID from Doctor_details'
        cursor.execute(q) 
        m=cursor.fetchall()
        j=m[-1]
        j_str = j[0]  # Extract the string value
        numeric_part = int(j_str[1:])  # Extract the numeric part
        n_id = 'D{:03d}'.format(numeric_part + 1)
        def did(inp):
            if inp.isalnum() or inp=='':
                return True
            else:
                return False
            
        Label(win,width=15,pady=1,text='DOCTOR ID',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=130)
        d1=Entry(bd=4)
        d1.place(x=630,y=130,width=250)
        d1.insert(0,n_id)
        reg=win.register(did)
        d1.config(validate='key',validatecommand=(reg,'%P'))

        #Name
        def name(inp):
            if all(char.isalpha() or char == '.' for char in inp) or inp == '':
                return True
            else:
                return False
            
        Label(width=15,pady=1,text='NAME',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=180)
        d2=Entry(bd=4)
        d2.place(x=630,y=180,width=250)
        reg=win.register(name)
        d2.config(validate='key',validatecommand=(reg,'%P'))

        #Age
        Label(width=15,pady=1,text='AGE',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=230)
        d3=Entry(bd=4)
        d3.place(x=630,y=230,width=250)
        reg=win.register(correct)
        d3.config(validate='key',validatecommand=(reg,'%P'))

        #Gender
        Label(width=15,pady=1,text='GENDER',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=280)
        
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
        d4=Entry(bd=4)
        d4.place(x=630,y=330,width=250)
        reg=win.register(correct)
        d4.config(validate='key',validatecommand=(reg,'%P'))

        #Specialist
        Label(width=15,pady=1,text='SPECIALISATION',font=('Times New Roman',11,'bold'),bg='white',fg='black',border=0).place(x=420,y=380)
        d5=Entry(bd=4)
        d5=ttk.Combobox(win,width=38,state='readonly')
        d5['values']=('General','Pediatrician','Dermatologist','Ophthalmologist','Cardiologist','Neurologist','ENT Specialist','Radiologist')
        d5.set(d5['values'][0])
        d5.place(x=630,y=380,width=250)

        #Email id
        Label(width=15,pady=1,text='EMAIL ID',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=430)
        d6=Entry(bd=4)
        d6.place(x=630,y=430,width=250)

        #Phone number
        def phno(inp):
            if inp.isdigit() and len(d7.get())<10 or inp=='':
                return True
            else:
                return False
        Label(width=15,pady=1,text='PHONE NO',font=('Times New Roman',12,'bold'),bg='white',fg='black',border=0).place(x=420,y=480)
        d7=Entry(bd=4)
        d7.place(x=630,y=480,width=250)
        reg=win.register(phno)
        d7.config(validate='key',validatecommand=(reg,'%P'))

        #Time
        def get_time():
            
            global d8
            selected_hour1 = hour1.get()
            selected_hour2 = hour2.get()
            selected_am_pm1 = am_pm1.get()
            selected_am_pm2 = am_pm2.get()
            d8= f"{selected_hour1} {selected_am_pm1} - {selected_hour2} {selected_am_pm2}"

        Label(width=20,height=2,text='AVAILABLE TIME',font=('Times New Roman',10,'bold'),bg='white',fg='black',border=0).place(x=420,y=530)
        Label(width=5,height=2,text='to',font=('Times New Roman',10,'bold'),bg='#FFD2D2',fg='black',border=0).place(x=730,y=530)
        
        # Hour selection using Spinbox
        hour1 = tk.Spinbox(win, from_=1, to=12, wrap=True,width=3, readonlybackground="white", state="readonly")
        hour1.pack()
        hour1.place(x=630,y=533)

        hour2 = tk.Spinbox(win, from_=1, to=12, wrap=True,width=3, readonlybackground="white", state="readonly")
        hour2.pack()
        hour2.place(x=780,y=533)
         
        # AM/PM selection using custom Spinbox
        am_pm1 = tk.Spinbox(win, values=("AM", "PM"), wrap=True, width=4,readonlybackground="white", state="readonly")
        am_pm1.pack()
        am_pm1.place(x=680,y=533)

        am_pm2 = tk.Spinbox(win, values=("AM", "PM"), wrap=True, width=4,readonlybackground="white", state="readonly")
        am_pm2.pack()
        am_pm2.place(x=830,y=533)

        #Back,Save,Cancel,Clear

        def clear():
            
            d1.delete(0, "end")
            d2.delete(0,'end')
            d3.delete(0,'end')
            d4.delete(0,'end')
            d5.set(n6['values'][0])
            d6.delete(0,'end')
            d7.delete(0,'end')

        def save():
            
            get_time()
            a= d1.get()
            b= d2.get()
            c=d3.get()
            d= gender.get()  
            e= d4.get()
            f= d5.get()
            g= d6.get()
            h= d7.get()
            i= d8

            q='select * from Doctor_details WHERE Doctor_Id = %s'
            cursor.execute(q,(a,))
            r=cursor.fetchall()
            if r is not  None:
                messagebox.showinfo('Invalid','Doctor already existing')
            elif b=='' or c=='' or e=='' or f=='' or g=='':
                messagebox.showinfo('Invalid','Enter all details')
            else:
                doc_info = (a,b,c,d,e,f,g,h,i)
                q="INSERT INTO Doctor_details(Doctor_ID,Name,Age,Gender,Experience,Specialization,Email,Phone_No,Available_Time) VALUES ('{}','{}',{},'{}',{},'{}','{}','{}','{}')".format(a,b,c,d,e,f,g,h,i)
                cursor.execute(q) # Executing the SQL query
                con.commit()
                messagebox.showinfo("Information", "Saved Successfully")

        def delete():
            
            a=d1.get()
            q='select * from Doctor_details WHERE Doctor_Id = %s'
            cursor.execute(q,(a,))
            r=cursor.fetchone()
            if r is None:
                messagebox.showinfo('Invalid','Doctor not existing')
            else:
                confirmation = messagebox.askquestion("Confirmation", "Are you sure you want to delete?")
                if confirmation == 'yes':
                        q='DELETE FROM Doctor_details WHERE Doctor_Id=%s'
                        cursor.execute(q,(a,))
                        con.commit()
                        messagebox.showinfo('Information','Successfully Deleted')
                    
        Button(width=20,pady=10,text='BACK',font=('Times New Roman',14,'bold'),bg='pink',fg='black',border=2,command=admin).place(x=230,y=590)
        Button(width=20,pady=10,text='DELETE',font=('Times New Roman',14,'bold'),bg='pink',fg='black',border=2,command=delete).place(x=450,y=590)
        Button(width=20,pady=10,text='SAVE',font=('Times New Roman',14,'bold'),bg='pink',fg='black',border=2,command=save).place(x=670,y=590)
        Button(width=20,pady=10,text='CLEAR',font=('Times New Roman',14,'bold'),bg='pink',fg='black',border=2).place(x=890,y=590)

        
    #-------------------------------------ADMIN PANEL CODE---------------------------------------------    
    def admin():

        #mysql-python interface
        global cursor,con
        import mysql.connector as sql
        con=sql.connect(host='localhost',user='root',password='Today@123',database='hospital')
        cursor =con.cursor()

        win.title('Admin Panel')
        global img2,img3
        img2=PhotoImage(file="D:\\Project-CSC\\hmbg - Copy.png")
        img3=PhotoImage(file="D:\\Project-CSC\\design - Copy.PNG")
        s=Label(win,image=img2)
        Label(win,image=img3).place(x=625,y=175)
        Label(win,width=20,pady=4,text='ADMIN PANEL',font=('Times New Roman',30,'bold'),bg='white',fg='black',border=0).place(x=350,y=50)
        s.place(x=0,y=0)

        def pat_det():
            
            patient_dt(win)
    
        def log_out():
            
            win.destroy()
            import Csc_Project
            Csc_Project.hospital()

        def bill_pay():

            bill(win)

        def appointment():

            app(win)

        def doc_det():

            doctor(win)
                       
        #AdminPanel Buttons   
        Button(width=30,pady=10,text='PATIENT DETAILS',font=('Times New Roman',14,'bold'),bg='white',fg='black',border=3,command=pat_det).place(x=170,y=220)
        Button(width=30,pady=10,text=' BOOK APPOINTMENT',font=('Times New Roman',14,'bold'),bg='white',fg='black',border=3,command=appointment).place(x=170,y=290)
        Button(width=30,pady=10,text='VIEW APPOINTMENTS',font=('Times New Roman',14,'bold'),bg='white',fg='black',border=3,command=viewapp).place(x=170,y=360)
        Button(width=30,pady=10,text='BILL',font=('Times New Roman',14,'bold'),bg='white',fg='black',border=3,command=bill_pay).place(x=170,y=430)
        Button(width=30,pady=10,text='DOCTOR DETAILS',font=('Times New Roman',14,'bold'),bg='white',fg='black',border=3,command=doc_det).place(x=170,y=500)
        Button(width=30,pady=10,text='LOG OUT',font=('Times New Roman',14,'bold'),bg='white',fg='black',border=3,command=log_out).place(x=170,y=570)

        win.mainloop()
        
    admin()
    cursor.close()
    con.close()

