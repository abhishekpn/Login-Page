
from tkinter import *
from PIL import  ImageTk

from tkinter import messagebox
class Login_System:

    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #### All Images
        self.bg_icon = ImageTk.PhotoImage(file ="338964.jpg" )
        # self.bg_user = PhotoImage(file ="user.png")
        # self.bg_pass = PhotoImage(file ="paass.png" )
        self.bg_logo = PhotoImage(file ="userlogo.png" )

        bg_label = Label(self.root, image = self.bg_icon)
        bg_label.pack()

        title = Label(self.root,text = "Login System", font = "Lucida 40 bold",bg = "yellow", fg = "Red",
                      relief = GROOVE)
        title.place(x = 0, y = 0, relwidth = 1)

        Login_frame = Frame(self.root, bg = "White",padx = 100)
        Login_frame.place(x = 400,y =150 )

        logo_label = Label(Login_frame, image = self.bg_logo,bd=0)
        logo_label.grid(row = 0, columnspan = 2, pady = 20)

        # lbuser = Label(Login_frame, text = "Username",height = 20, image = self.bg_user,compound = LEFT,
        #                font = ("times new roman", 20,"bold"))
        # lbuser.grid(row = 1, column = 0, padx = 20, pady = 10)

        self.user_name = StringVar()
        self.pass_word = StringVar()
        user_namelabel = Label(Login_frame,text = "Username: ",font = "ariel 15 bold",bg = "white",pady = 20)
        user_namelabel.grid(row = 1 , column = 0)
        username_entry = Entry(Login_frame,textvariable =self.user_name,bd = 5,relief = GROOVE,width = 30 )
        username_entry.grid(row = 1,column = 1)

        pass_namelabel = Label(Login_frame, text="Password: ", font="ariel 15 bold", bg="white")
        pass_namelabel.grid(row=3, column=0)
        password_entry = Entry(Login_frame, textvariable=self.pass_word,bd= 5,relief = GROOVE,width = 30)
        password_entry.grid(row=3, column=1)

        ######### Login Button

        login_btn = Button(Login_frame, text = "Login",font =("cambria",15,"bold"),relief = GROOVE,bg = "yellow",fg = "red",padx = 25,
                           pady = 3,command = self.login)
        login_btn.grid(row = 4, column = 0,pady = 10)

    def login(self):

        if self.user_name.get() == "" or self.pass_word.get() == "":
            messagebox.showerror("Error", message="All fields are required!!")

        elif self.user_name.get() == "Abhishek Pandey" and self.pass_word.get() == "abhi0409":
            messagebox.showinfo("Logged in", message=f"Welcome {self.user_name.get()}")

        else:
            messagebox.showerror("Error", message="Invalid Username or Password")


root = Tk()
obj = Login_System(root)
root.mainloop()
