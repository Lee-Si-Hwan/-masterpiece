import tkinter
import tkinter.ttk as ttk
from turtle import bgcolor
import model
import os
import matplotlib
from PIL import ImageTk, Image
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
userFilename='D:\\Programming\\-masterpiece\\program\\testData\\1.1.png'
nowDir = os.path.dirname(__file__)




# make everything in one class
class Main:
    def openImageBtnDialog(self):
        self.userFilename = tkinter.filedialog.askopenfilename(initialdir=".",title="Choose image file",filetypes=[("Image File","*.png *.jpg *.jpeg *.jpe *.bmp *.dib *.pbm *.pgm *.ppm *.sr *.ras *.tiff *.tif")])
        image = Image.open(self.userFilename)
        image = image.resize((150,150*image.height//image.width))
        self.userImageImage=ImageTk.PhotoImage(image)
        self.userImage.config(image=self.userImageImage)

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Masterpiece")
        self.root.geometry("1000x600+10+10")

        self.big_frame = ttk.Frame(self.root)
        self.big_frame.pack(fill="both", expand=True)

        print(os.path.join(nowDir,"Theme\\sun_valley.tcl"))
        self.root.tk.call("source", os.path.join(nowDir,"Theme\\sun-valley.tcl"))
        self.root.tk.call("set_theme", "light")

        selectImageBtn = ttk.Button(self.big_frame, text="Select Image", command=self.openImageBtnDialog)
        selectImageBtn.place(x=160, y=10)
        testModelBtn = ttk.Button(self.big_frame, text="Test Model", command=self.testModel)
        testModelBtn.place(x=160, y=45)
        
        self.graphFrame = ttk.Frame(self.big_frame, width=500, height=400)
        self.graphFrame.place(x=260, y=250)

        infoFrame = ttk.Frame(self.big_frame, width=700, height=100)
        infoFrame.place(x=260, y=120)

        self.listFrame = ttk.Frame(self.big_frame, width=700, height=100)
        self.listFrame.place(x=260, y=10)

        self.nameInfo = ttk.Label(infoFrame, text="")
        self.nameInfo.place(x=10, y=10)
        self.descInfo = ttk.Label(infoFrame, text="")
        self.descInfo.place(x=10, y=40)

        self.userImage = ttk.Label(self.big_frame)
        self.userImage.place(x=10, y=10)

        self.root.mainloop()

    def getInfo(self,x):
        filename = os.path.join(model.datasetDir,f'info/{x}.txt')
        with open(filename, encoding='utf-8') as desc:
                name = desc.readline()
                description = desc.readline()
                return name,description

    def showInformation(self,i):
        self.nameInfo.config(text=self.informations[i][0])
        self.descInfo.config(text=self.informations[i][1])
        try: 
            self.canvas.get_tk_widget().destroy()
        except:
            pass
        

    def testModel(self):

        data = model.findNearest(userFilename)
        
        self.informations=list()
        self.images = list()
        for i in range(7):
            self.informations.append(self.getInfo(data[i][2]))
            btn = ttk.Button(self.listFrame, text=f"{i+1}", command=lambda i=i: self.showInformation(i))
            image = Image.open(os.path.join(model.datasetDir,f"data\\{data[i][2]}.jpg"))
            image2 = ImageTk.PhotoImage(image.resize((80,80*image.height//image.width)))
            self.images.append(image2)
            btn.config(image=self.images[i])
            btn.pack(side=tkinter.LEFT)
        # fig = model.drawResult(data)
        # canvas = FigureCanvasTkAgg(fig, master=self.graphFrame)
        # canvas.draw()
        # toolbar = NavigationToolbar2Tk(canvas, self.graphFrame, pack_toolbar=True)
        # toolbar.update()

        # canvas.mpl_connect("key_press_event", key_press_handler)
        
        # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH)


if __name__ == "__main__":
    main = Main()