import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("My favorite saying")

        self.label = tkinter.Label(self.main_window, text = 'Another Day, Another Dollar')
        self.label.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()

# Program #1, Donovan Thompson 4/10/2025
