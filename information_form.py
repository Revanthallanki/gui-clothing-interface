from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox

root=Tk()
root.geometry("850x650")
root.title("Bank Information Form")
root.config(bg="honeydew2")
Label(root,text="Bank Management System",font=("bold",17),background="honeydew2").place(x=290,y=20)
c=Canvas(root,height=170,width=810,bg="black")
c.place(x=20,y=400)
rect=c.create_rectangle(3,170,810,3,fill="honeydew2")

account_var=StringVar()
ifsc_var=StringVar()
name_var=StringVar()
number_var=StringVar()
add_var=StringVar()
date_var=StringVar()
type_var=StringVar()
state_var=StringVar()
dist_var=StringVar()
pin_var=StringVar()
pan_var=StringVar()
occupation_var=StringVar()


def preview():

    wait.destroy()
    global acc,ifsc,name,number,address,type,state,dist,pin,pan,occ
    acc=account_var.get()
    ifsc=ifsc_var.get()
    name=name_var.get()
    number=number_var.get()
    address=add_var.get()
    type=type_var.get()
    state=state_var.get()
    dist=dist_var.get()
    pin=pin_var.get()
    pan=pan_var.get()
    occ=occupation_var.get()


    Label(root, text="Account holder name  :", font=("calibre", 10), background="honeydew2").place(x=30, y=420)
    Label(root, text="Account number         :", font=("calibre", 10), background="honeydew2").place(x=30, y=440)
    Label(root, text="IFSC code                 :", font=("calibre", 10), background="honeydew2").place(x=30, y=460)
    Label(root, text="Mobile number           :", font=("calibre", 10), background="honeydew2").place(x=30, y=480)
    Label(root, text="Email address            :", font=("calibre", 10), background="honeydew2").place(x=30, y=500)
    Label(root, text="Account type             :", font=("calibre", 10), background="honeydew2").place(x=30, y=520)
    Label(root, text="State           :", font=("calibre", 10), background="honeydew2").place(x=450, y=420)
    Label(root, text="District        :", font=("calibre", 10), background="honeydew2").place(x=450, y=440)
    Label(root, text="Pincode       :", font=("calibre", 10), background="honeydew2").place(x=450, y=460)
    Label(root, text="PAN            :", font=("calibre", 10), background="honeydew2").place(x=450, y=480)
    Label(root, text="Occupation  :", font=("calibre", 10), background="honeydew2").place(x=450, y=500)

    global lab1,lab2,lab3,lab4,lab5,lab6,lab7,lab8,lab9,lab10,lab11

    lab1=Label(root, text=acc,background="honeydew2")
    lab1.place(x=220,y=420)
    lab2=Label(root, text=ifsc,background="honeydew2")
    lab2.place(x=220, y=440)
    lab3=Label(root, text=name,background="honeydew2")
    lab3.place(x=220, y=460)
    lab4=Label(root, text=number,background="honeydew2")
    lab4.place(x=220, y=480)
    lab5=Label(root, text=address,background="honeydew2")
    lab5.place(x=220, y=500)
    lab6=Label(root, text=type,background="honeydew2")
    lab6.place(x=220, y=520)
    lab7=Label(root, text=state,background="honeydew2")
    lab7.place(x=640, y=420)
    lab8=Label(root, text=dist,background="honeydew2")
    lab8.place(x=640, y=440)
    lab9=Label(root, text=pin,background="honeydew2")
    lab9.place(x=640, y=460)
    lab10=Label(root, text=pan,background="honeydew2")
    lab10.place(x=640, y=480)
    lab11=Label(root, text=occ,background="honeydew2")
    lab11.place(x=640, y=500)

    Button(root, text="Reset", width=10, bg="black", foreground="white", font=("calibre", 12),command=reset).place(x=300, y=330, height=20)


def reset():

    account_var.set("")
    ifsc_var .set("")
    name_var.set("")
    number_var.set("")
    add_var.set("")
    date_var.set("")
    type_var.set("")
    state_var.set("")
    dist_var.set("")
    pin_var.set("")
    pan_var.set("")
    occupation_var.set("")

    lab1.destroy()
    lab2.destroy()
    lab3.destroy()
    lab4.destroy()
    lab5.destroy()
    lab6.destroy()
    lab7.destroy()
    lab8.destroy()
    lab9.destroy()
    lab10.destroy()
    lab11.destroy()

