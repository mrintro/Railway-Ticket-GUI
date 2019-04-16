from tkinter import *
import pandas as pd
import ctypes
import datetime

def booked(a,b,c,d,e,root) :
    root.destroy()
    root = Tk()
    root.geometry('500x500')
    root.title("Final")
    print(e)
    print(e[14])
    k=e[14:16]
    m=e[26:]
    label_1 = Label(root, text="Final Details",fg = 'Red', width=25,font=("bold", 20)).place(x=60,y=50)
    f = Frame(root, height = 10, width = 500, bg = "black").place(x=0,y=85)
    username = Label(root, text="Name",width=20,font=("bold", 10)).place(x = 70, y = 130)
    nameinfo = Label(root, text= a,width=20,font=("bold", 10)).place(x = 240, y = 130)
    useremail = Label(root, text="E-mail",width=20,font=("bold", 10)).place(x=70,y=160)
    emailinfo = Label(root, text = b ,width=20,font=("bold", 10)).place(x=240,y=160)
    userAge = Label(root, text="Age",width=20,font=("bold", 10)).place(x=70,y=190)
    Ageinfo = Label(root, text = c ,width=20,font=("bold", 10)).place(x=240,y=190)
    usersex = Label(root, text = "Sex", width = 20, font = ("bold", 10)).place(x = 70, y = 220)
    sexinfo = Label(root, text = d , width = 20, font = ("bold", 10)).place(x = 240, y = 220)
    train_no = Label(root, text = "Train No", width = 20, font = ("bold", 10)).place(x = 70, y = 250)
    train_info = Label(root, text = k , width = 20, font = ("bold", 10)).place(x = 240, y = 250)
    train_time = Label(root, text = "Train Time", width = 20, font = ("bold", 10)).place(x = 70, y = 280)
    time_info = Label(root, text = m , width = 20, font = ("bold", 10)).place(x = 240, y = 280)

    f = Frame(root, height = 10, width = 500, bg = "black").place(x=0,y=350)
    label_1 = Label(root, text="Happy Journey",fg = 'Blue', width=22,font=("bold", 28)).place(x=10,y=370)


    root.mainloop()



def inputdetails(tr,root) :
    root.destroy()
    root = Tk()
    root.geometry('500x500')
    root.title("Input")
    label_1 = Label(root, text="Enter Details",fg = 'Red', width=25,font=("bold", 20)).place(x=60,y=50)
    f = Frame(root, height = 10, width = 500, bg = "black").place(x=0,y=85)
    username = Label(root, text="Name",width=20,font=("bold", 10))
    username.place(x=70,y=130)
    entryusername = Entry(root)
    entryusername.place(x=240,y=130)
    useremail = Label(root, text="E-mail",width=20,font=("bold", 10))
    useremail.place(x=70,y=160)
    entryusermail = Entry(root)
    entryusermail.place(x=240,y=160)

    userAge = Label(root, text="Age",width=20,font=("bold", 10))
    userAge.place(x=70,y=190)
    entryuserAge = Entry(root)
    entryuserAge.place(x=240,y=190)
      
    usersex = Label(root, text = "Sex", width = 20, font = ("bold", 10)).place(x = 70, y = 220)
    list=['Male','Female']
    r=StringVar(root)
    droplist=OptionMenu(root,r,*list)
    droplist.config(width = 15)
    r.set("Sex")
    droplist.place(x = 240,y = 220)
    Button(root, text='Submit',width=18,bg='brown',fg='white',command=lambda:booked(entryusername.get(),entryusermail.get(),entryuserAge.get(),r.get(),tr,root)).place(x=200,y=300)
    root.mainloop()
      




