from tkinter import *

# self.app.configure(background="#d9d9d9") // light mode
# self.app.configure(background="#142433") // bluedeep
# self.app.configure(background="#36393b") // secondary

app = Tk()

class Application():
    def __init__(self):
        self.app = app
        self.appConf()
        app.mainloop()
    def appConf(self):
        self.app.title("Smart Point Flow")
        self.app.geometry("1400x860")
        self.app.configure(background="#1a1a1b")
        self.app.maxsize(1940, 1080)
        self.app.minsize(860, 520)

Application()