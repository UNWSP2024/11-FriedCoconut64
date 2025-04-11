import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("My favorite saying")
        self.info_button = tkinter.Button(self.main_window, text = 'Info', command=self.button_info)
        self.info_button.pack()
        self.button_quit = tkinter.Button(self.main_window, text = 'Quit', command=self.main_window.destroy)
        self.button_quit.pack()

        self.label = tkinter.Label(self.main_window)
        self.label.pack()

        tkinter.mainloop()

    def button_info(self):
        tkinter.messagebox.showinfo("Information", "Donovan Thompson, 2909 29th Ave NE")

if __name__ == '__main__':
    my_gui = MyGUI()

# Program #2, Donovan Thompson 4/10/2025
