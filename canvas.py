from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import ai
from tkinter import filedialog as fd
im = None
tk_img = None
window=None
canvas=None
x1,y1=None,None
status=0
drawWidth = 5
eraseWidth=20
data=[]
def open():
    global im, tk_img
    fname = fd.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250,250,image=tk_img)
    window.update()
    
def process():
    global data,info2Lbl
    yeah = ai.score(data)
    print(1234)
    print(yeah)
    info2Lbl.config(text=yeah)
    print(1)
    
def draw(event):
    global x1,y1,data
    x1=event.x
    y1=event.y

    if status==0:
        canvas.create_line(x1,y1,x1+1,y1+1,width=drawWidth,fill="black")
    

def erase(event):
    global x1,y1
    x1=event.x
    y1=event.y
    if status==0:
        canvas.create_line(x1,y1,x1+1,y1+1,width=eraseWidth,fill=color[1])

def clearCanvas():
    if status==0:
        canvas.delete("all")

def nextBtnClick():
    global status
    if status==0:
        goToNext()

def goToNext():
    global infoLbl,status,posLbl,nextBtn
    if status==0:
        infoLbl.config(text="왼쪽 눈을 클릭하세요")
    elif status==1:
        infoLbl.config(text="오른쪽 눈를 클릭하세요")
    elif status==2:
        infoLbl.config(text="코를 클릭하세요")
    elif status==3:
        infoLbl.config(text="입을 클릭하세요")
    elif status==4:
        infoLbl.config(text="처리를 시작합니다")
        process()
    else:
        return
    status+=1
    posLbl.config(text="")
def click(e):
    global x1,y1
    x1=e.x
    y1=e.y
    if status==0:
        return
    else:
        data.append([x1,y1])
        tmp="("+str(x1)+","+str(y1)+")"
        posLbl.config(text=tmp)
        print(tmp)
        goToNext()
        
window=Tk()
window.title("스케치북")
window.geometry("700x720+100+100")
canvas=Canvas(window,width=700,height=600,bg="white")

canvas.place(x=0,y=20)

infoLbl=Label(window,text="좌클릭으로 그리기, 우클릭으로 지우기",fg="black")
infoLbl.place(x=0,y=0)

info2Lbl=Label(window,text="",fg="black")
info2Lbl.place(x=500,y=0)

posLbl=Label(window,text="",fg="black")
posLbl.place(x=600,y=700)

canvas.bind("<B1-Motion>",draw)
canvas.bind("<B3-Motion>",erase)

canvas.bind("<Button-1>",click)

clearBtn=Button(window,text="Clear",fg="black",bg="white",command=clearCanvas, font=("둥근모꼴",20))
clearBtn.place(x=10,y=650)

openBtn=Button(window,text="Open File",fg="black",bg="white",command=open, font=("둥근모꼴",20))
openBtn.place(x=300,y=650)

nextBtn=Button(window,text="Next",fg="black", bg="white",command=nextBtnClick,font=("둥근모꼴",20))
nextBtn.place(x=100,y=650)

window.mainloop()
