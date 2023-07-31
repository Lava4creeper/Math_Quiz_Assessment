# Import statements
from tkinter import *

# Define main menu class
class main_menu:
  #Upon initialisation
  def __init__(self):

    #Initialise variables
    description = "This is a brief description of how this program works."
    button_font = ("Arial", "8", "bold")
    button_fg = "#000000"
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
    with open("history.txt", "r") as history_file:
      history = [int(x) for x in history_file.readlines()]
    high_score = max(history)
    mean_score = round(sum(history) / len(history))
    history_file.close()
    selected_level = StringVar()
    selected_level.set("Input Quiz Level")
    print(selected_level.get())
    
    # Form a frame to place all elements on
    self.main_frame = Frame(padx=10, pady=10)
    self.main_frame.grid()

    # Create and place the heading of the page
    self.main_heading = Label(self.main_frame, text="Hello World", font=("Arial", "16", "bold"))
    self.main_heading.grid(row=0)

    # Create and place a brief description of the quiz
    self.main_description = Label(self.main_frame, text=description, wrap=250, width=40, justify="left")
    self.main_description.grid(row=1)

    # Create and place a frame to place the Instructions, Quiz Contents and Settings buttons within
    self.instructions_contents_settings_frame = Frame(self.main_frame)
    self.instructions_contents_settings_frame.grid(row=2)

    # Create and place an instructions button within the previously created frame
    self.instructions_button = Button(self.instructions_contents_settings_frame, 
                                     text="Instructions",
                                     bg="#A1E887",
                                     fg=button_fg,
                                     font=button_font,
                                     width=12,
                                     command=lambda: self.button_pressed("instructions", selected_level.get()))
    self.instructions_button.grid(row=0, column=0)

    # Create and place a Quiz Contents button within the previously created frame
    self.quiz_contents_button = Button(self.instructions_contents_settings_frame,
                                      text="Quiz Contents",
                                      bg="#A1E887",
                                      fg=button_fg,
                                      font=button_font,
                                      width=12,
                                      command=lambda: self.button_pressed("contents", selected_level.get()))
    self.quiz_contents_button.grid(row=0, column=1)

    # Create and place a settings button within the previously created frame
    self.settings_button = Button(self.instructions_contents_settings_frame,
                                 text="Settings",
                                 bg="#A1E887",
                                 fg=button_fg,
                                 font=button_font,
                                 width=12,
                                 command=lambda: self.button_pressed("settings", selected_level.get()))
    self.settings_button.grid(row=0, column=2)

    #Create and place a drop-down menu with the level options for the quiz
    self.level_input = OptionMenu(self.main_frame, selected_level, *level_options)
    self.level_input.config(bg="#A1E887", width=42, fg="#000000", font=("arial", "8", "bold"))
    self.level_input.grid(row=3)

    # Create and place a frame to place the quiz type buttons within
    self.quiz_type_frame = Frame(self.main_frame)
    self.quiz_type_frame.grid(row=4)

    # Create and place within the previously created frame a multiple choice button
    self.multiple_choice_button = Button(self.quiz_type_frame,
                                        text="Multiple Choice",
                                        bg="#A1E887",
                                        fg=button_fg,
                                        font=button_font,
                                        width=20,
                                        command=lambda: self.button_pressed("multiple choice", selected_level.get()))
    self.multiple_choice_button.grid(column=0, row=0)

    # Create and place within the previously created frame a typed input button
    self.typed_input_button = Button(self.quiz_type_frame,
                                    text="Typed Input",
                                    bg="#A1E887",
                                    fg=button_fg,
                                    font=button_font,
                                    width=20,
                                    state=DISABLED,
                                    command=lambda: self.button_pressed("typed input", selected_level.get()))
    self.typed_input_button.grid(column=1, row=0)

    # Create and place a Begin Quiz button]
    self.begin_quiz_button = Button(self.main_frame,
                                   text="Begin Quiz",
                                   bg="#80B192",
                                   fg=button_fg,
                                   font=("Arial", "30", "bold"),
                                   width=11,
                                   command=lambda: self.button_pressed("start", selected_level.get()))
    self.begin_quiz_button.grid(row=5)

    # Create and place a frame for the history and close buttons
    self.history_close_frame = Frame(self.main_frame)
    self.history_close_frame.grid(row=7, column=0)
    
    # Create and display a label with the highest and average scores
    self.high_score_display = Label(self.history_close_frame,
                               text="High Score: {}".format(high_score),
                               fg="#9C0000")
    self.high_score_display.grid(row=0, column=0)

    self.mean_score_display = Label(self.history_close_frame,
                               text="Average Score: {}".format(mean_score),
                               fg="#9C0000")
    self.mean_score_display.grid(row=0, column=1)


    # Create and place a history/export button within the previously created frame
    self.history_button = Button(self.history_close_frame,
                                text="History/Export",
                                bg="#A1E887",
                                fg=button_fg,
                                font=button_font,
                                width=20,
                                command=lambda: self.button_pressed("history", selected_level.get()))
    self.history_button.grid(row=1, column=0)

    # Create and place a Close button within the previously created frame
    self.close_button = Button(self.history_close_frame,
                                text="Close",
                                bg="#A1E887",
                                fg=button_fg,
                                font=button_font,
                                width=20,
                              command=lambda: self.button_pressed("close", selected_level.get()))
    self.close_button.grid(row=1, column=1)

  def button_pressed(self, button, level):
    print(button)
    if button == "multiple choice":
      self.multiple_choice_button.config(state=DISABLED)
      self.typed_input_button.config(state=NORMAL)
    elif button == "typed input":
      self.typed_input_button.config(state=DISABLED)
      self.multiple_choice_button.config(state=NORMAL)
    print(level)

#**************Main Routine******************

# Check that code has been run directly by the interpreter
if __name__ == "__main__":
  #Create, name and size the window
  window = Tk()
  window.title("Main Menu")
  window.geometry("360x300")
  #window.configure(bg="#6A8D92")
  # open main menu
  main_menu()
  window.mainloop()
