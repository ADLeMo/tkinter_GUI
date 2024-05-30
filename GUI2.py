"""
    >>> def :: 
        1. sign up
        2. sign in 
        3. cancel
    >>> backgraund ::
    >>> def (menu) :: 
    >>> label :: 
        1. bachground 
        2. home page
    >>> buttom  ::
        1. sign up 
        2. sign in
        3.  cancel
        
    
    >>> place ::
        1.  bachground
        2.  home page
        3.  sign up
        4.  sign in
        5.  cancel
         
"""


from ast import If
from cProfile import label
from cgitb import text
from tkinter import * 
import tkinter as tk
import tkinter.font
import tkinter.messagebox
import tkinter.messagebox
import tkinter.messagebox
import tkinter.ttk
import tkinter.colorchooser
import tkinter.filedialog

information = {
    "email" : [],
    "username" : [],
    "pasword" : []
}



def sign_up():
    """         toplevel:: 
    
        >>> background ::
            1. labal for toplevel
            
            
        >>> label :: 
            1.  background
            2.  email note
            3.  username note
            4.  pasword note
            5.  email
            6.  username
            7.  pasword
            
        >>> entry ::
            1.  email
            2.  username
            3.  pasword
            
        >>> buttom ::
            1.  okey
            2.  cancel
        
    """
    def okey_buttom_top():
        if (buttom_cancel or buttom_okey)==False : 
            tkinter.messagebox.ERROR("you dont chose buttom")
        if (entry_email.get() or entry_pasword.get() or entry_username.get())==" " : 
            tkinter.messagebox.showerror("error EMPTY ..."
                ,"the entry is empty! , \npls try again!!")
            top.destroy()
        elif "@" not in entry_email.get() : 
            tkinter.messagebox.showwarning("warning ... "
                ,"your email dont have '@' ")
        elif len(entry_pasword.get())<8 : 
            tkinter.messagebox.showerror("error massage ...",
                "your pasword must have 8 charekter , \npls try again .")
            top.destroy()
        else:
            save_information = tkinter.messagebox.askyesno("Save Your Informations",
                "Do You Wnat Save Your Informations")
            if save_information==True :
                print("your list_buttom is : ",chose.get())
                print("====") 
                print(" user email is : {}".format(entry_email.get()))
                print("====")
                print("user username is : {}".format(entry_username.get()))
                print("====")
                print("user pasword is : {}".format(entry_pasword.get()))
                print("====")
                top.destroy() 
            else:
                tkinter.messagebox.showinfo("Back To Seit","PLS Try Again !")
                top.destroy()
        U_email = entry_email.get()
        U_username = entry_username.get()
        U_pasword = entry_pasword.get()
        if U_email in information["email"] : 
            massage = tkinter.messagebox.showerror("error","your EMAIL was in the seit !!\npls try again. ")
            # print(massage)
            if massage == "ok" : 
                top.destroy()
        else:
            if U_username in information["username"] : 
                massage = tkinter.messagebox.showerror("error","your USERNAME was in the seit !!\npls try again. ")
                if massage == "ok" : 
                     top.destroy()
            else:
                if U_pasword in information["pasword"] : 
                    massage = tkinter.messagebox.showerror("error","your PASWORD was in the seit !!\npls try again. ")
                    if massage == "ok" : 
                        top.destroy()
                else:
                    information["email"].append(U_email)
                    information["username"].append(U_username)
                    information["pasword"].append(U_pasword)
                    print("user information : \nemail = {} \nusername = {} \npasword = {}".format(U_email,U_username,U_pasword))
                        
                
            
                

    def cancel_buttom_top() :
        cansel_massagebox= tkinter.messagebox.askyesno("cansel",
            "Do You Wnat Exit This Seit ? ")
        if cansel_massagebox==True : 
            top.destroy() 
        
            
    
    top = Toplevel(window)
    top.geometry("600x600")
    top.resizable(width=False,height=False)
    top.title("sign up")
    top.configure(bg="#400040")
    
    # background_toplevel = tk.PhotoImage(file="D:\\work\\p\\rogram\\python\\GUI\\photos\\backraund2.png")
    # backgraund_toplevel_label = tk.Label(top,image=background_toplevel)
    def menu():
        menu = Menu(top)
        top.config(menu=menu)
        filemenu = Menu(menu,tearoff=0)
        menu.add_cascade(label='File', menu=filemenu)
        filemenu.add_command(label='New')
        filemenu.add_command(label='Open...')
        filemenu.add_command(label='Setting')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=top.quit)
        helpmenu = Menu(menu,tearoff=0)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About')
    menu()  
    
    
    label_optionmenu = tkinter.Label(top,
                           text=" Choose Your Birtday :  ",
                           bg= "#400040",fg="#ff8000",
                           font= ("times new roman",15,"bold"),
                           borderwidth=30,bd=2, 
                           )
    text_menu = tkinter.StringVar()
    text_menu.set("choose hier")   
    option_month = tkinter.OptionMenu(top,text_menu,"January","february", "march",
                "abril", "may", "june", "july","august","september","october","november","december")  
    
    option_month.config(bg="#ff0080")   
    option_month["menu"].config(bg="#8080ff")  
    
    number_list = []
    number_list2 = []
    for i in range(1,31):
        number_list.append(i)
    text_menu2 = tkinter.StringVar()
    text_menu2.set("choose hier")
    option_day = tkinter.OptionMenu(top,text_menu2,*number_list,)    
    option_day.config(bg="#ff0080",) 
    option_day["menu"].config(bg="#8080ff")
    
    for i in range(1989,2025):
        number_list2.append(i)
    text_menu3 = tkinter.StringVar()
    text_menu3.set("choose hier")
    option_year = tkinter.OptionMenu(top,text_menu3,*number_list2,)    
    option_year.config(bg="#ff0080",) 
    option_year["menu"].config(bg="#8080ff")
    
    
    label_email_note =   tk.Label(top,
                            text=" Pleas Inter Your E-Mail ",
                            bg= "#400040",fg="#ff8000",
                            font= ("times new roman",25,"bold"),
                            borderwidth=15,bd=3,width=20
                            )
    label_usernam_note = tk.Label(top,
                                text=" Pleas Inter Your Username ",
                                bg= "#400040",fg="#ff8000",
                                font= ("times new roman",25,"bold"),
                                borderwidth=15,bd=3,width=20
                                )
    label_pasword_note = tk.Label(top,
                                text=" Pleas Inter Your Pasword ",
                                bg= "#400040",fg="#ff8000",
                                font= ("times new roman",25,"bold"),
                                borderwidth=15,bd=3,width=20
                                )
    label_email =   tk.Label(top,
                            text="E-Mail : ",
                            fg="#00ffff",bg='#15181A',
                            font= ("NORMAL",12,"italic"),
                            bd=10,width=8
                            )
    label_username = tk.Label(top,
                            text="Username : ",
                            fg="#00ffff",bg='#15181A',
                            font= ("NORMAL",12,"italic"),
                            bd=10,width=8
                            )
    label_pasword = tk.Label(top,
                            text="Pasword : ",
                            fg="#00ffff",bg='#15181A',
                            font= ("NORMAL",12,"italic"),
                            bd=10,width=8
                            )
    entry_email =   tk.Entry(top,font=("names",10,"italic"),
                    bd=8,fg="#ffffff",bg="gray",
                    width=35,state="normal",highlightcolor="#8080ff",highlightthickness=3,
                    border=8,borderwidth=8,disabledbackground="#000000",
                        )
    entry_username = tk.Entry(top,font=("names",10,"italic"),
                    bd=8,fg="#ffffff",bg="gray",
                    width=35,state="normal",highlightcolor="#8080ff",highlightthickness=3,
                    border=8,borderwidth=8,disabledbackground="#000000",
                        )
    entry_pasword = tk.Entry(top,font=("names",10,"italic"),
                    bd=8,fg="#ffffff",bg="gray",
                    width=35,state="normal",highlightcolor="#8080ff",highlightthickness=3,
                    border=8,borderwidth=8,disabledbackground="#000000",
                        )
    buttom_okey = tk.Button(top,text ="Okey",
                            relief=FLAT,font=("times new roman",15,"bold"),
                            bd=10,fg="#15181A",bg="#ff8000"
                            ,width=15,height=0,borderwidth=6,
                            anchor="center",command=okey_buttom_top
                            )
    buttom_cancel = tk.Button(top,text ="Cancel",
                            relief=FLAT,font=("times new roman",15,"bold"),
                            bd=10,fg="#15181A",bg="#ff8000"
                            ,width=15,height=0,borderwidth=6,
                            anchor="center",command=cancel_buttom_top
                    )



    list_buttom = [ ("MAIL",  "number_1"),("FEMAIL","number_2")]
    chose = tkinter.StringVar()
    chose.set("a")
    x = 150
    for i,j in list_buttom : 
                buttom = tkinter.Radiobutton(top,
                            text="{}".format(i),
                            value=j,
                            bd=5 ,font=("times new roman",10,"bold"),
                            fg="#ff8000",
                            bg="#800000",
                            variable=chose
                            )
                buttom.place(x=x,y=450)
                x=x+240
    
    label_email_note.place(x=5,y=10)
    label_email.place(x=100,y=60)
    entry_email.place(x=250,y=60)

    label_usernam_note.place(x=30,y=120)
    label_username.place(x=100,y=170)
    entry_username.place(x=250,y=170)

    label_pasword_note.place(x=15,y=230)
    label_pasword.place(x=100,y=280)
    entry_pasword.place(x=250,y=280)

    label_optionmenu.place(x=15,y=350)
    option_year.place(x=230,y=350)
    option_month.place(x=350,y=350)
    option_day.place(x=480,y=350)


    buttom_cancel.place(x=15,y=500)
    buttom_okey.place(x=390,y=500)

    top.mainloop()

