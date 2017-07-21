from tkinter import Tk, Label, Button, StringVar, Canvas, PhotoImage
from urllib.request import urlopen
from PIL import Image, ImageTk
import io

class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

#        self.label_index = 0
#        self.label_text = StringVar()
#        self.label_text.set(self.LABEL_TEXT[self.label_index])
#        self.label = Label(master, textvariable=self.label_text)
#        self.label.bind("<Button-1>", self.cycle_label_text)
#        self.label.pack()

#        image_url = "https://www.barlaeus.nl/wp-content/uploads/2017/07/IMG_4526-1024x683.jpg"
#        path = io.BytesIO(urlopen(image_url).read())
#        pilimg = Image.open("IMG_4526-1024x683.jpg")
#        tkimg = ImageTk.PhotoImage(pilimg)
        tkimg = PhotoImage(file="deathstar.gif")

        self.image_label = Label(master, image = tkimg)
        self.image_label.image = tkimg
        self.image_label.pack(side = "bottom", fill = "both", expand = "yes")

#        self.canvas = Canvas(master, bg = "white", height=400, width=400)
#        self.canvas.create_image(10,10,image=tkimg, anchor="nw")
#        self.canvas.pack()

#        self.greet_button = Button(master, text="Greet", command=self.greet)
#        self.greet_button.pack()

#        self.close_button = Button(master, text="Close", command=master.quit)
#        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
