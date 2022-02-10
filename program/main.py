import tkinter
import tkinter.ttk as ttk
import model
import os
import matplotlib
from matplotlib import pyplot as plt
from PIL import ImageTk, Image
import histogram

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
nowDir = os.path.dirname(__file__)

class customCheckButton(ttk.Checkbutton):
    def deselect(self):
        self.var.set(0)

    def select(self):
        self.var.set(1)

class VerticalNavigationToolbar2Tk(NavigationToolbar2Tk):
    def __init__(self, canvas, window):
      super().__init__(canvas, window, pack_toolbar=False)

    # override _set_image_for_button for avoiding error
    def _set_image_for_button(self, button):
        if button._image_file is None:
            return
        size = button.winfo_pixels('18p')
        with Image.open(button._image_file.replace('.png', '_large.png')
                        if size > 24 else button._image_file) as im:
            image = ImageTk.PhotoImage(im.resize((size, size)), master=self)
        button.configure(image=image)
        button._ntimage = image  # Prevent garbage collection.
    
    # override _Button() to re-pack the toolbar button in vertical direction
    def _Button(self, text, image_file, toggle, command):
        if not toggle:
            b = ttk.Button(master=self, text=text, command=command)
        else:
            var = tkinter.IntVar(master=self)
            b = customCheckButton(
                master=self, text=text, command=command, variable=var)
            b.var = var
        b._image_file = image_file
        if image_file is not None:
            # Explicit class because ToolbarTk calls _Button.
            self._set_image_for_button(b)
        else:
            b.configure(font=self._label_font)
        b.pack(side=tkinter.TOP) # re-pack button in vertical direction
        return b

    # override _Spacer() to create vertical separator
    def _Spacer(self):
      s = ttk.Frame(self, width=26, relief=tkinter.RIDGE)
      s.pack(side=tkinter.TOP, pady=5) # pack in vertical direction
      return s

    # disable showing mouse position in toolbar
    def set_message(self, s):
        pass

# make everything in one class
class Main:
    def openImageBtnDialog(self):
        self.userFilename = tkinter.filedialog.askopenfilename(initialdir=os.path.join(nowDir,'testData'),title="Choose image file",filetypes=[("Image File","*.png *.jpg *.jpeg *.jpe *.bmp *.dib *.pbm *.pgm *.ppm *.sr *.ras *.tiff *.tif")])
        image = Image.open(self.userFilename)
        image = image.resize((150,150*image.height//image.width))
        self.userImageImage=ImageTk.PhotoImage(image)
        self.userImage.config(image=self.userImageImage)
    

    def makeComparingHist(self, data, to_compare, channel):
        fig = plt.figure()
        hist = histogram.load(os.path.join(nowDir,f'Dataset/compare/{to_compare}.histogram'))
        
        for x in range(1,10):
            subplot = fig.add_subplot(3,3,x)
            # remove legend of subplot
            subplot.legend_ = None
            subplot.plot(hist['histogram'][channel][x-1],color="g", label="masterpiece")
            subplot.plot(data[channel][x-1],color="b", label="user")
        return fig
    

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Masterpiece")
        self.root.geometry("1000x700+10+10")

        self.big_frame = ttk.Frame(self.root)
        self.big_frame.pack(fill="both", expand=True)

        print(os.path.join(nowDir,"Theme\\sun_valley.tcl"))
        self.root.tk.call("source", os.path.join(nowDir,"Theme\\sun-valley.tcl"))
        self.root.tk.call("set_theme", "light")

        selectImageBtn = ttk.Button(self.big_frame, text="Select Image", command=self.openImageBtnDialog)
        selectImageBtn.place(x=160, y=10)
        testModelBtn = ttk.Button(self.big_frame, text="Test Model", command=self.testModel)
        testModelBtn.place(x=160, y=45)
        
        self.userImage = ttk.Label(self.big_frame)
        self.userImage.place(x=10, y=10)


        self.listFrame = ttk.Frame(self.big_frame, width=700, height=90)
        self.listFrame.place(x=260, y=10)

        infoFrame = ttk.Frame(self.big_frame, width=700, height=60)
        infoFrame.place(x=260, y=140)
        self.nameInfo = ttk.Label(infoFrame, text="")
        self.nameInfo.place(x=10, y=0)
        self.descInfo = ttk.Label(infoFrame, text="")
        self.descInfo.place(x=10, y=20)
        self.yearInfo = ttk.Label(infoFrame, text="")
        self.yearInfo.place(x=10, y=40)
        self.percentInfo = ttk.Label(infoFrame)
        self.percentInfo.place(x=350, y=0)
        

        self.graphFrame = ttk.Frame(self.big_frame, width=500, height=400)
        self.graphFrame.place(x=260, y=200)

        self.getImageInfo()
        self.root.mainloop()

    def getImageInfo(self): #get information of all images
        self.informations={}
        with open(os.path.join(nowDir,"Dataset/info/info.csv"),'r',encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.split(',')
                self.informations[int(line[0])]=line[1:]

    def showInformation(self,rankNumber):
        self.nameInfo.config(text=self.informations[self.rank[rankNumber][0]][0])
        self.descInfo.config(text=self.informations[self.rank[rankNumber][0]][1])
        self.yearInfo.config(text=self.informations[self.rank[rankNumber][0]][2])
        self.percentInfo.config(text=f"Hue : {self.rank[rankNumber][2]}%\nSaturation : {self.rank[rankNumber][3]}%\nValue : {self.rank[rankNumber][4]}%")

        try:
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
        except:
            pass
        fig = self.makeComparingHist(self.test_hist,self.rank[rankNumber][0],0)

        self.canvas = FigureCanvasTkAgg(fig, master=self.graphFrame)
        self.canvas.draw()

        self.toolbar = VerticalNavigationToolbar2Tk(self.canvas, self.graphFrame)
        self.toolbar.update()
        
        self.canvas.mpl_connect("key_press_event", key_press_handler)
        self.canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH,expand=1)
        self.toolbar.pack(side=tkinter.LEFT,fill=tkinter.Y)

    def testModel(self):
        for widget in self.listFrame.winfo_children():
            widget.destroy()
        img = model.load_image(self.userFilename)
        self.test_hist = model.make_histogram(img)
        self.rank = model.predict(self.test_hist[0], self.test_hist[1], self.test_hist[2])
        self.images = list()
        for i in range(7):
            btn = ttk.Button(self.listFrame, text=f"{i+1}", command=lambda k=i: self.showInformation(k))
            image = Image.open(os.path.join(nowDir,f"Dataset/data/{self.rank[i][0]}.jpg"))
            image2 = ImageTk.PhotoImage(image.resize((80,80*image.height//image.width)))
            self.images.append(image2)
            
            btn.config(image=self.images[i])
            btn.pack(side=tkinter.LEFT)



if __name__ == "__main__":
    main = Main()