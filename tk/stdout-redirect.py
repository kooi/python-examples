from tkinter import *

class CoreGUI(object):
    def __init__(self,parent):
        self.parent = parent
        self.InitUI()
        button = Button(self.parent, text="Start", command=self.main)
        button.grid(column=0, row=1, columnspan=2)

    def main(self):
        print('whatever')

    def InitUI(self):
        self.text_box = Text(self.parent, wrap='word', height = 11, width=50)
        self.text_box.grid(column=0, row=0, columnspan = 2, sticky='NSWE', padx=5, pady=5)
        sys.stdout = StdoutRedirector(self.text_box)

if __name__ == '__main__':
    root = Tk()
    gui = CoreGUI(root)
    root.mainloop()
