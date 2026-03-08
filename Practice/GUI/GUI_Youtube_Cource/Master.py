from GUI_Master import RootGUI, ComGUI

RootMaster = RootGUI()

CommMaster = ComGUI(RootMaster.root)

RootMaster.root.mainloop()