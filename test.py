#!/usr/bin/python3

import turtle
import tkinter as tk
import tkinter.font as tkFont
import time

s,m,h=0,0,0

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

def update_clock(app):
    global h,m,s
    app.clock.circle(-80,6)
    s+=1
    if s==60:
        s=0
        m+=1
        if m==60:
            m=0
            h+=1
        app.clock.clear()

    if m==0:
        display = check_size(s)
    elif h==0:
        display = "{}:{}".format(check_size(m),check_size(s))
    else:
        display="{}:{}:{}".format(check_size(h),check_size(m),check_size(s))
    app.time_label.set(display)

class stopwatch():
    def __init__(self, root):

        #define the tkinter window
        self.page = root
        root.title("stopwatch")
        width=400
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root["bg"]="#b7ba26"#"#eb4531"

        #define the turtle canvas
        canvas = tk.Canvas(root)
        canvas.config(width=400, height=500)
        canvas.place(x=0,y=0)
        #canvas.place(x=10,y=15)
        screen = turtle.TurtleScreen(canvas)
        screen.bgcolor("#282828")

        #circle behind the clock
        circle = turtle.RawTurtle(screen)
        circle.speed(0)
        circle.width(3)
        circle.hideturtle()
        circle.penup()
        circle.goto(0,160)
        circle.pendown()
        circle.circle(-80)

        #define the moving clock object
        self.clock = turtle.RawTurtle(screen)
        self.clock.hideturtle()
        self.clock.color("#eb4531")
        self.clock.width(5)
        self.clock.penup()
        self.clock.goto(0,160)
        self.clock.pendown()

        #define the tkinter label to display time
        self.time_label = tk.StringVar()

        self.label_time=tk.Label(root)
        self.label_time["font"] = tkFont.Font(family='Gotham',size=12, weight = 'bold')
        self.label_time["fg"] = "#ffffff"
        self.label_time["bg"] = "#282828"
        self.label_time["justify"] = "center"
        self.label_time["textvariable"] = self.time_label
        self.label_time.place(x=145,y=150,width=110,height=30)
        #same thing but with turtle this time

        self.display = turtle.RawTurtle(screen)
        self.display.hideturtle()
        self.display.penup()
        self.display.goto(0,70)
        self.display.pendown()

if __name__ == "__main__":
    root = tk.Tk()
    app = stopwatch(root)

    while True:
        update_clock(app)
        app.page.update()
        #time.sleep(0.01)
