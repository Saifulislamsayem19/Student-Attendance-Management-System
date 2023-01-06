from tkinter import *
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1175x768+150+25")
        self.root.title("Face_Recogonition_System")

        # first header image
        img = Image.open(r"Images_GUI\banner1.jpg")
        img = img.resize((1175, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1175, height=130)

        # backgorund image 
        bg1 = Image.open(r"Images_GUI\bg2.jpg")
        bg1 = bg1.resize((1175, 768), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1175, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Welcome To Student Attendance Managment System",
                          font=("verdana", 25, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1175, height=45)

        # student button 1
        std_img_btn = Image.open(r"Images_GUI\student_portal_1.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.student_pannels, image=self.std_img1, cursor="hand2")
        std_b1.place(x=250, y=100, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.student_pannels, text="Students Details", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=250, y=280, width=180, height=30)

        # Photo   button 2
        pho_img_btn = Image.open(r"Images_GUI\photos.jpg")
        pho_img_btn = pho_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.pho_img1 = ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img, command=self.open_img, image=self.pho_img1, cursor="hand2", )
        pho_b1.place(x=480, y=100, width=180, height=180)

        pho_b1_1 = Button(bg_img, command=self.open_img, text="Check Photos", cursor="hand2", font=("tahoma", 15, "bold"),
                          bg="white", fg="navyblue")
        pho_b1_1.place(x=480, y=280, width=180, height=30)

        # Train   button 3
        tra_img_btn = Image.open(r"Images_GUI\train.png")
        tra_img_btn = tra_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.tra_img1 = ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img, command=self.train_pannels, image=self.tra_img1, cursor="hand2", )
        tra_b1.place(x=710, y=100, width=180, height=180)

        tra_b1_1 = Button(bg_img, command=self.train_pannels, text="Train AI", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        tra_b1_1.place(x=710, y=280, width=180, height=30)

        # Detect Face  button 4
        det_img_btn = Image.open(r"Images_GUI\facial_0.jpg")
        det_img_btn = det_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, command=self.face_rec, image=self.det_img1, cursor="hand2", )
        det_b1.place(x=250, y=330, width=180, height=180)

        det_b1_1 = Button(bg_img, command=self.face_rec, text="Take Attendance", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        det_b1_1.place(x=250, y=510, width=180, height=30)

        # Attendance System  button 5
        att_img_btn = Image.open(r"Images_GUI\att.jpg")
        att_img_btn = att_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, command=self.attendance_pannel, image=self.att_img1, cursor="hand2", )
        att_b1.place(x=480, y=330, width=180, height=180)

        att_b1_1 = Button(bg_img, command=self.attendance_pannel, text="Check Attendance", cursor="hand2",
                          font=("tahoma", 14, "bold"), bg="white", fg="navyblue")
        att_b1_1.place(x=480, y=510, width=180, height=30)

        # exit   button
        exi_img_btn = Image.open(r"Images_GUI\exit2.png")
        exi_img_btn = exi_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.exi_img1 = ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img, command=self.Close, image=self.exi_img1, cursor="hand2", )
        exi_b1.place(x=710, y=330, width=180, height=180)

        exi_b1_1 = Button(bg_img, command=self.Close, text="Exit", cursor="hand2", font=("tahoma", 15, "bold"),
                          bg="white", fg="navyblue")
        exi_b1_1.place(x=710, y=510, width=180, height=30)

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
    obj = Face_Recognition_System(root)
    root.mainloop()
