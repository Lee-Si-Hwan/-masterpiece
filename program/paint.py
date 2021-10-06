from tkinter import *
from tkinter.colorchooser import askcolor

colors=['#000000','#FFFFFF','#FF0000','#00FF00','#0000FF','#FFFF00','#00FFFF','#FF00FF']
class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.place(x=0, y=0)

        # self.color_button = Button(self.root, text='color', command=self.choose_color)
        # self.color_button.place(x=50, y=0)

        self.color_button=[]
        for i in range(8):
            self.color_button=(Button(self.root,bg=colors[i],command=self.choose_color))
            self.color_button.place(x=i*10+30,y=10)
            i+=1

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.place(x=100,y=0)

        self.choose_size_button = Scale(self.root, from_=10, to=50, orient=HORIZONTAL)
        self.choose_size_button.place(x=150,y=0)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.place(x=0,y=100)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None
Paint()
