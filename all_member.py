from tkinter import *
from tkinter import ttk
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
    get_data = img_open.getdata()
    newdata = []
    for temp in get_data:
        newdata.append((temp[0], temp[1], temp[2], 190))
    img_open.putdata(newdata)
    return img_open
#==================================================
obj=Tk()
obj.title("Gym Registeration")
obj.geometry("700x600+300+40")
obj.resizable(False,False)
bg_image = image_background("gym5.jpeg")
bg_image_re=bg_image.resize((700,600))
bg_image_tk = ImageTk.PhotoImage(bg_image_re)
bg_label = Label(image=bg_image_tk, bg="#06283D")
bg_label.place(relwidth=1, relheight=1)
#================================================= 

#================================================= 
def search(id_val):
    if not id_val:  
        messagebox.showwarning("Input Error", "Please enter an ID to search.")
        return
    
    
    for row in tree.get_children():
        tree.delete(row)

    try:
        
        con = sqlite3.connect("Member_data.db")
        pen = con.cursor()
        
        pen.execute("SELECT * FROM member WHERE ID = ?", (id_val,))
        res = pen.fetchall()

        if not res:
            messagebox.showinfo("No Results", "No member found with that ID.")
        else:
            for row in res:
                tree.insert("", "end", values=row)

        con.commit()
        con.close()

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
        return
def delete_member():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("No selection", "Please select a member to delete.")
        return

    member_id = tree.item(selected_item)["values"][0]  

    
    confirm = messagebox.askyesno("Delete Member", "Are you sure you want to delete this member?")
    if confirm:
        
        con = sqlite3.connect("Member_data.db")
        pen = con.cursor()
        pen.execute("DELETE FROM member WHERE ID = ?", (member_id,))
        con.commit()
        con.close()

        
        tree.delete(selected_item)
        messagebox.showinfo("Delete Successful", "Member has been deleted successfully.")
def Back():
    obj.destroy()
    subprocess.run(["python", "main_page.py"])
def create_db():
    con = sqlite3.connect("Member_data.db") 
    pen = con.cursor() 
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
#================================================= 
l1=Label(
    text="All Member",
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
#===================================================
large_font = font.Font(size=20)
search_image=Image.open("search_icon.png") #open the photo
image_resizable=search_image.resize((20,20))#specifi width and height for photo
convert_image=ImageTk.PhotoImage(image_resizable)#convert photo to tkinter
search_all_member_g=StringVar()
search_all_member=Entry(width=25,font=large_font,textvariable=search_all_member_g).place(x=88,y=75)
search_button=Button(
    text="Search",
    font="bold",
    width=100,
    height=30,
    image=convert_image,#add photo
    compound=LEFT,#put photo at the left
    command=lambda: search(search_all_member_g.get())
).place(x=480,y=75)
#===================================================

go=Button(text="Back",width=10,height=2,font="arial 12 italic bold",command=Back,bg="#06283D",fg="white").place(x=0,y=550)
delete_button = Button(width=12,height=2,text="Delete Member",font="arial 12 italic bold", command=delete_member, bg="#06283D", fg="white")
delete_button.place(x=280, y=450)
Ex=Button(text="Exit",width=7,height=1,font="arial 12 bold italic",bg="#c21d36",fg="white",command=ex).place(x=617,y=560)
#====================================================
def show_data():
    create_db()
    # مسح البيانات القديمة في Treeview
    for row in tree.get_children():
        tree.delete(row)

    
    con = sqlite3.connect("Member_data.db")
    pen = con.cursor()
    pen.execute("SELECT * FROM member")
    rows = pen.fetchall()
    con.close()

    
    for row in rows:
        tree.insert("", "end", values=row)


tree = ttk.Treeview(columns=("ID" , "Date", "Name", "Age", "Phone", "Gender", "Height", "Weight", "System","Point"), show="headings")
tree.place(x=0, y=147, width=700, height=300)

# تعريف الأعمدة
tree.heading("ID", text="ID")
tree.heading("Date", text="Date")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Phone", text="Phone")
tree.heading("Gender", text="Gender")
tree.heading("Height", text="Height")
tree.heading("Weight", text="Weight")
tree.heading("System", text="System")
tree.heading("Point", text="Point")
#========================================
tree.column("ID", width=30, anchor="center")
tree.column("Date", width=60, anchor="center")
tree.column("Name", width=170, anchor="center")
tree.column("Age", width=30, anchor="center")
tree.column("Phone", width=90, anchor="center")
tree.column("Gender", width=60, anchor="center")
tree.column("Height", width=60, anchor="center")
tree.column("Weight", width=60, anchor="center")
tree.column("System", width=70, anchor="center")
tree.column("Point", width=30, anchor="center")

show_data()
Show_all=Button(
    text="Show all",
    font="bold",
    width=8,
    height=2,
    compound=LEFT,#put photo at the left
    command=show_data,
).place(x=590,y=450)
obj.mainloop()
#=============================================


