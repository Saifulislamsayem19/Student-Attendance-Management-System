from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os


class Login:
    def __init__(self, root):

        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()

        self.root = root
        self.root.title("Login")
        self.root.geometry('1530x790+0+0')

        # bg image
        img = Image.open(r"Images_GUI\lbg.png")
        img = img.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        fbl = Label(self.root, image=self.photoimg)
        fbl.place(x=0, y=0, width=1530, height=790)

        # login frame
        self.lgn_frame = Frame(self.root, bg="#000000", width="1150", height=700)
        self.lgn_frame.place(x=200, y=70)
        self.txt = 'Welcome ! ! !'
        self.heading = Label(self.lgn_frame, text=self.txt, font=('Times new roman', 30, 'bold'), bg='#000000',
                             fg='white')
        self.heading.place(x=80, y=30, width=300, height=30)

        leftimg = Image.open(r"Images_GUI\new.png")
        leftimg = leftimg.resize((590, 520), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(leftimg)

        leftbl = Label(self.root, image=self.photoimg1, bg='#000000')
        leftbl.place(x=200, y=230, width=590, height=520)

        # sign up part
        signimg = Image.open(r"Images_GUI\hyy.png")
        signimg = signimg.resize((160, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(signimg)
        signlbl = Label(self.root, image=self.photoimg2, bg='#000000')
        signlbl.place(x=977, y=100, width=160, height=130)

        self.txt1 = "Sign in"
        self.sign_in_lbl = Label(self.lgn_frame, text=self.txt1, font=('Times new roman', 25, 'bold'), bg='#000000',
                                 fg='white')
        self.sign_in_lbl.place(x=725, y=110, width=250, height=180)

        # username
        self.txt2 = "Email Address"
        self.sign_in_lbl = Label(self.lgn_frame, text=self.txt2, font=('Times new roman', 16, 'bold'), bg='#000000',
                                 fg='#4f4d4e')
        self.sign_in_lbl.place(x=625, y=250, width=180, height=50)

        self.txtuser = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='black', fg='white',
                             font=('comic sans ms', 15, 'bold'), cursor='hand2')
        self.txtuser.place(x=700, y=305, width=370)

        self.username_line = Canvas(self.lgn_frame, width=400, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.username_line.place(x=668, y=338)

        userimg = Image.open(
            r"Images_GUI\username_icon.png")
        userimg = userimg.resize((40, 30), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(userimg)
        userlbl = Label(self.root, image=self.photoimg3, bg='#000000')
        userlbl.place(x=860, y=375, width=40, height=30)

        # password
        self.txt3 = "Password"
        self.pswdlbl = Label(self.lgn_frame, text=self.txt3, font=('Times new roman', 16, 'bold'), bg='#000000',
                             fg='#4f4d4e')
        self.pswdlbl.place(x=605, y=340, width=180, height=50)

        self.txtpwd = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg='black', fg='white',
                            font=('comic sans ms', 15, 'bold'), cursor='hand2')
        self.txtpwd.place(x=700, y=395, width=370)

        self.pswdline = Canvas(self.lgn_frame, width=400, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.pswdline.place(x=668, y=428)

        psdimg = Image.open(
            r"Images_GUI\password_icon.png")
        psdimg = psdimg.resize((40, 30), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(psdimg)
        plbl = Label(self.root, image=self.photoimg4, bg='#000000')
        plbl.place(x=860, y=465, width=40, height=30)

        lgnbuttonimg = Image.open(
            r"Images_GUI\login2.png")
        lgnbuttonimg = lgnbuttonimg.resize((200, 60), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(lgnbuttonimg)
        lgnbbl = Button(self.root, command=self.login, image=self.photoimg5, bg='#000000', activebackground='#040405',
                        cursor='hand2',
                        bd=0)
        lgnbbl.place(x=975, y=525, width=200, height=60)

        # self.lgn_button=Button(self.lgn_frame,text="LOGIN",font=('Times new roman',13,'bold'),width=25,bd=0,bg='#3047ff',cursor='hand2',activebackground='#3047ff',fg='white')
        # self.lgn_button.place(x=20,y=10)

        # forget password
        self.forgetb = Button(self.lgn_frame, command=self.forget_pwd, text='Forget password?',
                              font=('Times new roman', 14, 'bold underline'),
                              fg='red', width=25, bd=0, bg='#040405', activebackground='#040405', cursor='hand2')
        self.forgetb.place(x=740, y=520)

        # sign up
        self.sign_up = Label(self.lgn_frame, text="No account yet?", font=('Times new roman', 13, 'bold'),
                             background='#040405', fg='white')
        self.sign_up.place(x=665, y=570)

        signbuttonimg = Image.open(
            r"Images_GUI\s3.png")
        signbuttonimg = signbuttonimg.resize((150, 60), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(signbuttonimg)
        sbl = Button(self.root, command=self.reg, image=self.photoimg6, bg='#000000', activebackground='#040405',
                     cursor='hand2', bd=0)
        sbl.place(x=1000, y=640, width=150, height=60)

        # # show/hide
        # showbuttonimg = Image.open(
        #     r"Images_GUI\show.png")
        # showbuttonimg = showbuttonimg.resize((15, 15), Image.ANTIALIAS)
        # self.photoimg7 = ImageTk.PhotoImage(showbuttonimg)
        # swbl = Button(self.root, image=self.photoimg7, bg='black', activebackground='black', cursor='hand2', bd=0,
        #               command=self.show)
        # swbl.place(x=1275, y=475, width=15, height=15)
        #
        # hidebuttonimg = Image.open(
        #     r"Images_GUI\hide.png")
        # hidebuttonimg = hidebuttonimg.resize((15, 15), Image.ANTIALIAS)
        # self.photoimg8 = ImageTk.PhotoImage(hidebuttonimg)

    #  THis function is for open register root
    def reg(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpwd.get() == "":
            messagebox.showerror("Error", "All Field Required!")
        elif self.txtuser.get() == "admin" and self.txtpwd.get() == "admin":
            messagebox.showinfo("Sussessfully", "Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='Saiful2000', host='localhost',
                                           database='face_recognition', port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s", (
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid Username and Password!")
            else:
                open_min = messagebox.askyesno("Access", "Access only Admin")
                if open_min > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()

    def reset_pass(self):
        if self.var_ssq.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question!", parent=self.root2)
        elif self.var_sa.get() == "":
            messagebox.showerror("Error", "Please Enter the Answer!", parent=self.root2)
        elif self.var_pwd.get() == "":
            messagebox.showerror("Error", "Please Enter the New Password!", parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='Saiful2000', host='localhost',
                                           database='face_recognition', port=3306)
            mycursor = conn.cursor()
            query = "select * from regteach where email=%s and ssq=%s and sa=%s"
            value = (self.txtuser.get(), self.var_ssq.get(), self.var_sa.get())
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please Enter the Correct Answer!", parent=self.root2)
            else:
                query = "update regteach set pwd=%s where email=%s"
                value = (self.var_pwd.get(), self.txtuser.get())
                mycursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Successfully Your password has been rest, Please login with new Password!",
                                    parent=self.root2)

    def forget_pwd(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='Saiful2000', host='localhost',
                                           database='face_recognition', port=3306)
            mycursor = conn.cursor()
            query = "select * from regteach where email=%s"
            value = (self.txtuser.get(),)
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            # print(row)

            if row is None:
                messagebox.showerror("Error", "Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l = Label(self.root2, text="Forget Password", font=("times new roman", 30, "bold"), fg="#002B53",
                          bg="#fff")
                l.place(x=0, y=10, relwidth=1)

                # label1
                ssq = lb1 = Label(self.root2, text="Select Security Question:", font=("times new roman", 15, "bold"),
                                  fg="#002B53", bg="#F2F2F2")
                ssq.place(x=70, y=80)

                # Combo Box1
                self.combo_security = ttk.Combobox(self.root2, textvariable=self.var_ssq,
                                                   font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security["values"] = ("Select", "Your Date of Birth", "Your Nick Name", "Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70, y=110, width=270)

                # label2
                sa = lb1 = Label(self.root2, text="Security Answer:", font=("times new roman", 15, "bold"),
                                 fg="#002B53", bg="#F2F2F2")
                sa.place(x=70, y=150)

                # entry2
                self.txtpwd = ttk.Entry(self.root2, textvariable=self.var_sa, font=("times new roman", 15, "bold"))
                self.txtpwd.place(x=70, y=180, width=270)

                # label2
                new_pwd = lb1 = Label(self.root2, text="New Password:", font=("times new roman", 15, "bold"),
                                      fg="#002B53", bg="#F2F2F2")
                new_pwd.place(x=70, y=220)

                # entry2
                self.new_pwd = ttk.Entry(self.root2, textvariable=self.var_pwd, font=("times new roman", 15, "bold"))
                self.new_pwd.place(x=70, y=250, width=270)

                # Creating Button New Password
                loginbtn = Button(self.root2, command=self.reset_pass, text="Reset Password",
                                  font=("times new roman", 15, "bold"), bd=0, relief=RIDGE, fg="#fff", bg="#002B53",
                                  activeforeground="white", activebackground="#007ACC")
                loginbtn.place(x=70, y=300, width=270, height=35)

    def show(self):
        self.hidebl = Button(self.root, image=self.photoimg8, bg='white', activebackground='white', cursor='hand2',
                             bd=0,
                             command=self.hide)
        self.hidebl.place(x=1275, y=475, width=15, height=15)
        self.txtpwd.config(show=' ')

    def hide(self):
        self.photoimg7 = ImageTk.PhotoImage(self.photoimg7)
        swbl = Button(self.root, image=self.photoimg7, bg='black', activebackground='black', cursor='hand2', bd=0,
                      command=self.show)
        swbl.place(x=1275, y=475, width=15, height=15)
        self.txtpwd(show='*')

        def reg(self):
            self.new_window = Toplevel(self.root)
            self.app = Register(self.new_window)


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1175x768+150+25")
        self.root.title("Face_Recogonition_System")

        # first header image
        img = Image.open(
            r"Images_GUI\banner1.jpg")
        img = img.resize((1175, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1175, height=130)

        # backgorund image
        bg1 = Image.open(r"Images_GUI\bg.jpg")
        bg1 = bg1.resize((1175, 768), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1175, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Attendance Managment System Using Facial Recognition",
                          font=("verdana", 25, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1175, height=45)

        # student button 1
        std_img_btn = Image.open(
            r"Images_GUI\student_portal_1.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.student_pannels, image=self.std_img1, cursor="hand2")
        std_b1.place(x=250, y=100, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.student_pannels, text="Student Details", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=250, y=280, width=180, height=45)

        # Detect Face  button 2
        det_img_btn = Image.open(
            r"Images_GUI\facialrecognition.png")
        det_img_btn = det_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, command=self.face_rec, image=self.det_img1, cursor="hand2", )
        det_b1.place(x=480, y=100, width=180, height=180)

        det_b1_1 = Button(bg_img, command=self.face_rec, text="Face Recognition", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        det_b1_1.place(x=480, y=280, width=180, height=45)

        # Attendance System  button 3
        att_img_btn = Image.open(
            r"Images_GUI\facial_0.jpg")
        att_img_btn = att_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, command=self.attendance_pannel, image=self.att_img1, cursor="hand2", )
        att_b1.place(x=710, y=100, width=180, height=180)

        att_b1_1 = Button(bg_img, command=self.attendance_pannel, text="Attendance", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        att_b1_1.place(x=710, y=280, width=180, height=45)

        # Train   button 4
        tra_img_btn = Image.open(
            r"Images_GUI\train.png")
        tra_img_btn = tra_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.tra_img1 = ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img, command=self.train_pannels, image=self.tra_img1, cursor="hand2", )
        tra_b1.place(x=250, y=330, width=180, height=180)

        tra_b1_1 = Button(bg_img, command=self.train_pannels, text="Data Train", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        tra_b1_1.place(x=250, y=510, width=180, height=45)

        # Photo   button 5
        pho_img_btn = Image.open(
            r"Images_GUI\photos.jpg")
        pho_img_btn = pho_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.pho_img1 = ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img, command=self.open_img, image=self.pho_img1, cursor="hand2", )
        pho_b1.place(x=480, y=330, width=180, height=180)

        pho_b1_1 = Button(bg_img, command=self.open_img, text="Photos", cursor="hand2", font=("tahoma", 15, "bold"),
                          bg="white", fg="navyblue")
        pho_b1_1.place(x=480, y=510, width=180, height=45)

        # exit   button
        exi_img_btn = Image.open(
            r"Images_GUI\exit2.png")
        exi_img_btn = exi_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.exi_img1 = ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img, command=self.Close, image=self.exi_img1, cursor="hand2", )
        exi_b1.place(x=710, y=330, width=180, height=180)

        exi_b1_1 = Button(bg_img, command=self.Close, text="Exit", cursor="hand2", font=("tahoma", 15, "bold"),
                          bg="white", fg="navyblue")
        exi_b1_1.place(x=710, y=510, width=180, height=45)

    def open_img(self):
        os.startfile("dataset")

    def student_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_rec(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_pannel(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def Close(self):
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()