def sign_in():
    '''
    
    '''
    def yes():
        top2 = Toplevel(window)
        top2.geometry("600x600")
        top2.resizable(width=False,height=False)
        top2.title("sign in")
        top2.configure(bg="#400040")
        def okey_buttom_top():
            if (buttom_cancel or buttom_okey)==False : 
                tkinter.messagebox.ERROR("you dont chose buttom")
            if (entry_pasword.get() or entry_username.get())==" " : 
                tkinter.messagebox.showerror("error EMPTY ..."
                    ,"the entry is empty! , \npls try again!!")
                top2.destroy()
            
            elif len(entry_pasword.get())<8 : 
                tkinter.messagebox.showerror("error massage ...",
                    "your pasword must have 8 charekter , \npls try again .")
                top2.destroy()
            else:
                save_information = tkinter.messagebox.askyesno("Save Your Informations",
                    "Do You Wnat Save Your Informations")
                if save_information==True :
                    print("user username is : {}".format(entry_username.get()))
                    print("====")
                    print("user pasword is : {}".format(entry_pasword.get()))
                    print("====") 
                else:
                    tkinter.messagebox.showinfo("Back To Seit","PLS Try Again !")
                    top2.destroy()
            U_username = entry_username.get()
            U_pasword = entry_pasword.get()        
            I_email = information["email"]
            I_username = information["username"]
            I_pasword = information["pasword"]
            if U_username==I_username : 
                if U_pasword==I_pasword : 
                    massage =tkinter.messagebox.askyesno("emial massage ..."," if your EMAIL is : \n{}\nclick YES !!".format(I_email))
                    if massage==True :  
                        top3 = Toplevel(window)
                        top3.geometry("600x600")
                        top3.resizable(width=False,height=False)
                        top3.title("wellcome {}".format(U_username))
                        top3.configure(bg="#400040") 
                        labal = tkinter.Label(top3,text="<<< 'wellcome to your accont' >>>").pack()
                        top3.mainloop()
                    else : 
                        massage2 = tkinter.messagebox.showerror("error","pls back to SIGN UP\nYOUR INFORMATION IS NOT TREU ")
                        if massage2=="ok" : 
                            top2.destroy() 
                            sign_up()
                        else:
                           top2.destroy()    
                else:
                    massage2 = tkinter.messagebox.showerror("error","pls back to SIGN UP\nYOUR INFORMATION IS NOT TREU\n 'PASWORD dose not CORRECT !!' ")
                    if massage2=="ok" : 
                        top2.destroy() 
                        sign_up()
                    else:
                        top2.destroy()
            else:
                massage2 = tkinter.messagebox.showerror("error","pls back to SIGN UP\nYOUR INFORMATION IS NOT TREU\n 'USERNAME dose not CORRECT !!' ")
                if massage2=="ok" : 
                    top2.destroy() 
                    sign_up()
                else:
                    top2.destroy()
                         
                    
                    
                    
        def cancel_buttom_top() :
            cansel_massagebox= tkinter.messagebox.askyesno("cansel",
                "Do You Wnat Exit This Seit ? ")
            if cansel_massagebox==True : 
                top2.destroy()
        
        
        
        
        labal_username_note= tkinter.Label(top2,
                            text=" Pleas Inter Your Username ",
                            bg= "#400040",fg="#ff8000",
                            font= ("times new roman",25,"bold"),
                            borderwidth=15,bd=3,width=20)
        
        label_pasword_note = tk.Label(top2,
                            text=" Pleas Inter Your Pasword ",
                            bg= "#400040",fg="#ff8000",
                            font= ("times new roman",25,"bold"),
                            borderwidth=15,bd=3,width=20)
        
        label_username = tk.Label(top2,
                        text="Username : ",
                        fg="#00ffff",bg='#15181A',
                        font= ("NORMAL",12,"italic"),
                        bd=10,width=8)
        
        label_pasword = tk.Label(top2,
                        text="Pasword : ",
                        fg="#00ffff",bg='#15181A',
                        font= ("NORMAL",12,"italic"),
                        bd=10,width=8)
        
        entry_username = tk.Entry(top2,font=("names",10,"italic"),
                  bd=8,fg="#ffffff",bg="gray",
                  width=35,state="normal",highlightcolor="#8080ff",highlightthickness=3,
                  border=8,borderwidth=8,disabledbackground="#000000",)
        
        entry_pasword = tk.Entry(top2,font=("names",10,"italic"),
                  bd=8,fg="#ffffff",bg="gray",
                  width=35,state="normal",highlightcolor="#8080ff",highlightthickness=3,
                  border=8,borderwidth=8,disabledbackground="#000000",)
        
        buttom_okey = tk.Button(top2,text ="Okey",
                        relief=FLAT,font=("times new roman",15,"bold"),
                        bd=10,fg="#15181A",bg="#ff8000"
                        ,width=15,height=0,borderwidth=6,
                        anchor="center",command=okey_buttom_top)
        
        buttom_cancel = tk.Button(top2,text ="Cancel",
                        relief=FLAT,font=("times new roman",15,"bold"),
                        bd=10,fg="#15181A",bg="#ff8000"
                        ,width=15,height=0,borderwidth=6,
                        anchor="center",command=cancel_buttom_top )
        
        
        def menu():
            menu = Menu(top2)
            top2.config(menu=menu)
            filemenu = Menu(menu,tearoff=0)
            menu.add_cascade(label='File', menu=filemenu)
            filemenu.add_command(label='New')
            filemenu.add_command(label='Open...')
            filemenu.add_command(label='Setting')
            filemenu.add_separator()
            filemenu.add_command(label='Exit', command=window.quit)
            helpmenu = Menu(menu,tearoff=0)
            menu.add_cascade(label='Help', menu=helpmenu)
            helpmenu.add_command(label='About')
        menu()
        
        
        
        

        labal_username_note.place(x=10,y=80)
        label_username.place(x=100,y=150)
        entry_username.place(x=250,y=150)

        label_pasword_note.place(x=0,y=250)
        label_pasword.place(x=100,y=320)
        entry_pasword.place(x=250,y=320)

        buttom_cancel.place(x=15,y=500)
        buttom_okey.place(x=390,y=500)
                
        top2.mainloop()
    massagebox = tkinter.messagebox.askyesno("sing in","do you have accont in this seit ? ")
    if massagebox==True :
        yes() 
    else:
        sign_up()  
    
