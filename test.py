#!/usr/bin/python3

import turtle
import tkinter as tk
import tkinter.font as tkFont
import time

c=0

def do_stuff(app):
    global c
    #coord = -100, -100, 240, 210
    #arc = canvas.create_arc(coord, start=30, extent=c, style=tk.ARC, width=3)
    app.clock.circle(-80,6)
    c+=6
    app.time_label.set(str(c))
    if c==360:
        c=0
        app.clock.clear()

def press():
    do_stuff()


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
        root["bg"]="#eb4531"

        #define the turtle canvas
        canvas = tk.Canvas(root)
        canvas.config(width=380, height=480)
        canvas.place(x=10,y=10)
        screen = turtle.TurtleScreen(canvas)
        screen.bgcolor("#282828")

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

        label_time=tk.Label(root)
        label_time["font"] = tkFont.Font(family='Gotham',size=12, weight = 'bold')
        label_time["fg"] = "#000000"
        label_time["bg"] = "#282828"
        label_time["justify"] = "center"
        label_time["textvariable"] = self.time_label
        label_time.place(x=150,y=150,width=116,height=30)


if __name__ == "__main__":
    root = tk.Tk()
    app = stopwatch(root)

    while True:
        do_stuff(app)
        app.page.update()
        time.sleep(0.2)
