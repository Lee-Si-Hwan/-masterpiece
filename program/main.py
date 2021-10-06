import tkinter
import comparer
if __name__ == "__main__":
    print("Hello world!")
    filename = tkinter.filedialog.askopenfilename(initialdir="/",title="Choose image file",filetypes=("Image File",".png"))
    try:
        nearest = comparer.findNearestImg(filename)
    except:
        print("something is wierd@!!!")

    with open('Dataset/info/'+str(nearest)+'.txt') as desc:
        name = desc.readline()
        description = desc.readline()
        print('Name : '+name+', Description : '+description)
    print("Program FINISH")
