from tkinter import *

class RootGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Master")
        self.root.geometry("600x600")
        self.root.config(bg="white")

class ComGUI():
    def __init__(self, root):
        self.root = root
        self.frame = LabelFrame(root, text="comm_manager", padx=5, pady=5, bg="White")
        self.Label_com = Label(self.frame, text = "Available Ports()", bg="White", width=10, anchor="w")
        self.Label_Bd = Label(self.frame, text="Baud Rate", bg = "White", width=10, anchor="w")
        self.Ref_Butt = Button(self.frame, text = "Refresh", bg="White", width=10, anchor="w")
        self.Connect_Butt = Button(self.frame, text = "Connect", bg="White", width=10, anchor="w", state="disabled")
        
        self.CommOptionMenu()
        self.BaudOptionMenu()

        self.Padx = 2
        self.Pady = 2

        self.publish()

    def CommOptionMenu(self):
        comms = ["-", "COM1", "COM2", ]
        self.Clicked_Comm = StringVar()
        self.Clicked_Comm.set(comms[0])
        self.CommMenu = OptionMenu(self.frame, self.Clicked_Comm, *comms)
        self.CommMenu.config(width=10)

    def BaudOptionMenu(self):
        Baud = ["9600", 
                "19200", 
                "38400", 
                "57600", 
                "115200"]
        self.Clickable_Baud = StringVar()
        self.Clickable_Baud.set(Baud[0])
        self.BaudOption_Menu = OptionMenu(self.frame,self.Clickable_Baud, *Baud)
        self.BaudOption_Menu.config(width=10)

    def publish(self):
        self.frame.grid(row=0, column=0, rowspan=2, columnspan=2, padx=self.Padx, pady = self.Pady)
        self.Label_com.grid(row=1, column=1, padx=self.Padx, pady = self.Pady)
        self.Label_Bd.grid(row=2, column=1, padx=self.Padx, pady = self.Pady)
        self.CommMenu.grid(row=1, column=2, padx=self.Padx, pady = self.Pady)
        self.BaudOption_Menu.grid(row=2, column=2,padx=self.Padx, pady = self.Pady)
        self.Ref_Butt.grid(row=1, column=3, padx=self.Padx, pady = self.Pady)
        self.Connect_Butt.grid(row=2, column=3, padx=self.Padx, pady = self.Pady)

if __name__ == "__main__":
    RootGUI()
    ComGUI()