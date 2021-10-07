import tkinter
import model

name=None
description=None

root = tkinter.Tk()
root.title("Masterpiece")
root.geometry("700x100+10+10")

if __name__ == "__main__":
    print("Hello world!")
    filename = tkinter.filedialog.askopenfilename(initialdir=".",title="Choose image file",filetypes=[("Image File","*.png *.jpg *.jpeg *.jpe *.bmp *.dib *.pbm *.pgm *.ppm *.sr *.ras *.tiff *.tif")])
    nearest=None
    nearest = model.findNearest(filename)
    print(nearest)
    filename = f'Dataset/info/{nearest}.txt'
    try:
        with open(filename, encoding='utf-8') as desc:
            name = desc.readline()
            description = desc.readline()
            print('Name : '+name+', Description : '+description)
    except Exception as e:
        print("something is wierd@!!!")
        print(e)

    nameLabel = tkinter.Label(root, text=name)
    descLabel = tkinter.Label(root, text=description)
    
    nameLabel.place(x=20,y=10)
    descLabel.place(x=20, y=40)

    # originalImage = tkinter.PhotoImage(file=f"Dataset/data/{nearest}.jpg")
    # userImage = tkinter.PhotoImage(file=filename)

    # imgLabel1 = tkinter.Label(root, image=originalImage)
    # imgLabel2 = tkinter.Label(root, image=userImage)

    # imgLabel1.place(x=10, y=50)
    # imgLabel2.place(x=500, y=50)


root.mainloop()