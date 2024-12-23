from tkinter import *
from PIL import Image,ImageTk 
from datetime import date
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import font
import subprocess
import sqlite3
#==================================================
def ex():
    def ex2():
        Exit_window.destroy()
        root.destroy()
    def ex3():
        Exit_window.destroy()
    Exit_window = Toplevel(root)
    Exit_window.title("Exit")
    Exit_window.geometry("300x150+480+230")
    Exit_window.configure(bg="#06283D")
    Label(Exit_window,text="Are you sure to exit for program ?",bg="#06283D", fg="white", font="Arial 12 bold").pack(pady=10)
    yes=Button(Exit_window,text="Yes", width=8, height=2, command=ex2,bg="#06283D", fg="white", font="Arial 12 bold").place(x=50, y=70)
    no=Button(Exit_window,text="No", width=8, height=2, command=ex3,bg="#06283D", fg="white", font="Arial 12 bold").place(x=150, y=70)
#==================================================
def image_background(nameofimage):
    img_open = Image.open(nameofimage)
    img_res=img_open.resize((150,150))
    img_open = img_res.convert("RGBA")
    get_data = img_open.getdata()
    newdata = []
    for temp in get_data:
        newdata.append((temp[0], temp[1], temp[2], 190))
    img_open.putdata(newdata)
    return img_open
#==================================================
root=Tk()
root.title("Gym Registeration")
root.geometry("700x600+300+40")
root.resizable(False,False)
bg_image = image_background("gym5.jpeg")
bg_image_re=bg_image.resize((700,600))
bg_image_tk = ImageTk.PhotoImage(bg_image_re)
bg_label = Label(image=bg_image_tk, bg="black")
bg_label.place(relwidth=1, relheight=1)
#==================================================
#==================================================
def create_db():
    con = sqlite3.connect("Member_data.db")  # إعادة الاتصال بقاعدة البيانات
    pen = con.cursor()  # الحصول على القلم للكتابة في القاعدة
    pen.execute('''CREATE TABLE IF NOT EXISTS member(
                    ID INTEGER,
                    Date Date,
                    Name text,
                    Age INTEGER,
                    Phone Varchar(50),
                    Gender text,
                    Height INTEGER,
                    Weight INTEGER,
                    System  Text,
                    Point INTEGER
                    )''')
def select():
    global radio
    value=radio.get() #radio is the variable
    if value==1:
        Gender="Male"
    elif value==2:
        Gender="Female"
    return Gender
def delete():
    name_g.set("")
    age_g.set("")
    phone_g.set("")
    weight_g.set("")
    height_g.set("")
    system_g.set("Select system")
def create():
    id_val=ID()
    date_val=date_g.get()
    name_val=name_g.get()
    age_val=age_g.get()
    try:
        gender_val=select()
    except:
        messagebox.showerror("error","choose gender")
        return
    phone_val=phone_g.get()
    Weight_val=weight_g.get()
    Height_val=height_g.get()
    system_val=system_g.get()
    if not name_val :
        messagebox.showerror("Error", "Name cannot be empty!")
        return
    elif  name_val.isdigit():
        messagebox.showerror("Error", "Name cannot be countain number!")
        return
    elif not phone_val.isdigit():
        messagebox.showerror("Error", "Phone number must be numeric!")
        return
    elif not Weight_val.isdigit() or int(Weight_val) < 20  :
        messagebox.showerror("Error", "Weight must be greater than 20!")
        return
    elif  not Height_val.isdigit() or  int(Height_val) <= 70 :
        messagebox.showerror("Error", "Height must be greater than 70!")
        return
    elif  not age_val:
        messagebox.showerror("Error", "Age cannot be empty!")
        return
    elif not age_val.isdigit() or int(age_val) <= 8:
        messagebox.showerror("Error", "Age must be greater than 8!")
        return
    elif system_val=="Select system":
        messagebox.showerror("error","choose System")
        return
    try:
        con = sqlite3.connect("Member_data.db") 
        pen = con.cursor()  
        pen.execute('''CREATE TABLE IF NOT EXISTS member(
                    ID INTEGER,
                    Date DATE,
                    Name text,
                    Age INTEGER,
                    Phone Varchar(50),
                    Gender text,
                    Height INTEGER,
                    Weight INTEGER,
                    System  Text,
                    Point INTEGER
                    )''')
        pen.execute('''INSERT INTO member (ID, Date ,Name, Age, Phone, Gender, Height, Weight, System,Point)
                    VALUES (?,?,?,?, ?, ?, ?, ?, ?,?)''', 
                    (id_val,d1,name_val, age_val, phone_val, gender_val, Height_val, Weight_val, system_val,50))
        # pen.execute('''INSERT INTO member (point) VALUES (50)''')
        con.commit()  
        con.close()  
        
        messagebox.showinfo("Success", f"Account created for {name_val}!")  
        ID()
        delete()
    except:
        messagebox.showerror("Error", "Error")
