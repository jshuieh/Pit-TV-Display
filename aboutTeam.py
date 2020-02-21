notificationnotificationclose

from PIL import Image, ImageTk 
import tkinter
import PIL.Image
import tkinter as Tk, tkinter.font as tkFont

#vars
#screenW = 768
#screenH = 1024

#window setup
window = Tk.Tk()
window.title("window1")
window.config(bg='black')
screenW = window.winfo_screenwidth()
screenH = window.winfo_screenheight()
screenRatio = screenH*screenW
#window.geometry(str(screenW)+"x"+str(screenH))
#window.geometry("{0}x{1}+0+0".format(int(0.9*screenW), int(0.9*screenW*screenRatio)))
window.geometry("{0}x{1}+0+0".format(screenW, screenH))
window.overrideredirect(1)


'''
#background image
bgImg = Image.open("bg.jpeg")
bgImg = bgImg.resize((window.winfo_screenwidth(),window.winfo_screenheight()), Image.ANTIALIAS)
background_image = Tk.PhotoImage(file = bgImg)
#background_image.zoom(window.winfo_screenwidth(),window.winfo_screenheight())
background_label = Tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
'''

#title text
title = Tk.Label(window, text = "About the Team", font = ('Helvetica',int(0.053*screenW)), fg = "white", bg= "#010102")
title.pack(ipadx = 3, ipady = 3, pady = 5)

#team pic 2
team_pic2 = PIL.Image.open("team_pic2.jpg")
t_img_width2, t_img_height2 = team_pic2.size
team_pic_ratio2 = t_img_height2/t_img_width2
team_pic2 = team_pic2.resize((int(0.6*screenW), int(0.6*screenW*team_pic_ratio2)))
team_photo2 = ImageTk.PhotoImage(team_pic2)
team_panel2 = Tk.Label(window, image = team_photo2, bg = "#010102")
#team_panel.pack(fill = "both", expand = "yes", pady = 3)
team_panel2.pack(pady = 5)
'''
class BLabel(object):
    b = "•"
    def __init__(self,master):
        import tkinter as tk
        self.l = tk.Label(master)
    def add_option(self,text):
        if self.l.cget("text") == "":
            self.l.config(text=self.b+" "+text)
        else:
            self.l.config(text=self.l.cget("text") +"\n"+ self.b + " "+text)

lbal = BLabel(master=window)    
lbal.add_option("2473 was founded in 2007 by just 7 students with the desire to learn how to build a robot. Today, the team has grown to over 70 students divided into several sub-teams that work together, constructing a complex robot by the end of each season. Building off of the 2018 season, this team looks to take the next step in becoming a cohesive group of individuals competing in robotics.")
lbal.add_option("Our team's strategy this year revolved around crossing the Auto Run line. During the autonomous period, picking up and placing cubes on the switch throughout the driver operated period, and climbing the scale to fight the boss during End Game. We believed that this strategy would give us the best chance to be chosen as an alliance during playoff elimination rounds at tournament.")
lbal.add_option("After kickoff, all members of this team contributed towards brainstorming a strategy that would give us an ideal position at tournaments, and a strategy document is formulated. Based off of this, subteams created requirement documents for specific mechanisms of the robot, both hardware and software, and this becomes a contract that sets the standards for our end product. The project has to meet every single one of these requirements and could exceed these to meet any reaches if they have time.")
lbal.add_option("The hardware teams collaborate using Computer Aided Design (CAD) for planning the spacing distributions on the robot and ensures both accuracy and precision in the manufacturing of parts. The students operate machinery provided by the facilities at Cupertino High School to build their projects, and after an intense prototyping process under a strict schedule, high quality hardware is produced.")
lbal.add_option("The software team cohesively works as a unit to bring this hardware to life. Collaborating using technologies for version control such as Github and communication such as Slack, teams are able to work in an efficient manner. The 2473 software team endeavors in areas such as computer vision, networking, usage of the WPI library, implementing sensors, and other special projects in order to make the most out of the fine product produced by the hardware team.")
lbal.add_option("Assisting with this process are our amazing mentors. With 8 mentors total for both the hardware and software subteams, they provide their time, knowledge, and expertise to guide students in the right direction. Students are able to remain productive while also learning immensely under the selfless mentors, who donate several hours every week to working with us.")
lbal.l.pack()
'''
#text body
label2 = Tk.Label(window, text = "     2473 was founded in 2007 by just 7 students with the desire to learn how to build a robot. Today, the team has grown to over      70 students divided into several sub-teams that work together, constructing a complex robot by the end of each season. Building off of the 2018 season, this team looks to take the next step in becoming a cohesive group of individuals competing in robotics."+ 
"\n\n     The challenge this year is called DESTINATION: DEEP SPACE and is detailed below."+
"\n     The objective of this year’s challenge, DESTINATION: DEEP SPACE, is to deploy a robot from a station called habitat, attach hatch panels to hatches on the rockets and the cargo ship, and add cargo through the hatches into the rockets and the cargo ship. The competition also has an autonomous and manual period. During the autonomous period, our robot can dismount from stage 2, among the 3 stages, 1 being the lowest and 3 being to highest. The robot is also driver-operated using a camera on the robot. The robot can intake cargo from the ground and the player station as well using an arm mechanism, score hatch panels on the hatches, and cargo on the cargo ship and all levels of the rocket using an elevator mechanism. When the game is over, and the robot is to return to the habitat, it can climb onto stage 1."
"\n     After kickoff, all members of this team contributed towards brainstorming a strategy that would give us an ideal position at tournaments, and a strategy document is formulated. Based off of this, subteams created requirement documents for specific mechanisms of the robot, both hardware and software, and this becomes a contract that sets the standards for our end product. The project has to meet every single one of these requirements and could exceed these to meet any reaches if they have time."
"\n     Assisting with this process are our amazing mentors. With 10 mentors total for both the hardware and software subteams, they provide their time, knowledge, and expertise to guide students in the right direction. Students are able to remain productive while also learning immensely under the selfless mentors, who donate several hours every week to working with us.", wraplength = int(0.887*screenW),font = ('Arial', 19), fg = "white", bg = "#010102",justify='left')
label2.pack(ipadx = 3, ipady = 3,pady = 5)

#logo image
pic = PIL.Image.open("img1.png")
pic = pic.resize((int(0.075*screenW), int(0.075*screenW)))
photo = ImageTk.PhotoImage(pic)
panel = Tk.Label(window, image = photo, bg = "#010102")
panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.place(x=int(0.1*screenW), y=0)

#team pic
team_pic = PIL.Image.open("team_pic.jpg")
t_img_width, t_img_height = team_pic.size
team_pic_ratio = t_img_height/t_img_width
team_pic = team_pic.resize((int(0.6*screenW), int(0.6*screenW*team_pic_ratio)))
team_photo = ImageTk.PhotoImage(team_pic)
team_panel = Tk.Label(window, image = team_photo, bg = "#010102")
#team_panel.pack(fill = "both", expand = "yes", pady = 3)
team_panel.pack(pady = 5)

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