def getdata(s,d,e,root):
    data=pd.read_csv('trains.csv')
    data.head()
    if s==d:
        ctypes.windll.user32.MessageBoxW(0,'invalid source and destination','alert',1)
        return
    X=data['source'].values
    Y=data['destination'].values
    Z=data['train number'].values
    K=data['time'].values
    n=len(X)
    j=0
    L=[]
    for i in range(n):
        s1=str(X[i])
        s2=str(Y[i])
        s3=str(Z[i])
        s4=str(K[i])
        if(s==s1 and d==s2):
                L.append("train number : "+s3+"    time : "+s4)
                j+=1

    if j==0:
        ctypes.windll.user32.MessageBoxW(0,'No trains run into this route','alert',1)
    else:
        tr=StringVar(root)
        droplist=OptionMenu(root,tr,*L)
        droplist.config(width = 28)
        tr.set("Available Trains")
        droplist.place(x = 150,y = 400)
        Button(root, text='PROCEED',width=18,bg='brown',fg='white',command = lambda: inputdetails(tr.get(),root)).place(x=180,y=450)
    return

def select():
    root=Tk()
    root.geometry('500x500')
    root.title("Train booking")

    label_1 = Label(root, text="Welcome to e-Ticketing System",fg = 'Red', width=25,font=("bold", 20)).place(x=60,y=50)
    f = Frame(root, height = 10, width = 500, bg = "black").place(x = 0, y = 80)
    label_2 = Label(root,text = "From", width=20, font=("bold",12)).place(x = 20,y =150)
    label_3 = Label(root,text = "To", width=20, font=("bold",12)).place(x = 280,y =150)
    label_4 = Label(root,text = "Date of Travelling", width=20, font=("bold",12)).place(x = 160,y =270)
    list_1 = ['Kurukshetra','Haridwar','Saharanpur','Dehradun']
    list_2 = ['Chandigarh','Delhi','Aligarh','Roorkee','Ambala','Lucknow','Kurukshetra']

    today = datetime.date.today()
    today1 = today + datetime.timedelta(1)
    today2 = today + datetime.timedelta(2)
    today3 = today + datetime.timedelta(3)

    list_3 = [today,today1,today2,today3]

    c = StringVar(root)
    d = StringVar(root)
    e = StringVar(root)
    droplist = OptionMenu(root,c, *list_1)
    droplist.config(width = 15)
    c.set("Choose Source")
    droplist.place(x = 50, y =170)
    droplist = OptionMenu(root,d, *list_2)
    droplist.config(width = 15)
    d.set("Choose Destination")
    droplist.place(x = 300, y =170)
    droplist = OptionMenu(root,e, *list_3)
    droplist.config(width = 15)
    e.set("Choose Date")
    droplist.place(x = 180, y =297)
    Button(root, text='Find Trains',width=18,bg='brown',fg='white',command = lambda: getdata(c.get(),d.get(),e.get(),root)).place(x=180,y=360)
    root.mainloop()


def logincheck(s1,s2,root):
    data=pd.read_csv("database.csv")
    data.head()
    X=data['LOG IN'].values
    Y=data['PASSWORD'].values
    n=len(X)
    for i in range(n):
        s3=str(X[i])
        s4=str(Y[i])
        if(s1==s3 and s2==s4):
            root.destroy()
            select()
            return
    ctypes.windll.user32.MessageBoxW(0,'Invalid username or password','Error',1)
    return



def login():
	root = Tk()
	root.geometry('500x500')
	root.title("Login")
	
	textlogin = Label(root, text="Railway Ticket Booking",fg = 'Red', width=20,font=("bold", 20)).place(x=100,y=53)
	userID = Label(root, text="User ID",width=20,font=("bold", 10)).place(x=80,y=130)

	entryuserID = Entry(root)
	entryuserID.place(x=240,y=130)

	password = Label(root, text="Password",width=20,font=("bold", 10)).place(x=68,y=180)

	entrypassword = Entry(root,show='*')
	entrypassword.place(x=240,y=180)
	button=Button(root, text='Submit',width=20,bg='brown',fg='white',command = lambda: logincheck(entryuserID.get(),entrypassword.get(),root)).place(x=180,y=250)
	root.mainloop()


login()