def ID():
    create_db()
    con = sqlite3.connect("Member_data.db")
    pen = con.cursor()
    
    pen.execute("SELECT MAX(ID) FROM member")
    result = pen.fetchone() 

    
    if result[0] is None:
        next_id = 1
    else:
        next_id = result[0] + 1  

    con.close()
    id_g.set(next_id)
    return next_id
def main():
    root.destroy()
    subprocess.run(["python", "main_page.py"])
#==================================================
l1=Label(
    text="New Registretion",
    bg="#06283D",
    width=10,
    height=2,
    fg="white",
    font="arial 22 bold" 
).pack(side=TOP,fill=X) #fill=====>علشاان ياخد العرض كلو
#==================================================
img=Image.open("logo.jpg")
icon_img=Image.open("logo.jpg") #open the photo
image_resizable1=icon_img.resize((80,70))#specifi width and height for photo
convert_image1=ImageTk.PhotoImage(image_resizable1)#convert photo to tkinter
l_image=Label(width=80,height=70,image=convert_image1)
l_image.place(x=0,y=0)
#======================================================
bg_image1 = image_background("gym5.jpeg")
bg_image_re1=bg_image1.resize((30,30))
bg_image_tk1 = ImageTk.PhotoImage(bg_image_re1)
Label(root,text="Name :",font="arial 18 bold",fg="white",bg="#06283D").place(x=140,y=105)
Label(root,text="Age :",font="arial 18 bold",fg="white",bg="#06283D").place(x=140,y=165)
Label(root,text="Phone :",font="arial 18 bold",fg="white",bg="#06283D").place(x=140,y=225)
Label(root,text="Gender :",font="arial 18 bold",fg="white",bg="#06283D").place(x=140,y=285)
Label(root,text="Height :",font="arial 18 bold",fg="white",bg="#06283D").place(x=140,y=345)
Label(root,text="Weight :",font="arial 18 bold",fg="white",bg="#06283D").place(x=140,y=405)
Label(root,text="Kg",font="arial 18 italic",fg="white",bg="#06283D").place(x=346,y=348)
Label(root,text="cm",font="arial 18 italic",fg="white",bg="#06283D").place(x=346,y=405)
Label(root,text="Year",font="arial 18  italic",fg="white",bg="#06283D").place(x=350,y=168)
Label(root,text="System :",font="arial 18  bold ",fg="white",bg="#06283D").place(x=140,y=455)
Label(root,text="ID :",font="arial 18  bold ",fg="white",bg="#06283D").place(x=570,y=75)
Label(text="Date :",bg="#06283D",font="arial 16  bold",fg="white").place(x=0,y=74)
#======================================================
large_font = font.Font(size=17)
date_g=StringVar()
datte=Entry(width=20,font="bold",textvariable=date_g)
current=date.today()
d1=current.strftime("%d/%m/%y")
date_g.set(d1) 
name_g=StringVar()
name=Entry(width=20,textvariable=name_g,font=large_font)
age_g=StringVar()
age=Entry(width=6,textvariable=age_g,font=large_font)
phone_g=StringVar()
phone=Entry(width=20,textvariable=phone_g,font=large_font)
weight_g=StringVar()
weight=Entry(width=6,textvariable=weight_g,font=large_font)
height_g=StringVar()
height=Entry(width=6,textvariable=height_g,font=large_font)
gender_g = IntVar()
radio=IntVar()
male=Radiobutton(text="Male",value=1,variable=radio,font="arial 16 bold italic",fg="White",bg="#06283D",selectcolor="#06283D",command=select)
female=Radiobutton(text="Female",value=2,variable=radio,font="arial 16 bold italic",fg="White",selectcolor="#06283D",bg="#06283D",command=select)
Reg=Button(text="Create New Account",width=17,height=1,font="arial 19 bold italic",bg="#06283D",fg="white",command=create)
system_g=StringVar()
go=Button(text="Back",width=15,height=2,font="arial 10 bold italic",bg="#06283D",fg="white",command=main)
Ex=Button(text="Exit",width=7,height=1,font="arial 12 bold italic",bg="#c21d36",fg="white",command=ex).place(x=617,y=560)
system=Combobox(width=15,height=6,values=["Fitness","Bulking","Weight loss"],textvariable=system_g,font="Ropoto 10",state="r")
system_g.set("Select system")
id_g=IntVar()
id=Entry(width=3,textvariable=id_g,font=large_font)
id_g.set(ID())
id.place(x=620,y=79)
name.place(x=260,y=110)
age.place(x=260,y=170)
phone.place(x=260,y=230)
weight.place(x=260,y=410)
height.place(x=260,y=350)
male.place(x=260,y=285)
female.place(x=360,y=285)
system.place(x=260,y=462)
Reg.place(x=200,y=510)
go.place(x=0,y=555)
datte.place(x=73,y=79)
#======================================================
root.mainloop()