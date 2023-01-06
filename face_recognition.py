# import re
import csv
from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import time


class Face_Recognition:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        # first header image
        img = Image.open(r"Images_GUI\banner.jpg")
        img = img.resize((1366, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # backgorund image
        bg1 = Image.open(r"Images_GUI\bg2.jpg")
        bg1 = bg1.resize((1366, 768), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Welcome to Face Recognition Pannel", font=("verdana", 30, "bold"), bg="white",
                          fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Training button 1
        std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)

    def mark_attendance(self, d, r, n):
        col_names = ['Roll', ' Name', ' Dept', ' Date', ' Time',' Attendance']

        now = datetime.now()
        d1 = now.strftime("%d-%m-%Y")
        dtString = now.strftime("%H:%M:%S")
        dir = os.path.dirname("Attendance/")
        if not os.path.exists(dir):
            os.makedirs(dir)
        exists = os.path.isfile("Attendance\Attendance_" + d1 + ".csv")
        # print(exists)
        if exists:
            with open("Attendance\Attendance_" + d1 + ".csv", "r+", newline="\n") as f:
                myDatalist = f.readlines()
                name_list = []
                for line in myDatalist:
                    entry = line.split((","))
                    name_list.append(entry[0])

                if (d not in name_list) and (r not in name_list) and (n not in name_list):
                    f.writelines(f"\n{r}, {n}, {d}, {dtString}, {d1}, Present")
                    print("attendance")
            f.close()
        else:
            with open("Attendance\Attendance_" + d1 + ".csv", "a+") as f:
                writer = csv.writer(f)
                writer.writerow(col_names)
                myDatalist = f.readlines()
                name_list = []
                for line in myDatalist:
                    entry = line.split((","))
                    name_list.append(entry[0])

                if (d not in name_list) and (r not in name_list) and (n not in name_list):
                    f.writelines(f"{r}, {n}, {d}, {dtString}, {d1}, Present")
                    # print("attendance")
            f.close()

    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")
        videoCap = cv2.VideoCapture(0)
        # col_names = ['Id', '', 'Name', '', 'Roll', '', 'Date', '', 'Time']
        while True:
            ret, img = videoCap.read()
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            featuers = faceCascade.detectMultiScale(gray_image, 1.1, 10)

            for (x, y, w, h) in featuers:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(username='root', password='Saiful2000', host='localhost',
                                               database='face_recognition', port=3306)
                cursor = conn.cursor()
                # print(id)

                cursor.execute("select Name from student where Student_ID=" + str(id))
                n = cursor.fetchone()
                # print(n, id)
                n = "+".join(n)

                cursor.execute("select Roll_No from student where Student_ID=" + str(id))
                r = cursor.fetchone()
                r = "+".join(r)

                cursor.execute("select Department from student where Student_ID=" + str(id))
                d = cursor.fetchone()
                d = "+".join(d)
                # print(n, r, i)

                if confidence > 77:
                    # now = datetime.now()
                    # date = now.strftime("%d-%m-%Y")
                    # time = now.strftime("%H:%M:%S")

                    cv2.putText(img, f"Name:{n}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll-No:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Dept:{d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(d, r, n)
                    # attendance = [i, '', n, '', r, '', str(date), '', str(time)]
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == ord('q'):
                break

        # now = datetime.now()
        # date = now.strftime("%d-%m-%Y")
        #
        # exists = os.path.isfile("Attendance\Attendance_" + date + ".csv")
        # print(exists)
        # if exists:
        #     with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
        #         writer = csv.writer(csvFile1)
        #         writer.writerow(attendance)
        #     csvFile1.close()
        # else:
        #     with open("Attendance\Attendance_" + date + ".csv", 'a+') as csvFile1:
        #         writer = csv.writer(csvFile1)
        #         writer.writerow(col_names)
        #         writer.writerow(attendance)
        #     csvFile1.close()

        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