def submit():

    k=0

    if len(account_var.get())==0:
        messagebox.showerror("error","enter the account number")
        k=k+1
    elif account_var.get().isalpha():
        messagebox.showerror("error","Enter the proper account number \nAccount number must be in digits")
        k = k + 1

    elif len(ifsc_var.get())==0:
        messagebox.showerror("error","enter the IFSC")
        k=k+1
    elif ifsc_var.get().islower():
        messagebox.showerror("error","Enter the proper IFSC code \nIFSC must be in uppercase")
        k = k + 1

    elif len(name_var.get())==0:
        messagebox.showerror("error","enter the name of the account holder")
        k = k + 1
    elif name_var.get().isdigit():
        messagebox.showerror("error","Enter the proper account holder name \nName must be in alphabet")
        k = k + 1

    elif len(number_var.get())==0:
        messagebox.showerror("error","enter the number")
        k = k + 1
    elif number_var.get().isalpha():
        messagebox.showerror("error","Enter the proper Mobile number \nMobile number must be in digits")
        k = k + 1

    elif len(add_var.get())==0:
        messagebox.showerror("error","enter the address")
        k = k + 1

    elif len(type_var.get())==0:
        messagebox.showerror("error","enter the type of the account \nSAVINGS or CURRENT")
        k = k + 1
    elif type_var.get().isdigit():
        messagebox.showerror("error","Enter the proper account type \nAccount type must be in alphabet")
        k = k + 1

    elif len(state_var.get())==0:
        messagebox.showerror("error","enter the state")
        k = k + 1
    elif state_var.get().isdigit():
        messagebox.showerror("error","Enter the proper state \nstate must be in alphabet")
        k = k + 1

    elif len(dist_var.get())==0:
        messagebox.showerror("error","enter the  district")
        k = k + 1
    elif dist_var.get().isdigit():
        messagebox.showerror("error","Enter the proper district \ndistrict must be in alphabet")
        k = k + 1

    elif len(pin_var.get())==0:
        messagebox.showerror("error","enter the pincode")
        k = k + 1
    elif pin_var.get().isalpha():
        messagebox.showerror("error","Enter the proper pincode \nPincode must be in digits")
        k = k + 1

    elif len(pan_var.get())==0:
        messagebox.showerror("error","enter the PAN")
        k = k + 1

    elif len(occupation_var.get())==0:
        messagebox.showerror("error","enter the Occupation")
        k=k+1
    elif occupation_var.get().isdigit():
        messagebox.showerror("error","Enter the proper occupation \nOccupation must be in alphabet")
        k=k+1


    if k==0:
        messagebox.showinfo("confirmation","Your application successfullly submited")

Label(root,text="Enter account number  :",font=("calibre",10),background="honeydew2").place(x=30,y=60)
Label(root,text="Enter IFSC code          :",font=("calibre",10),background="honeydew2").place(x=30,y=100)
Label(root,text="Account holder name   :",font=("calibre",10),background="honeydew2").place(x=30,y=140)
Label(root,text="Enter Mobile number    :",font=("calibre",10),background="honeydew2").place(x=30,y=180)
Label(root,text="Enter email address     :",font=("calibre",10),background="honeydew2").place(x=30,y=220)
Label(root,text="Enter the date             :",font=("calibre",10),background="honeydew2").place(x=30,y=260)
Label(root,text="Enter Account type     :",font=("calibre",10),background="honeydew2").place(x=450,y=60)
Label(root,text="Enter the state           :",font=("calibre",10),background="honeydew2").place(x=450,y=100)
Label(root,text="Enter the district         :",font=("calibre",10),background="honeydew2").place(x=450,y=140)
Label(root,text="Enter the pincode       :",font=("calibre",10),background="honeydew2").place(x=450,y=180)
Label(root,text="Enter PAN number      :",font=("calibre",10),background="honeydew2").place(x=450,y=220)
Label(root,text="Enter Occupation        :",font=("calibre",10),background="honeydew2").place(x=450,y=260)


ent1=Entry(root,width=30,textvariable=account_var).place(x=220,y=60)
ent2=Entry(root,width=30,textvariable=ifsc_var).place(x=220,y=100)
ent3=Entry(root,width=30,textvariable=name_var).place(x=220,y=140)
ent4=Entry(root,width=30,textvariable=number_var).place(x=220,y=180)
ent5=Entry(root,width=30,textvariable=add_var).place(x=220,y=220)
ent6=DateEntry(root).place(x=220,y=260)
ent7=Entry(root,width=30,textvariable=type_var).place(x=640,y=60)
ent8=Entry(root,width=30,textvariable=state_var).place(x=640,y=100)
ent9=Entry(root,width=30,textvariable=dist_var).place(x=640,y=140)
ent10=Entry(root,width=30,textvariable=pin_var).place(x=640,y=180)
ent11=Entry(root,width=30,textvariable=pan_var).place(x=640,y=220)
ent12=Entry(root,width=30,textvariable=occupation_var).place(x=640,y=260)



wait=Label(root,text="Waiting for account holder information.....",font=("calibre",15),background="honeydew")
wait.place(x=200,y=470)
button1=Button(root,text="Reset",width=10,bg="black",foreground="white",font=("calibre",12),command=reset).place(x=300,y=330,height=20)
button2=Button(root,text="Preview",width=10,bg="black",foreground="white",font=("calibre",12),command=preview).place(x=430,y=330,height=20)
button3=Button(root,text="Submit",width=10,bg="black",foreground="white",font=("calibre",12),command=submit).place(x=350,y=590,height=20)

root.mainloop()
