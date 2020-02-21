from PIL import Image, ImageTk 
import tkinter
import PIL.Image
from tkinter import *
import RPi.GPIO as GPIO
import os

#vars
screenW = 564
screenH = 894

#window setup
window = tkinter.Tk()
window.title("window1")
window.geometry(str(screenW)+"x"+str(screenH))

#title text
title = tkinter.Label(window, text = "About the Team", font = ('Helvetica',int(0.053*screenW)))
title.pack()

#text body
label2 = tkinter.Label(window, text = "2473 was founded in 2007 by just 7 students with the desire to learn how to build a robot. Today, the team has grown to over 70 students divided into several sub-teams that work together, constructing a complex robot by the end of each season. Building off of the 2018 season, this team looks to take the next step in becoming a cohesive group of individuals competing in robotics."+ 
"/nThe challenge this year is called DESTINATION: DEEP SPACE and is detailed below."+
"/n/nOur team’s strategy this year revolved around crossing the Auto Run line. During the autonomous period, picking up and placing cubes on the switch throughout the driver operated period, and climbing the scale to fight the boss during End Game. We believed that this strategy would give us the best chance to be chosen as an alliance during playoff elimination rounds at tournament."
"/nAfter kickoff, all members of this team contributed towards brainstorming a strategy that would give us an ideal position at tournaments, and a strategy document is formulated. Based off of this, subteams created requirement documents for specific mechanisms of the robot, both hardware and software, and this becomes a contract that sets the standards for our end product. The project has to meet every single one of these requirements and could exceed these to meet any reaches if they have time."
"/n/nThe hardware teams collaborate using Computer Aided Design (CAD) for planning the spacing distributions on the robot and ensures both accuracy and precision in the manufacturing of parts. The students operate machinery provided by the facilities at Cupertino High School to build their projects, and after an intense prototyping process under a strict schedule, high quality hardware is produced."
"/nThe software team cohesively works as a unit to bring this hardware to life. Collaborating using technologies for version control such as Github and communication such as Slack, teams are able to work in an efficient manner. The 2473 software team endeavors in areas such as computer vision, networking, usage of the WPI library, implementing sensors, and other special projects in order to make the most out of the fine product produced by the hardware team."
"/nAssisting with this process are our amazing mentors. With 8 mentors total for both the hardware and software subteams, they provide their time, knowledge, and expertise to guide students in the right direction. Students are able to remain productive while also learning immensely under the selfless mentors, who donate several hours every week to working with us.", wraplength = int(0.887*screenW))
label2.pack()

#logo image
pic = PIL.Image.open("img.png")
pic = pic.resize((int(0.115*screenW), int(0.115*screenW)))
photo = ImageTk.PhotoImage(pic)
panel = tkinter.Label(window, image = photo)
panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.place(x=int(0.035*screenW), y=0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check():
    input_state = GPIO.input(14)
    if input_state == False:
        os.system("sudo python3 videoDemo.py")
    else:
        window.after(0, check)

window.after(1000,check)
window.mainloop()