def cancel():
    cansel_massagebox= tkinter.messagebox.askyesno("cansel",
        "Do You Wnat Exit This Seit ? ")
    if cansel_massagebox==True : 
        window.destroy()
     
window = Tk()
window.geometry("500x500")
window.resizable(width=False,height=False)
window.title("welcome ...")
window.config(bg="#62626a")

# foto_background = PhotoImage(file = "D:\\work\\program\\python\\GUI\\photos\\background.png")
# foto_background2 = PhotoImage(file = "D:\\work\\program\\python\\GUI\\photos\\backraund2.png")

##      menu :: 
def menu():
    menu = Menu(window)
    window.config(menu=menu)
    filemenu = Menu(menu,tearoff=0)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_command(label='Setting')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=window.quit)
    helpmenu = Menu(menu,tearoff=0)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')
menu()

# foto_background_label = Label(window,image=foto_background)
home_page_label = Label(window,text="Home Page",
                        bg= "#400040",fg="#ff8000",
                        font= ("times new roman",25,"bold"),
                        borderwidth=15,bd=3,width=21)
sign_up_buttom = Button(window,text="Sign Up",
                        relief=FLAT,font=("times new roman",15,"bold"),
                        bd=10,fg="#15181A",bg="#ff8000",
                        width=8,height=0,borderwidth=6,
                        anchor="center",command=sign_up)
sign_in_buttom = Button(window,text="Sign In",
                        relief=FLAT,font=("times new roman",15,"bold"),
                        bd=10,fg="#15181A",bg="#ff8000",
                        width=8,height=0,borderwidth=6,
                        anchor="center",command=sign_in)
cancel_buttom = Button(window,text="Cancel",
                       relief=FLAT,font=("times new roman",15,"bold"),
                        bd=10,fg="#15181A",bg="#74cdc5",
                        width=8,height=0,borderwidth=6,
                        anchor="center",command=cancel)



##      place :: 

# foto_background_label.place(relheight=1,relwidth=1,)
home_page_label.place(x=40,y=50)
sign_in_buttom.place(x=40,y=150)
sign_up_buttom.place(x=355,y=150)
cancel_buttom.place(x=40,y=350)





mainloop()

'''     >>> fragen :: 
                1.  dakhele buttom ha che jori mishe did 
                2.  entry.get() kar nmikone baraye avalin error
                3.  age bekhaim baz bargardim be aval ?  


'''

