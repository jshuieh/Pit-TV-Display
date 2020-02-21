from PIL import Image, ImageTk 
import tkinter
import PIL.Image
import tkinter as Tk, tkinter.font as tkFont
from threading import Timer
import os
import RPi.GPIO as GPIO
import subprocess
from subprocess import Popen
import time

#vars
#screenW = 768
screenH = 1024
video_name = "moonwalk1.mov"

#window setup
window = Tk.Tk()
window.title("window1")
#window.geometry(str(screenW)+"x"+str(screenH))
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.overrideredirect(1)
screenW = window.winfo_screenwidth()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14,GPIO.RISING,callback=playVideo)
                      

def main(): 
    t = Timer(30.0, playVideo)
    
    aboutRobot()

def aboutRobot():
    #background image
    
    background_image = Tk.PhotoImage(file="background.gif")
    background_label = Tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #title text
    title = Tk.Label(window, text = "About the Robot", font = ('Arial',int(0.053*screenW)), fg = "white", bg= "#010102")
    title.pack(ipadx = 3, ipady = 3, pady = 5)
    
    #text body
    label2 = Tk.Label(window, text = "2473 was founded in 2007 by just 7 students with the desire to learn how to build a robot. Today, the team has grown to over 70 students divided into several sub-teams that work together, constructing a complex robot by the end of each season. Building off of the 2018 season, this team looks to take the next step in becoming a cohesive group of individuals competing in robotics."+ 
    "\nThe challenge this year is called DESTINATION: DEEP SPACE and is detailed below."+
    "\nOur team's strategy this year revolved around crossing the Auto Run line. During the autonomous period, picking up and placing cubes on the switch throughout the driver operated period, and climbing the scale to fight the boss during End Game. We believed that this strategy would give us the best chance to be chosen as an alliance during playoff elimination rounds at tournament."
    "\nAfter kickoff, all members of this team contributed towards brainstorming a strategy that would give us an ideal position at tournaments, and a strategy document is formulated. Based off of this, subteams created requirement documents for specific mechanisms of the robot, both hardware and software, and this becomes a contract that sets the standards for our end product. The project has to meet every single one of these requirements and could exceed these to meet any reaches if they have time."
    "\n\nThe hardware teams collaborate using Computer Aided Design (CAD) for planning the spacing distributions on the robot and ensures both accuracy and precision in the manufacturing of parts. The students operate machinery provided by the facilities at Cupertino High School to build their projects, and after an intense prototyping process under a strict schedule, high quality hardware is produced."
    "\nThe software team cohesively works as a unit to bring this hardware to life. Collaborating using technologies for version control such as Github and communication such as Slack, teams are able to work in an efficient manner. The 2473 software team endeavors in areas such as computer vision, networking, usage of the WPI library, implementing sensors, and other special projects in order to make the most out of the fine product produced by the hardware team."
    "\nAssisting with this process are our amazing mentors. With 8 mentors total for both the hardware and software subteams, they provide their time, knowledge, and expertise to guide students in the right direction. Students are able to remain productive while also learning immensely under the selfless mentors, who donate several hours every week to working with us.", wraplength = int(0.887*screenW),font = ('Arial', 12), fg = "white", bg = "#010102")
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
    robot_panel.pack(side = "bottom", fill = "both", expand = "yes", pady = 5)
    
    window.mainloop()

def aboutTeam():
    #background image
    background_image = Tk.PhotoImage(file="background.gif")
    background_label = Tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    #title text
    title = Tk.Label(window, text = "About the Team", font = ('Arial',int(0.053*screenW)), fg = "white", bg= "#010102")
    title.pack(ipadx = 3, ipady = 3, pady = 5)
    
    #text body
    label2 = Tk.Label(window, text = "2473 was founded in 2007 by just 7 students with the desire to learn how to build a robot. Today, the team has grown to over 70 students divided into several sub-teams that work together, constructing a complex robot by the end of each season. Building off of the 2018 season, this team looks to take the next step in becoming a cohesive group of individuals competing in robotics."+ 
    "\nThe challenge this year is called DESTINATION: DEEP SPACE and is detailed below."+
    "\nOur team's strategy this year revolved around crossing the Auto Run line. During the autonomous period, picking up and placing cubes on the switch throughout the driver operated period, and climbing the scale to fight the boss during End Game. We believed that this strategy would give us the best chance to be chosen as an alliance during playoff elimination rounds at tournament."
    "\nAfter kickoff, all members of this team contributed towards brainstorming a strategy that would give us an ideal position at tournaments, and a strategy document is formulated. Based off of this, subteams created requirement documents for specific mechanisms of the robot, both hardware and software, and this becomes a contract that sets the standards for our end product. The project has to meet every single one of these requirements and could exceed these to meet any reaches if they have time."
    "\n\nThe hardware teams collaborate using Computer Aided Design (CAD) for planning the spacing distributions on the robot and ensures both accuracy and precision in the manufacturing of parts. The students operate machinery provided by the facilities at Cupertino High School to build their projects, and after an intense prototyping process under a strict schedule, high quality hardware is produced."
    "\nThe software team cohesively works as a unit to bring this hardware to life. Collaborating using technologies for version control such as Github and communication such as Slack, teams are able to work in an efficient manner. The 2473 software team endeavors in areas such as computer vision, networking, usage of the WPI library, implementing sensors, and other special projects in order to make the most out of the fine product produced by the hardware team."
    "\nAssisting with this process are our amazing mentors. With 8 mentors total for both the hardware and software subteams, they provide their time, knowledge, and expertise to guide students in the right direction. Students are able to remain productive while also learning immensely under the selfless mentors, who donate several hours every week to working with us.", wraplength = int(0.887*screenW),font = ('Arial', 12), fg = "white", bg = "#010102")
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
    team_photo = ImageTk.PhotoImage(team_pic)
    team_panel = Tk.Label(window, image = team_photo, bg = "#010102")
    team_panel.pack(side = "bottom", fill = "both", expand = "yes", pady = 5)
    
    #team pic
    tean_pic = PIL.Image.open("team_pic.jpg")
    t_img_width, t_img_height = team_pic.size
    team_pic_ratio = t_img_height/t_img_width
    team_pic = team_pic.resize((int(0.13*screenW), int(0.13*screenW*team_pic_ratio)))
    tean_photo = ImageTk.PhotoImage(team_pic)
    team_panel = Tk.Label(window, image = team_photo, bg = "#010102")
    team_panel.pack(side = "bottom", fill = "both", expand = "yes", pady = 5)
    
    window.mainloop()

def playVideo(channel):
   player = subprocess.Popen(["omxplayer",video_name,"--aspect-mode","fill"])
    


main()
