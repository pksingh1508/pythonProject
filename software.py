from tkinter import *
import mysql.connector as msl
from PIL import Image, ImageTk
from gtts import gTTS
import os
from playsound import playsound


root = Tk()

image = Image.open(r"C:\Users\hp\Downloads\bg1.jpg")
image = image.resize((900, 600))
photo = ImageTk.PhotoImage(image)
lbl = Label(root, image=photo)
lbl.place(x=0, y=0)

# functions
def submit():
    name = n_entry.get()
    roll = r_entry.get()
    age = a_entry.get()
    mob = m_entry.get()
    print(name, roll, age, mob)

    conn = msl.connect(host='localhost', user='root', password='pawan@860122', database='kipm')
    print("connected successfully")
    cur = conn.cursor()
    cur.execute("insert into user_details values(%s, %s, %s, %s)",(name, roll, age, mob))
    conn.commit()
    

def view_details():

    conn = msl.connect(host='localhost', user='root', password='pawan@860122', database='kipm')
    print("connected successfully")
    cur = conn.cursor()
    cur.execute("select * from user_details")
    result = cur.fetchall()

    lbx = Listbox(root, width=30, height=20, font="Helvetica 16 bold", bg="grey", fg="white")
    lbx.place(x=90, y=370)

    for i in result:
        lbx.insert(END, str(i))
         
    

def rstbtn():
    n_entry.delete(0, END)
    r_entry.delete(0, END)
    a_entry.delete(0, END)
    m_entry.delete(0, END)

def n_removePlaceholder(event):
    n_entry.delete(0, END)

def r_removePlaceholder(event):
    r_entry.delete(0, END)

def a_removePlaceholder(event):
    a_entry.delete(0, END)

def m_removePlaceholder(event):
    m_entry.delete(0, END)





# ---------CODE FOR CALCULATOR---------------------
def cal_click():
    window = Tk()

    def u1_removePlaceholder(event):
        user1_entry.delete(0, END)

    def u2_removePlaceholder(event):
        user2_entry.delete(0, END)
    
    def add():
        firstnum = user1_entry.get()
        secondnum = user2_entry.get()
        result = int(firstnum) + int(secondnum)
        #Label(window, text=result, bg="grey",font="Roboto 20 bold").place(x=250, y=220)
        myentry.insert(0,result)
        data = [f"{firstnum} + {secondnum} = {result}"]

        conn = msl.connect(host='localhost', user='root', password='pawan@860122', database='kipm')
        print("connected successfully")
        cur = conn.cursor()
        cur.execute("insert into calculation values(%s)",(data))
        conn.commit()
        
    
    def sub():
        firstnum = user1_entry.get()
        secondnum = user2_entry.get()
        result = int(firstnum) - int(secondnum)
        #Label(window, text=result, bg="grey",font="Roboto 20 bold").place(x=250, y=220)
        myentry.insert(0,result)

        data = [f"{firstnum} - {secondnum} = {result}"]

        conn = msl.connect(host='localhost', user='root', password='pawan@860122', database='kipm')
        print("connected successfully")
        cur = conn.cursor()
        cur.execute("insert into calculation values(%s)",(data))
        conn.commit()
        

    def mul():
        firstnum = user1_entry.get()
        secondnum = user2_entry.get()
        result = int(firstnum) * int(secondnum)
        #Label(window, text=result, bg="grey",font="Roboto 20 bold").place(x=250, y=220)
        myentry.insert(0,result)

        data = [f"{firstnum} * {secondnum} = {result}"]

        conn = msl.connect(host='localhost', user='root', password='pawan@860122', database='kipm')
        print("connected successfully")
        cur = conn.cursor()
        cur.execute("insert into calculation values(%s)",(data))
        conn.commit()
        
        

    def div():
        firstnum = user1_entry.get()
        secondnum = user2_entry.get()
        result = int(int(firstnum) / int(secondnum))
        #Label(window, text=result, bg="grey",font="Roboto 20 bold").place(x=250, y=220)
        myentry.insert(0,result)

        data = [f"{firstnum} / {secondnum} = {result}"]

        conn = msl.connect(host='localhost', user='root', password='pawan@860122', database='kipm')
        print("connected successfully")
        cur = conn.cursor()
        cur.execute("insert into calculation values(%s)",(data))
        conn.commit()
        
    def click():
        myentry.insert(0,"                                                                    ")


    window.title("Calculator")
    window.geometry("400x400")
    window.resizable(0,0)
    window.configure(bg="grey")
    Label(window, text="Welcome to Calculator", font="Algerian 20 bold", bg="grey").place(x=20, y=10)

    user1_entry = Entry(window, font="Helvetica 15 bold", relief=SUNKEN, borderwidth=5)
    user1_entry.bind('<Button-1>', u1_removePlaceholder)
    user1_entry.insert(0, "Enter first value...")
    user1_entry.place(x=100, y=60)

    user2_entry = Entry(window, font="Helvetica 15 bold", relief=SUNKEN, borderwidth=5)
    user2_entry.bind('<Button-1>', u2_removePlaceholder)
    user2_entry.insert(0, "Enter second value...")
    user2_entry.place(x=100, y=100)

    Button(window, text="  +  ", font="Helvetica 12 bold", bg="red", fg="black", command=add).place(x=120, y=150)
    Button(window, text="  -  ", font="Helvetica 12 bold", bg="red", fg="black", command=sub).place(x=180, y=150)
    Button(window, text="  *  ", font="Helvetica 12 bold", bg="red", fg="black", command=mul).place(x=230, y=150)
    Button(window, text="  /  ", font="Helvetica 12 bold", bg="red", fg="black", command=div).place(x=280, y=150)
    
    Label(window, text="Result :- ", font="Algerian 20 bold", bg="grey").place(x=20, y=220)
    ans = StringVar()
    ans.set("12")
    myentry = Entry(window, textvariable=ans, font="Helvetica 12 bold", borderwidth=5, relief=SUNKEN)
    myentry.place(x=170, y=227)

    cbtn = Button(window, text="Clear",font="Helvetica 20 bold", bg="orange", fg="black",command=click)
    cbtn.place(x=180, y=280)

    window.mainloop()
    



