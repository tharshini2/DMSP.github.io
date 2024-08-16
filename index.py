from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
import function
window = Tk()
window.title("Donation Management System")
window.configure(bg="gray")

def view_command():
    lb.delete(0,END)
    for row in function.viewall():
        lb.insert(END,row)

def search_command():
    lb.delete(0,END)
    for row in function.search(name=name.get(),user=user.get(),password=password.get(),category=category.get()):
        lb.insert(END,row)

def add_command():
    function.add(name.get(),user.get(),password.get(),category.get(),cdate.get())
    lb.delete(0,END)
    lb.insert(END,name.get(),user.get(),password.get(),category.get(),cdate.get())

def get_selected_row(event):
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass

def update_command():
    function.update(selected_tuple[0],name.get(),user.get(),password.get(),category.get(),cdate.get())
    view_command()

def delete_command():
    function.delete(selected_tuple[0])
    view_command()
   
def clear_command():
    lb.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)

l1 = Label(window,text="Name", fg="black")
l1.grid(row=0,column=0)
l2 = Label(window,text="company name/profession", fg="black")
l2.grid(row=1,column=0)
l3 = Label(window,text="purpose ", fg="black")
l3.grid(row=2,column=0)
l4 = Label(window,text="amount ", fg="black")
l4.grid(row=3,column=0)
l5 = Label(window,text="date", fg="black")
l5.grid(row=4,column=0)

name=StringVar()
e1 = Entry(window,textvariable=name,width=50)
e1.grid(row=0,column=0,columnspan=10)

user=StringVar()
e2 = Entry(window,textvariable=user,width=50)
e2.grid(row=1,column=0,columnspan=10)

password=StringVar()
e3 = Entry(window,textvariable=password,width=50)
e3.grid(row=2,column=0,columnspan=10)

category=StringVar()
e4 = Entry(window,textvariable=category,width=50)
e4.grid(row=3,column=0,columnspan=10)

cdate=StringVar()
e5 =DateEntry(window,selectmode='day',textvariable=cdate)
e5.grid(row=4,column=0,columnspan=10)

b1 = Button(window,text="Add",width=12,command=add_command)
b1.grid(row=5,column=0)

b2 = Button(window,text="Update",width=12,command=update_command)
b2.grid(row=5,column=1)

b3 = Button(window,text="Search",width=12,command=search_command)
b3.grid(row=5,column=2)

b4 = Button(window,text="View All",width=12,command=view_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=5,column=4)

b6 = Button(window,text="Cancel",width=12,command=window.destroy)
b6.grid(row=5,column=5)

b7 = Button(window,text="Clear All",bg="red",width=12,command=clear_command)
b7.grid(row=0,column=5)

lb=Listbox(window,height=20,width=94)
lb.grid(row=6,column=0,columnspan=6)

sb=Scrollbar(window)
sb.grid(row=6,column=6,rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop()
