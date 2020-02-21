from PIL import Image, ImageTk 
import tkinter
import PIL.Image
import tkinter as Tk, tkinter.font as tkFont

#vars
#screenW = 768
screenH = 1024

#window setup
window = Tk.Tk()
window.title("window1")
#window.geometry(str(screenW)+"x"+str(screenH))
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.overrideredirect(1)

screenW = window.winfo_screenwidth()

#background image

background_image = Tk.PhotoImage(file="background.gif")
background_label = Tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#title text
title = Tk.Label(window, text = "About the Robot", font = ('Arial',int(0.053*screenW)), fg = "white", bg= "#010102")
title.pack(ipadx = 3, ipady = 3, pady = 5)

#text body
label2 = Tk.Label(window, text = ""+ 
"\n"+
"\n"
"\n"
"\n\n"
"\n"
"\n", wraplength = int(0.887*screenW),font = ('Arial', 12), fg = "white", bg = "#010102")
label2.pack(ipadx = 3, ipady = 3,pady = 5)

#logo image
pic = PIL.Image.open("img1.png")
pic = pic.resize((int(0.075*screenW), int(0.075*screenW)))
photo = ImageTk.PhotoImage(pic)
panel = Tk.Label(window, image = photo, bg = "#010102")
panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.place(x=int(0.1*screenW), y=0)

#robot pic
robot_pic = PIL.Image.open("robot_pic.jpg")
r_img_width, r_img_height = robot_pic.size
robot_pic_ratio = r_img_height/r_img_width
robot_pic = robot_pic.resize((int(0.13*screenW), int(0.13*screenW*robot_pic_ratio)))
robot_photo = ImageTk.PhotoImage(robot_pic)
robot_panel = Tk.Label(window, image = robot_photo, bg = "#010102")
robot_panel.pack(pady = 5)

#button labels
label_1 = Tk.Label(window,text = "About the Robot",font = ('Helvetica', 16), bg = "gray")
label_2 = Tk.Label(window,text = "About the Team",font = ('Helvetica', 16))
label_3 = Tk.Label(window,text = "Computer Vision",font = ('Helvetica', 16), bg = "gray")
label_4 = Tk.Label(window,text = "Video Game Demo",font = ('Helvetica', 16))
label_1.pack(side = "left", fill = "both", expand = "yes")
label_2.pack(side = "left", fill = "both", expand = "yes")
label_3.pack(side = "left", fill = "both", expand = "yes")
label_4.pack(side = "left", fill = "both", expand = "yes")

window.mainloop()