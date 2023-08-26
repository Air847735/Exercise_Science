import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import db, credentials
import cv2

""""
          VideoFrame              Frame1            Frame2            Frame3           Frame4
---------------------------------------------------------------------------------------------------
                                                    球員背號           最高速度        確認按鈕
                                                    entry10           entry11         button1
    ---------------------         label             entry20           entry21         button2
    -                   -                           entry30           entry31         button3
    -       Video       -         entry             entry40           entry41         button4
    -                   -                           entry50           entry51         button5
    ---------------------         button            entry60           entry61         button6
                                                    entry70           entry71         button7
                                                    entry80           entry81         button8
                                                 更新按鈕  ====>  button_All_Update
---------------------------------------------------------------------------------------------------
"""

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://sport-backend-7ec3f-default-rtdb.asia-southeast1.firebasedatabase.app/"})

def video_stream():
    _,pic = cam.read()
    frame = pic.copy()
    cv2image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    video.imgtk = imgtk
    video.configure(image=imgtk)
    video.after(1,video_stream)
    # print(frame.shape)

root = tk.Tk()
root.geometry('1600x800') # 長寬設定

#videoFrame 影片格
videoFrame = tk.Frame(root,bg="white").pack()
video = tk.Label(videoFrame)
video.pack(side='left')

# frame1 中間
frame1 = tk.Frame(root)
frame1.pack(side='left',padx='60px')

label = tk.Label(frame1,text="測試版本",font='100px')
label.pack(side='top',pady='10px')

entry = tk.Entry(frame1)
# entry.insert(0,"輸入文字")
entry.pack(side='top',pady='10px')

def button_Update():
    text = entry.get()
    db.reference("/playersInfo").set(text)
    print(text)

button = tk.Button(frame1,text='確認上傳',command=button_Update)
button.pack(side='top',pady='10px')

# frame2
frame2 = tk.Frame(root)
frame2.pack(side='left',padx='25px',fill='both')

entry10 = tk.Entry(frame2)
entry10.pack(side='top',pady='15px')

entry20 = tk.Entry(frame2)
entry20.pack(side='top',pady='15px')

entry30 = tk.Entry(frame2)
entry30.pack(side='top',pady='15px')

entry40 = tk.Entry(frame2)
entry40.pack(side='top',pady='15px')

entry50 = tk.Entry(frame2)
entry50.pack(side='top',pady='15px')

entry60 = tk.Entry(frame2)
entry60.pack(side='top',pady='15px')

entry70 = tk.Entry(frame2)
entry70.pack(side='top',pady='15px')

entry80 = tk.Entry(frame2)
entry80.pack(side='top',pady='15px')

entry_frame2 = [entry10,entry20,entry30,entry40,entry50,entry60,entry70,entry80]

check_frame2 = db.reference("/waitForRecord_list").get(False,True)
check_frame2 = [*check_frame2]
check_frame2_len = len(check_frame2)

if check_frame2_len >= 8:
    check_frame2_len = 8

for i in range(0,check_frame2_len):
    print(entry_frame2[i])
    print(db.reference("/waitForRecord_list/" + check_frame2[i]).get())
    entry_frame2[i].insert(0 , db.reference("/waitForRecord_list/" + check_frame2[i]).get())



#frame3
frame3 = tk.Frame(root)
frame3.pack(side='left',padx='25px',fill='both')

entry11 = tk.Entry(frame3)
entry11.pack(side='top',pady='15px')

entry21 = tk.Entry(frame3)
entry21.pack(side='top',pady='15px')

entry31 = tk.Entry(frame3)
entry31.pack(side='top',pady='15px')

entry41 = tk.Entry(frame3)
entry41.pack(side='top',pady='15px')

entry51 = tk.Entry(frame3)
entry51.pack(side='top',pady='15px')

entry61 = tk.Entry(frame3)
entry61.pack(side='top',pady='15px')

entry71 = tk.Entry(frame3)
entry71.pack(side='top',pady='15px')

entry81 = tk.Entry(frame3)
entry81.pack(side='top',pady='15px')

entry_frame3 = [entry11,entry21,entry31,entry41,entry51,entry61,entry71,entry81]

check_frame3 = db.reference("/waitForRecord_list").get(False,True)
check_frame3 = [check_frame3] # 進度
check_frame3_len = len(check_frame3)

if check_frame3_len >= 8:
    check_frame3_len = 8

for i in range(0,check_frame3_len):
    print(entry_frame3[i])
    print(db.reference("/waitForRecord_list/" + check_frame3[i]).get())
    entry_frame3[i].insert(0 , db.reference("/waitForRecord_list/" + check_frame3[i]).get())

def button_All_Update_command():
    # 全部Entry更新內容

button_All_Update = tk.Button(frame3,text='Update_All',height=2,command=button_All_Update_command)


#frame4
frame4 = tk.Frame(root)
frame4.pack(side='left',padx='25px',fill='both')

def button1_Update():
    number = entry10.get()
    speed = entry11.get()
    print(number)
    print(speed)
    db.reference("/waitForRecords_list/" + number).set(speed)

button1 = tk.Button(frame4,text='Button1',height=1,command=button1_Update)
button1.pack(side='top',pady='13px')

def button2_Update():
    number = entry20.get()
    speed = entry21.get()
    print(number)
    print(speed)
    db.reference("/waitForRecords_list/" + number).set(speed)

button2 = tk.Button(frame4,text='Button2',command=button2_Update)
button2.pack(side='top',pady='13px')

def button3_Update():
    number = entry30.get()
    speed = entry31.get()
    print(number)
    print(speed)
    db.reference("/waitForRecords_list/" + number).set(speed)

button3 = tk.Button(frame4,text='Button3',command=button3_Update)
button3.pack(side='top',pady='13px')

def button4_Update():
    number = entry40.get()
    speed = entry41.get()
    print(number)
    print(speed)
    db.reference("/waitForRecords_list/" + number).set(speed)

button4 = tk.Button(frame4,text='Button4',command=button4_Update)
button4.pack(side='top',pady='13px')

def button5_Update():
    number = entry50.get()
    speed = entry51.get()
    print(number)
    print(speed)
    db.reference("/waitForRecords_list/" + number).set(speed)

button5 = tk.Button(frame4,text='Button5',command=button5_Update)
button5.pack(side='top',pady='12px')

def button6_Update():
    number = entry60.get()
    speed = entry61.get()
    print(number)
    print(speed)
    db.reference("/waitForRecords_list/" + number).set(speed)

button6 = tk.Button(frame4,text='Button6',command=button6_Update)
button6.pack(side='top',pady='12px')

def button7_Update():
    number = entry70.get()
    speed = entry71.get()
    print(number)
    print(speed)
    db.reference("/waitForRecords_list/" + number).set(speed)

button7 = tk.Button(frame4,text='Button7',command=button7_Update)
button7.pack(side='top',pady='12px')

def button8_Update():
    number = entry80.get()
    speed = entry81.get()
    print(number)
    print(speed)
    db.reference("/waitForRecords_list/" + number).set(speed)

button8 = tk.Button(frame4,text='Button8',command=button8_Update)
button8.pack(side='top',pady='12px')







cam = cv2.VideoCapture(0)

video_stream()
video.mainloop()

'''
window = tk.Tk()
window.title('Sprt Science') # UI標題
window.geometry('380x400') # 長寬設定
window.resizable(False,False) # 設定視窗是否可以大小縮放
# window.iconbitmap('icon.ico') # 程式icon圖示

test = tk.Button(text='test')
test.pack(side='top')
entry = tk.Entry(window)
entry.insert(0,"輸入文字")
entry.pack(side='top')
'''
