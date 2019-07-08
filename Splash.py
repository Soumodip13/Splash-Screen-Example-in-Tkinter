import tkinter as tk
import time

from PIL import ImageTk, Image


class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Splash")
        self.geometry("600x700")
        path = "img.jpg"

        # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        img = ImageTk.PhotoImage(Image.open(path))

        # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
        panel = tk.Label(self, image=img)

        # The Pack geometry manager packs widgets in rows or columns.
        panel.pack(side="bottom", fill="both", expand="yes")

        # required to make window show before the program gets to the mainloop
        self.update()


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.withdraw()
        splash = Splash(self)

        # setup stuff goes here
        self.title("Main")
        # simulate a delay while loading
        # delays loading for 3 seconds
        time.sleep(3)

        # finished loading so destroy splash
        splash.destroy()

        # show window again
        self.deiconify()


if __name__ == "__main__":
    app = App()
    app.mainloop()