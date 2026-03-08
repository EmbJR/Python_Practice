from GUI_Master import RootGUI, ComGUI
from Serial_Comm_Cntrl import serialCntrl

MySerialCntrl = serialCntrl()

RootMaster = RootGUI()

CommMaster = ComGUI(RootMaster.root, MySerialCntrl)

RootMaster.root.mainloop()