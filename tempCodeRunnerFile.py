from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import subprocess
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

    get_data = img_open.getdata()
    newdata = []
    for temp in get_data:
        newdata.append((temp[0], temp[1], temp[2], 190))
    img_open.putdata(newdata)
    return img_open
#==================================================
def check():
        password_window = Toplevel(obj)
        password_window.title("Check Password")
        password_window.geometry("300x150+480+230")
        password_window.configure(bg="#06283D")
        Label(password_window, text="Please enter your password:").pack(pady=10)
        password_entry = Entry(password_window, show="*", width=20)
        password_entry.pack(pady=10)
        def check_password():
            password = password_entry.get()
            correct_password = "mahmoud22"
            if password == correct_password:
                messagebox.showinfo("Success", "Password Correct!")
                password_window.destroy()
                obj.destroy()
                subprocess.run(["python", "all_member.py"])
            else:
                messagebox.showerror("Error", "Incorrect Password. Try Again.")
        submit_button = Button(password_window, text="Submit",font="arial 12 bold italic",bg="#06283D",fg="white", command=check_password)
        submit_button.pack(pady=20)
#==================================================
obj=Tk()
obj.title("Gym Registeration")
obj.geometry("700x600+300+40")
obj.configure(bg="#06283D")
obj.resizable(False,False)
bg_image = image_background("gym5.jpeg")
bg_image_re=bg_image.resize((700,600))
bg_image_tk = ImageTk.PhotoImage(bg_image_re)
bg_label = Label(image=bg_image_tk,bg="#06283D")
bg_label.place(relwidth=1, relheight=1)
#================================================= 
#================================================= 
def create():
    obj.destroy()
    subprocess.run(["python", "gym.py"])
def log_in():
    obj.destroy()
    subprocess.run(["python", "log_in.py"])
#================================================= 
l1=Label(
    text="Welcome",
    bg="#06283D",
    width=10,
    height=2,
    fg="white",
    font="arial 28 bold" 
).pack(side=TOP,fill=X)
l2=Label(
    text="In the gym, today's effort is tomorrow's victory!🏆💥",
    bg="#06283D",
    width=10,
    height=2,
    fg="white",
    font="arial 18 bold italic" 
).pack(side=BOTTOM,fill=X)
#==================================================
icon_img=Image.open("logo.jpg") #open the photo
image_resizable1=icon_img.resize((100,100))#specifi width and height for photo
convert_image1=ImageTk.PhotoImage(image_resizable1)#convert photo to tkinter
l_image=Label(width=100,height=91,image=convert_image1)
l_image.place(x=0,y=0)
#==================================================
Sign=Button(text="Sign Up",width=13,height=3,font="arial 12 bold italic",bg="#06283D",fg="white",command=create)
logn=Button(text="Log In",width=13,height=3,font="arial 12 bold italic",bg="#06283D",fg="white",command=log_in)
Show=Button(text="Show all member",width=13,height=3,font="arial 12 bold italic",bg="#06283D",fg="white",command=check).place(x=500,y=370)
Ex=Button(text="Exit",width=7,height=1,font="arial 12 bold italic",bg="#c21d36",fg="white",command=ex).place(x=617,y=500)
#==================================================
img1=Image.open("add.png")
resiz1=img1.resize((120,120))
convert1=ImageTk.PhotoImage(resiz1)
l_image1=Label(width=120,height=120,image=convert1)
img2=Image.open("login_1.png")
resiz2=img2.resize((120,120))
convert2=ImageTk.PhotoImage(resiz2)
l_image2=Label(width=120,height=120,image=convert2)
img3=Image.open("members.png")
resiz3=img3.resize((120,120))
convert3=ImageTk.PhotoImage(resiz3)
l_image3=Label(width=120,height=120,image=convert3)
#==================================================
Sign.place(x=100,y=370)
logn.place(x=300,y=370)

l_image1.place(x=105,y=220)
l_image2.place(x=305,y=220)
l_image3.place(x=505,y=220)
#==================================================
obj.mainloop()