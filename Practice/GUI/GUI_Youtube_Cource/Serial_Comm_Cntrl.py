import serial.tools.list_ports


class serialCntrl():
    def __init__(self):
        self.comm_List = []
    
    def getCommList(self):
        ports = serial.tools.list_ports.comports()
        self.comm_List = [comm[0] for comm in ports]
        self.comm_List.insert(0, "-")

    def serialOpen(self, gui):
        print("Serial Connection try")
        self.ser = serial.Serial()
        
        try:
            if self.ser.is_open:
                self.ser.status = True
            else:
                #self.ser = serial.Serial()
                self.ser.baudrate = gui.Clickable_Baud.get()
                self.ser.port = gui.Clicked_Comm.get()
                self.ser.timeout = 1
                self.ser.open()
                self.ser.status = True
        except:
            self.ser.status = False

    def serialClose(self):
        try:
            self.ser.is_open
            self.ser.close()
            self.ser.status = False
        except:
            self.ser.status = False

        
                    

if __name__ == "__main__":
    MySerialCntrl = serialCntrl()
    print("Hello World")