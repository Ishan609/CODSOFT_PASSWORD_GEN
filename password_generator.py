#!/usr/bin/env python
# coding: utf-8

# In[5]:


import string
import random
from tkinter import *
from tkinter import messagebox


# In[6]:


win=Tk()
#width and height of the window
win.geometry("600x400")
win.configure(bg="grey")




def pasw_genration():
    #storing all characters to create samples of passwords
    a1=string.ascii_lowercase #[a-b]
    a2=string.ascii_uppercase #[A-B]
    a3=string.digits #[0-9]
    a4=string.punctuation #[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.]#taking input from the user for his/her password length


    b=int(e2.get())

    #creating an empty list for storing characters
    lis=[] 
    #converting string into a list by breaking a string into characters 
    lis.extend(a1)
    lis.extend(a2)
    lis.extend(a3)
    lis.extend(a4)

    #It will generate random characters in list 
    pasw = random.sample(lis,b)


    #converting list into string 
    pasw="".join(pasw)
    #for printing as label
    #l3=Label(win,text=("GENERATED PASSWORD IS : ",pasw),font=("arial",15,"bold"))
    #l3.place(relx=0.2,rely=0.6)
    
    #printing as message box
    '''messagebox.showinfo("PASW GENERATION",("GENERATED PASSWORD IS",pasw))'''
    l2=Label(win,text=f"PASSWORD GENERATED : {pasw}",font=("arial",20,"bold"),bg="grey",fg="white")
    l2.place(relx=0.4,rely=0.6)
    e1.delete(0,"end")
    e2.delete(0,"end")
    



# In[7]:


#creating and placing labels and entry fields
l=Label(win,text="PASSWORD GENERATION",width=25,font=("ink free",40,"bold"),fg="blue")
l.pack(side="top",anchor="c")
l1=Label(win,text="Enter user name",font=("arial",20),bg="yellow")
l1.place(relx=0.3,rely=0.2)
e1=Entry(win,font=("arial",15),bd=8)
e1.place(relx=0.5,rely=0.2)

l2=Label(win,text="Length for pasw",font=("arial",20),bg="yellow")
l2.place(relx=0.3,rely=0.4)
e2=Entry(win,font=("arial",15),bd=8)
e2.place(relx=0.5,rely=0.4)

#creating and placing button
b1 = Button(win,text= "GENERATE PASSWORD",width=20,font=("arial",18,"bold"),bg="red",fg='black',command=pasw_genration)
b1.place(relx=0.40,rely=0.7)
win.mainloop()


# In[ ]:




