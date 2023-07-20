from tkinter import *


class main_menu:

  def __init__(self):
    
    level_selected = ""
    description = "This is a brief description of how this program works."
    level_options = [
      "Year 1",
      "Year 2",
      "Year 3",
      "Year 4",
      "Year 5",
      "Year 6",
      "Year 7",
      "Year 8",
      "Year 9",
      "Year 10",
      "Year 11",
      "Year 12",
      "Year 13",
      "Custom"
    ]

    selected_level = StringVar()
    selected_level.set( "Input Quiz Level" )
    
    button_font = ("Arial", "8", "bold")
    button_fg = "#FFFFFF"
    
    self.main_frame = Frame(padx=10, pady=10)
    self.main_frame.grid()

    self.main_heading = Label(self.main_frame, text="Hello World", font=("Arial", "16", "bold"))
    self.main_heading.grid(row=0)

    
    self.main_description = Label(self.main_frame, text=description, wrap=250, width=40, justify="left")
    self.main_description.grid(row=1)

    self.button_frame = Frame(self.main_frame)
    self.button_frame.grid(row=2)

    self.instructions_button = Button(self.button_frame, 
                                     text="Instructions",
                                     bg="#990099",
                                     fg=button_fg,
                                     font=button_font,
                                     width=12)
    self.instructions_button.grid(row=0, column=0)

    self.quiz_contents_button = Button(self.button_frame,
                                      text="Quiz Contents",
                                      bg="#990099",
                                      fg=button_fg,
                                      font=button_font,
                                      width=12)
    self.quiz_contents_button.grid(row=0, column=1)

    self.settings_button = Button(self.button_frame,
                                 text="Instructions",
                                 bg="#990099",
                                 fg=button_fg,
                                 font=button_font,
                                 width=12)
    self.settings_button.grid(row=0, column=2)


    
    
    self.level_input = OptionMenu(self.main_frame, selected_level, *level_options)
    self.level_input.grid(row=3)
if __name__ == "__main__":
  window = Tk()
  window.title("Main Menu")
  window.geometry("430x900")
  main_menu()
  window.mainloop()
