from tkinter import *

class RootGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Master")
        self.root.geometry("1024x600")
        self.root.config(bg="Grey")


if __name__ == "__main__":
    RootGUI()