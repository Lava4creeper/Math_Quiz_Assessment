from tkinter import *


class main_menu:

  def __init__(self):
    print("hello world")
    button_font = ("Arial", "12", "bold")
    button_fg = "#FFFFFF"
    self.main_frame = Frame(padx=10, pady=10)
    self.main_frame.grid()

    self.main_heading = Label(self.main_frame, text="Hello World", font=("Arial", "16", "bold"))
    self.main_heading.grid(row=0)
if __name__ == "__main__":
  window = Tk()
  window.title("Main Menu")
  window.geometry("430x900")
  main_menu()
  window.mainloop()
