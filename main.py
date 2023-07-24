from tkinter import *

class main_menu:

  def __init__(self):
    
    level_selected = ""
    description = "This is a brief description of how this program works."
    button_font = ("Arial", "8", "bold")
    button_fg = "#000000"
    high_score = 0
    mean_score = 0
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
    
    self.main_frame = Frame(padx=10, pady=10)
    self.main_frame.grid()

    self.main_heading = Label(self.main_frame, text="Hello World", font=("Arial", "16", "bold"))
    self.main_heading.grid(row=0)

    
    self.main_description = Label(self.main_frame, text=description, wrap=250, width=40, justify="left")
    self.main_description.grid(row=1)

    self.button_frame = Frame(self.main_frame)
    self.button_frame.grid(row=2)

    self.quiz_type_frame = Frame(self.main_frame)
    self.quiz_type_frame.grid(row=4)

    self.history_close_frame = Frame(self.main_frame)
    self.history_close_frame.grid(row=7)

    self.instructions_button = Button(self.button_frame, 
                                     text="Instructions",
                                     bg="#A1E887",
                                     fg=button_fg,
                                     font=button_font,
                                     width=12)
    self.instructions_button.grid(row=0, column=0)

    self.quiz_contents_button = Button(self.button_frame,
                                      text="Quiz Contents",
                                      bg="#A1E887",
                                      fg=button_fg,
                                      font=button_font,
                                      width=12)
    self.quiz_contents_button.grid(row=0, column=1)

    self.settings_button = Button(self.button_frame,
                                 text="Settings",
                                 bg="#A1E887",
                                 fg=button_fg,
                                 font=button_font,
                                 width=12)
    self.settings_button.grid(row=0, column=2)
    
    self.level_input = OptionMenu(self.main_frame, selected_level, *level_options,)
    self.level_input.config(bg="#A1E887", width=42, fg="#000000", font=("arial", "8", "bold"))
    self.level_input.grid(row=3)

    self.multiple_choice_button = Button(self.quiz_type_frame,
                                        text="Multiple Choice",
                                        bg="#A1E887",
                                        fg=button_fg,
                                        font=button_font,
                                        width=20)
    self.multiple_choice_button.grid(column=0, row=0)

    self.typed_input_button = Button(self.quiz_type_frame,
                                    text="Typed Input",
                                    bg="#A1E887",
                                    fg=button_fg,
                                    font=button_font,
                                    width=20,
                                    state=DISABLED)
    self.typed_input_button.grid(column=1, row=0)

    self.begin_quiz_button = Button(self.main_frame,
                                   text="Begin Quiz",
                                   bg="#80B192",
                                   fg=button_fg,
                                   font=("Arial", "30", "bold"),
                                   width=11)
    self.begin_quiz_button.grid(row=5)

    self.scores_display = Label(self.main_frame,
                               text="High Score: {}        Average Score: {}".format(high_score, mean_score),
                               fg="#9C0000")
    self.scores_display.grid(row=6)

    self.history_button = Button(self.history_close_frame,
                                text="History/Export",
                                bg="#A1E887",
                                fg=button_fg,
                                font=button_font,
                                width=20)
    self.history_button.grid(row=0, column=0)

    self.close_button = Button(self.history_close_frame,
                                text="Close",
                                bg="#A1E887",
                                fg=button_fg,
                                font=button_font,
                                width=20)
    self.close_button.grid(row=0, column=1)
    
if __name__ == "__main__":
  window = Tk()
  window.title("Main Menu")
  window.geometry("430x900")
  # indow.configure(bg="#6A8D92")
  main_menu()
  window.mainloop()
