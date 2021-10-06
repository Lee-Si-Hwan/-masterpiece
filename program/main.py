import tkinter
import comparer
if __name__ == "__main__":
    print("Hello world!")
    filename = tkinter.filedialog.askopenfilename(initialdir="/",title="Choose image file",filetypes=[("Image File","*.png *.jpg *.jpeg *.jpe *.bmp *.dib *.pbm *.pgm *.ppm *.sr *.ras *.tiff *.tif")])
    nearest=None
    print(filename)
    try:
        nearest = comparer.findNearestImg(filename)

        with open('Dataset/info/'+str(nearest)+'.txt') as desc:
            name = desc.readline()
            description = desc.readline()
            print('Name : '+name+', Description : '+description)
        print("Program FINISH")
    except Exception as e:
        print("something is wierd@!!!")
        print(e)

input()