# --------------CODE FOR NOTE PAD ----------------------
def note_click():
    nroot = Tk()


    def save():
        value = text.get()
        with open("record.txt","a") as f:
            f.write(f"{value}"+"\n")
        
        value = [value]
        print(value)
        conn = msl.connect(host='localhost', user='root', password='pawan@860122', database='kipm')
        print("connected successfully")
        cur = conn.cursor()
        cur.execute("insert into notes values(%s)",(value))
        conn.commit()


        
    def view():

        conn = msl.connect(host='localhost', user='root', password='pawan@860122', database='kipm')
        print("connected successfully")
        cur = conn.cursor()
        cur.execute("select * from notes")
        result = cur.fetchall()

        lbx = Listbox(nroot, width=50, height=20, font="Helvetica 16 bold", bg="grey", fg="white")
        lbx.place(x=90, y=300)

        for i in result:
            lbx.insert(END, str(i))

        
    nroot.title("Note Taking Application")
    nroot.resizable(0,0)
    nroot.geometry("900x600")
    nroot.config(bg="grey")
    Label(nroot, text="Welcome to NotePad", font="Algerian 20 bold", bg="grey").pack(pady=10)
    
    
    text = Entry(nroot, width=800, font="Helvetica 20 bold", fg="black")
    text.pack(padx=20)

    Button(nroot, text="Save", font="Algerian 19 bold", bg="orange", fg="black", command=save).pack(pady=10)

    Button(nroot, text="View Notes", font="Algerian 19 bold", bg="orange", fg="black", command=view).pack(pady=10)



    nroot.mainloop()
    pass







# ---------------CODE FOR Robot ---------------------------
def play_game():

    main = Tk()
    main.geometry("400x300")
    main.title("Speaking Robot")
    main.configure(bg="grey")

    def generate():
        text = my_text.get()
        language = 'en'

        my_obj = gTTS(text=text, lang=language, slow=False)
        my_obj.save("speech.mp3")
        os.system("mpg321 audio.mp3")

    def play():
        playsound("speech.mp3")
        
        

    my_text = Entry(main, width=300, font="Helvetica 20 bold")
    my_text.pack(padx=20, pady=30)

    my_btn = Button(main, text="Convert", font="Algerian 19 bold", bg="red", fg="black", command=generate)
    my_btn.pack()

    Button(main, text="Play Sound", font="Algerian 19 bold", bg="red", fg="black", command=play).pack(pady=10)


    main.mainloop()    
    pass


# ---------------MAIN PROGRAM-----------------
root.title("User Data Application")
root.iconbitmap(r"C:\Users\hp\Downloads\myicon.ico")
root.geometry("600x600")
root.resizable(0,0)


Label(text="User Detail Page", font="Algerian 30 bold", bg="black", fg="white").place(x=130, y=5)

# Entry field
n_entry = Entry(root, borderwidth=5, relief=SUNKEN, font="Helvetica 13 bold")
n_entry.insert(0, "Enter your name")
n_entry.bind('<Button-1>', n_removePlaceholder)
n_entry.place(x=25, y=60)

r_entry = Entry(root, borderwidth=5, relief=SUNKEN, font="Helvetica 13 bold")
r_entry.insert(0, "Enter your roll")
r_entry.bind('<Button-1>', r_removePlaceholder)
r_entry.place(x=25, y=110)

a_entry = Entry(root, borderwidth=5, relief=SUNKEN, font="Helvetica 13 bold")
a_entry.insert(0, "Enter your age")
a_entry.bind('<Button-1>', a_removePlaceholder)
a_entry.place(x=25, y=160)

m_entry = Entry(root, borderwidth=5, relief=SUNKEN, font="Helvetica 13 bold")
m_entry.insert(0, "Enter your mobile no")
m_entry.bind('<Button-1>', m_removePlaceholder)
m_entry.place(x=25, y=210)

# button 
s_btn = Button(root, text="   Submit   ", font="Roboto 10 bold", relief=RAISED, borderwidth=5, bg="green", fg="black", command=submit)
s_btn.place(x=400, y=60)

vd_btn = Button(root, text=" View Detail", font="Roboto 10 bold", relief=RAISED, borderwidth=5, bg="blue", command=view_details)
vd_btn.place(x=400, y=110)

r_btn = Button(root, text="    Reset   ", font="Roboto 10 bold", relief=RAISED, borderwidth=5, bg="orange", command=rstbtn)
r_btn.place(x=400, y=160)

e_btn = Button(root, text="    Exit    ", font="Roboto 12 bold", relief=RAISED, borderwidth=5, bg="red", fg="black", command=quit)
e_btn.place(x=400, y=210)


# extra three button
c_button = Button(root, text="Calculator", font="Roboto 12 bold", relief=RAISED, borderwidth=5, bg="red", fg="black", command=cal_click)
c_button.place(x=25, y=300)

n_button = Button(root, text="NotePad", font="Roboto 12 bold", relief=RAISED, borderwidth=5, bg="red", fg="black", command=note_click)
n_button.place(x=225, y=300)

g_button = Button(root, text="Robot", font="Roboto 12 bold", relief=RAISED, borderwidth=5, bg="red", fg="black", command=play_game)
g_button.place(x=425, y=300)


root.mainloop()
