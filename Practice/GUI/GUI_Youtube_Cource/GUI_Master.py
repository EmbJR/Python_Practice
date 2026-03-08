from tkinter import *
from tkinter import messagebox

class RootGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Master")
        self.root.geometry("600x600")
        self.root.config(bg="white")

class ComGUI():
    def __init__(self, root, serial):
        self.root = root
        self.serial = serial
        self.frame = LabelFrame(root, text="comm_manager", padx=5, pady=5, bg="White")
        self.Label_com = Label(self.frame, text = "Available Ports()", bg="White", width=10, anchor="w")
        self.Label_Bd = Label(self.frame, text="Baud Rate", bg = "White", width=10, anchor="w")
        
        self.Ref_Butt = Button(self.frame, text = "Refresh", bg="White", width=10, anchor="w", command=self.Refresh_btn_Cmd)
        self.Connect_Butt = Button(self.frame, text = "Connect", bg="White", width=10, anchor="w", state="disabled", command=self.serial_Connect)
        
        self.CommOptionMenu()
        self.BaudOptionMenu()

        self.Padx = 2
        self.Pady = 2

        self.publish()

    def CommOptionMenu(self):
        self.serial.getCommList()
        self.Clicked_Comm = StringVar()
        self.Clicked_Comm.set(self.serial.comm_List[0])
        self.CommMenu = OptionMenu(self.frame, self.Clicked_Comm, *self.serial.comm_List,
                                   command=self.Connect_Cntrl)
        self.CommMenu.config(width=10)

    def BaudOptionMenu(self):
        Baud = ["-",
                "9600", 
                "19200", 
                "38400", 
                "57600", 
                "115200"]
        self.Clickable_Baud = StringVar()
        self.Clickable_Baud.set(Baud[0])
        self.BaudOption_Menu = OptionMenu(self.frame,self.Clickable_Baud, *Baud,
                                          command=self.Connect_Cntrl)
        self.BaudOption_Menu.config(width=10)

    def Connect_Cntrl(self, other):
        print("Baud Rate Selected") 
        if "-" in self.Clicked_Comm.get() or "-" in self.Clickable_Baud.get():
            self.Connect_Butt["state"] = "disabled"
        else:
            self.Connect_Butt["state"] = "active"

    def Refresh_btn_Cmd(self):
        self.CommMenu.destroy()
        self.CommOptionMenu()
        self.CommMenu.grid(row=1, column=2, padx=self.Padx, pady = self.Pady)
        logoc = []
        self.Connect_Cntrl(logoc)
        print(self.serial.comm_List)

    def serial_Connect(self):
        
        if self.Connect_Butt["text"] == "Connect":
            self.serial.serialOpen(self)
            if self.serial.ser.status == True:
                self.BaudOption_Menu["state"] = "disabled"
                self.CommMenu["state"] = "disabled"
                self.Ref_Butt["state"] = "disabled"                
                self.Connect_Butt["text"] = "Disconnect"
                messagebox.showinfo("showinfo", "Connection Successful")
                print("comm opened") 
            else:
                messagebox.showerror("showerror", "Serial Port Connection failed")
        else:
            self.serial.serialClose()
            messagebox.showinfo("showinfo", "Connection Closed")
            self.Connect_Butt["text"] = "Connect"
            self.Ref_Butt["state"] = "active"
            self.BaudOption_Menu["state"] = "activ"
            self.CommMenu["state"] = "activ"                

    def publish(self):
        self.frame.grid(row=0, column=0, rowspan=2, columnspan=2, padx=self.Padx, pady = self.Pady)
        self.Label_com.grid(row=1, column=1, padx=self.Padx, pady = self.Pady)
        self.Label_Bd.grid(row=2, column=1, padx=self.Padx, pady = self.Pady)
        self.CommMenu.grid(row=1, column=2, padx=self.Padx, pady = self.Pady)
        self.BaudOption_Menu.grid(row=2, column=2,padx=self.Padx, pady = self.Pady)
        self.Ref_Butt.grid(row=1, column=3, padx=self.Padx, pady = self.Pady)
        self.Connect_Butt.grid(row=2, column=3, padx=self.Padx, pady = self.Pady)

    

if __name__ == "__main__":
    print("GUI Main Started")
    root_gui = RootGUI()
    ComGUI(root_gui.root)
    root_gui.root.mainloop()
    