from tkinter import *
from PIL import Image,ImageTk 
from tkinter import messagebox
from tkinter import font
import subprocess
import sqlite3
#==================================================
def ex():
    def ex2():
        Exit_window.destroy()
        obj.destroy()
    def ex3():
        Exit_window.destroy()
    Exit_window = Toplevel(obj)
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
    get_data = img_res.getdata()
    newdata = []
    for temp in get_data:
        newdata.append((temp[0], temp[1], temp[2], 190))
    img_open.putdata(newdata)
    return img_open
#==================================================
def Back():
    obj.destroy()
    subprocess.run(["python", "main_page.py"])
def show_points(newpoint):
    def Back2():
        obj2.destroy()
        subprocess.run(["python", "main_page.py"])
    obj2=Tk()
    obj2.title("Gym Registeration")
    obj2.geometry("500x300+380+150")
    obj2.configure(bg="#06283D")
    obj2.resizable(False,False)
    bg_image3 = image_background("gym5.jpeg")
    bg_image_re3=bg_image3.resize((600,300))
    bg_image_tk3 = ImageTk.PhotoImage(bg_image_re3)
    bg_label = Label(image=bg_image_tk3, bg="#06283D")
    bg_label.place(relwidth=1, relheight=1)
    l1=Label(
    text="Points",
    bg="#06283D",
    width=10,
    height=2,
    fg="white",
    font="arial 28 bold" 
    ).pack(side=TOP,fill=X)
    icon_img2=Image.open("logo.jpg") #open the photo
    image_resizable2=icon_img2.resize((100,100))#specifi width and height for photo
    convert_image2=ImageTk.PhotoImage(image_resizable2)#convert photo to tkinter
    l_image=Label(width=100,height=91,image=convert_image2)
    l_image.image = convert_image2
    l_image.place(x=0,y=0)
    Label(text=" Your point is :",bg="#06283D",width=12,height=1,fg="white",font="arial 20 bold" ).place(x=78,y=160)
    en_point_g=StringVar()
    en_point=Entry(width=8,font="arial 21 bold",textvariable=en_point_g).place(x=290,y=160)
    en_point_g.set(newpoint)
    go=Button(text="Back",width=10,height=2,bg="#06283D",fg="white",command=Back2).place(x=0,y=260)
    obj2.mainloop()
def log_in():
    user_name_val = user_name_g.get()
    password_val = pass_g.get()
    con = sqlite3.connect("Member_data.db")
    pen = con.cursor()

    try:
        if not user_name_val:
            messagebox.showerror("Login Failed", "Enter Username")
            return
        if not password_val:
            messagebox.showerror("Login Failed", "Enter ID")
            return

        # استعلام التحقق
        pen.execute("SELECT * FROM member WHERE Name = ? AND ID = ? ", (user_name_val, password_val))
        check = pen.fetchone() 

        if check:  
            pen.execute("SELECT Point FROM member WHERE Name = ? AND ID = ?", (user_name_val, password_val))
            result = pen.fetchone()
            current_points = result[0]
            new_points = current_points - 1
            pen.execute("UPDATE member SET Point = ? WHERE Name = ? AND ID = ?", (new_points, user_name_val, password_val))
            con.commit()  
            messagebox.showinfo("Login Success", "Success login")
            
            obj.destroy()
            show_points(str(new_points))
            # subprocess.run(["python", "all_member.py"])
        else:
            messagebox.showerror("Login Failed", "Invalid Username or ID")
            user_name_g.set("")
            pass_g.set("")
    except:
        messagebox.showerror("Login Failed", "Error:No data in database ")
        user_name_g.set("")
        pass_g.set("")
    con.close()
#==================================================
obj = Tk()
obj.title("Gym Registration")
obj.geometry("700x600+300+40")
obj.resizable(False, False)
bg_image = image_background("gym5.jpeg")
bg_image_re=bg_image.resize((700,600))
bg_image_tk = ImageTk.PhotoImage(bg_image_re)
bg_label = Label(image=bg_image_tk, bg="#06283D")
bg_label.place(relwidth=1, relheight=1)
#================================================= 
#================================================= 
def create():
    obj.destroy()
    subprocess.run(["python", "gym.py"])
# def log_in():
#     obj.destroy()
#     subprocess.run(["python", "gym.py"])
def Show():
    obj.destroy()
    subprocess.run(["python", "all_member.py"])
#================================================= 
l1=Label(
    text="Log In",
    bg="#06283D",
    width=10,
    height=2,
    fg="white",
    font="arial 28 bold" 
).pack(side=TOP,fill=X)
l2=Label(
    text="Today's struggle, tomorrow's strength!🏆💥",
    bg="#06283D",
    width=10,
    height=2,
    fg="white",
    font="arial 18 bold italic" 
).pack(side=BOTTOM,fill=X)
icon_img=Image.open("logo.jpg") #open the photo
image_resizable1=icon_img.resize((100,100))#specifi width and height for photo
convert_image1=ImageTk.PhotoImage(image_resizable1)#convert photo to tkinter
l_image=Label(width=100,height=91,image=convert_image1)
l_image.place(x=0,y=0)
#=============================================================
Label(text="User_name :",font="arial 18 bold",fg="white",bg="#06283D").place(x=120,y=250)
Label(text="ID :",font="arial 18 bold",fg="white",bg="#06283D").place(x=170,y=330)
#=============================================================
large_font = font.Font(size=17)
user_name_g=StringVar()
user_name=Entry(width=23,textvariable=user_name_g,font=large_font)
pass_g=StringVar()
password=Entry(width=23,textvariable=pass_g,font=large_font)
login=Button(text="Log In",width=15,height=1,font="arial 20 bold italic",bg="#06283D",fg="white",command=log_in)
go=Button(text="Back",width=10,height=1,command=Back,bg="#06283D",fg="white",font="bold").place(x=0,y=494)
Ex=Button(text="Exit",width=7,height=1,font="arial 12 bold italic",bg="#c21d36",fg="white",command=ex).place(x=617,y=500)
#=============================================================
user_name.place(x=270,y=253)
password.place(x=270,y=333)
login.place(x=247,y=390)
#=============================================================
obj.mainloop()
