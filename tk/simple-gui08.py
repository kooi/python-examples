from tkinter import Tk, Label, Button, StringVar, Canvas, PhotoImage
from urllib.request import urlopen
from PIL import Image, ImageTk
import io

class MyFirstGUI:

    IMAGE_URLS = [
        "https://www.barlaeus.nl/wp-content/uploads/2017/07/IMG_4526-1024x683.jpg",
        "http://49.media.tumblr.com/e73c640381ff1469f7679f84ceed2380/tumblr_o19mgh6T1Z1so5dgeo1_400.gif"
    ]

    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        master.bind("<Key>", self.print_key)
        master.bind("<Right>", self.cycle_image)

        self.image_index = 0
        path = io.BytesIO(urlopen(self.IMAGE_URLS[self.image_index]).read())
        pilimg = Image.open(path)
        tkimg = ImageTk.PhotoImage(pilimg)

        self.image_label = Label(master, image = tkimg)
        self.image_label.image = tkimg
        self.image_label.pack(side = "bottom", fill = "both", expand = "yes")

    def print_key(self, event):
        print(event.keysym)

    def cycle_image(self, event):
        print("key pressed")
        self.image_index += 1
        self.image_index %= len(self.IMAGE_URLS) # wrap around

        path = io.BytesIO(urlopen(self.IMAGE_URLS[self.image_index]).read())
        pilimg = Image.open(path)
        tkimg = ImageTk.PhotoImage(pilimg)

        self.image_label.configure(image = tkimg)
        self.image_label.image = tkimg

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
