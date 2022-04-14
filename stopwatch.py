#!/usr/bin/python3

import turtle
from tkinter import *
import tkinter as tk
from tkinter.ttk import * 
import tkinter.font as tkFont
import time

s,m,h,d=0,0,0,0
RUNNING = False
RESET = False
FLAG = False

def check_size(inp):
    """
    a function checking if a number (seconde,minute or hour)
    need a 0 for a better display
    ex: 01:09 is better than 1:9
    """
    if inp<10:
        r = "0"+str(inp)
    else:
        r = str(inp)
    return r

def setup_clock(clock):

    clock.hideturtle()
    clock.color("#eb4531")
    clock.width(5)
    clock.up()
    clock.goto(0,160)
    clock.down()

def update_clock(app):
    global d,h,m,s,RESET,FLAG

    s+=1
    d+=6
    if d == 360: d=0

    if RESET:
        s=0
        m=0
        h=0
        RESET=False

    if s==60:
        s=0
        m+=1
        if m==60:
            m=0
            h+=1
        app.clock.clear()
    if h==24:
        h=0
        app.page.title("YOU SHOULD STOP NOW...")

    if m==0 and h==0:
        display = check_size(s)
    elif h==0:
        display = "{}:{}".format(check_size(m),check_size(s))
    else:
        display="{}:{}:{}".format(check_size(h),check_size(m),check_size(s))
    app.time_label.set(display)
    if FLAG:
        app.flag_label.set(display)
        FLAG=False

    app.clock.circle(-110,6)

class stopwatch():
    def __init__(self, root):

        #define the tkinter window
        self.page = root
        root.title("stopwatch")
        width=300
        height=400
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root["bg"]="#b7ba26"
        p=PhotoImage(file='data/stopwatch.png')
        root.iconphoto(False,p)

        #define the turtle canvas
        canvas = tk.Canvas(root)
        canvas.config(width=290, height=390)

        canvas.place(x=5,y=5,width=290,height=390)
        screen = turtle.TurtleScreen(canvas)
        screen.bgcolor("#282828")

        #circle behind the clock
        circle = turtle.RawTurtle(screen)
        circle.speed(0)
        circle.width(3)
        circle.color("#000000")
        circle.hideturtle()
        circle.up()
        circle.goto(0,160)
        circle.down()
        circle.circle(-110)

        #define the moving clock object
        self.clock = turtle.RawTurtle(screen)
        self.clock.speed(0)
        self.clock.hideturtle()
        self.clock.color("#eb4531")
        self.clock.width(5)
        self.clock.up()
        self.clock.goto(0,160)
        self.clock.down()

        #define the tkinter label to display time
        self.time_label = tk.StringVar()
        self.time_label.set("00:00:00")

        label_time=tk.Label(root)
        label_time["font"] = tkFont.Font(family='DejaVu Sans Mono',size=15)
        label_time["fg"] = "#ffffff"
        label_time["bg"] = "#282828"
        label_time["justify"] = "center"
        label_time["textvariable"] = self.time_label
        label_time.place(x=95,y=135,width=110,height=30)

        #start/pause self.button
        self.button_text = tk.StringVar()
        self.button_text.set("\U000025b6")

        button_start=tk.Button(root)
        button_start["bg"] = "#282828"
        button_start["activebackground"] = "#282828"
        button_start["activeforeground"] = "#ffffff"
        button_start["font"] = tkFont.Font(family="Gotham",size=20)
        button_start["fg"] = "#a5a5a5"
        button_start["justify"] = "center"
        button_start["highlightthickness"] = 0
        button_start["borderwidth"] = 0
        button_start["textvariable"] = self.button_text
        button_start.place(x=100,y=330,width=100,height=40)
        button_start["command"] = self.button_start

        #close app button X

        button_close=tk.Button(root)
        button_close["bg"]="#282828"
        button_close["activebackground"] = "#282828"
        button_close["activeforeground"] = "#ff0000"
        button_close["fg"]="#a5a5a5"
        button_close["font"] = tkFont.Font(family="Gotham",size=25)
        button_close["justify"]="center"
        button_close["highlightthickness"] = 0
        button_close["borderwidth"] = 0
        button_close["text"] = '\U00002715'
        button_close.place(x=250,y=10,width=40,height=40)
        button_close["command"] = self.button_close

        #reset clock button
        button_reset=tk.Button(root)
        button_reset["bg"]="#282828"
        button_reset["activebackground"] = "#282828"
        button_reset["activeforeground"] = "#ffffff"
        button_reset["fg"]="#a5a5a5"
        button_reset["font"] = tkFont.Font(family="Gotham",size=25)
        button_reset["justify"]="center"
        button_reset["highlightthickness"] = 0
        button_reset["borderwidth"] = 0
        button_reset["text"] = '\U000021ba'
        button_reset.place(x=30,y=330,width=40,height=40)
        button_reset["command"] = self.button_reset

        # flag button
        button_flag=tk.Button(root)
        button_flag["bg"]="#282828"
        button_flag["activebackground"] = "#282828"
        button_flag["activeforeground"] = "#ffffff"
        button_flag["fg"]="#a5a5a5"
        button_flag["font"] = tkFont.Font(family="Gotham",size=25)
        button_flag["justify"]="center"
        button_flag["highlightthickness"] = 0
        button_flag["borderwidth"] = 0
        button_flag["text"] = '\U00002691'
        button_flag.place(x=230,y=330,width=40,height=40)
        button_flag["command"] = self.button_flag

        #define the tkinter label to display time

        self.flag_label = tk.StringVar()

        label_flag=tk.Label(root)
        label_flag["font"] = tkFont.Font(family='DejaVu Sans Mono',size=15)
        label_flag["fg"] = "#ffffff"
        label_flag["bg"] = "#282828"
        label_flag["justify"] = "center"
        label_flag["textvariable"] = self.flag_label
        label_flag.place(x=80,y=280,width=140,height=20)


    def button_close(self):
        self.page.destroy()

    def button_start(self):
        global RUNNING
        RUNNING = not RUNNING
        if(RUNNING): self.button_text.set('\U000001c0\U000001c0') # 01c0 is better than 01c1 bcause more space btween the 2 bar (ǀǀ or ǁ)
        else: self.button_text.set('\U000025b6') # ▶

    def button_flag(self):
        global FLAG
        FLAG = True

    def button_reset(self):
        global RESET
        self.clock.clear()
        #self.clock.speed(0)
        self.clock.up()
        self.clock.home()
        self.clock.goto(0,160)
        self.clock.down()
        #self.clock.speed(6)
        self.time_label.set("00:00:00")
        self.flag_label.set("")
        RESET = True

if __name__ == "__main__":
    root = tk.Tk()
    app = stopwatch(root)
    t1=0
    while True:
        app.page.update()
        if RUNNING:
            t2 = time.perf_counter()
            if t2 - t1 > 1:
                #print(t2-t1)
                update_clock(app)
                t1 = t2
                #d = t2-t1
                #time.sleep(1-d)
