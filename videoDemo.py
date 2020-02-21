'''
import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk

video_name = "moonwalk.mov" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

if __name__ == "__main__":

    root = tk.qTk()
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.dqqqqqqaemon = 1
    thread.start()
    root.mainloop()
'''

import os
video_name = "moonwalk1.mov"
import RPi.GPIO as GPIO
import subprocess
from subprocess import Popen
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

player = subprocess.Popen(["omxplayer",video_name,"--aspect-mode","fill"])
while True:
    input_state = GPIO.input(14)
    if input_state == False:
        subprocess.call("pkill omx", shell = True)
        break
