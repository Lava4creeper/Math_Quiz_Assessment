# Import statements
from tkinter import *
import random
import time


# Define main menu class
class main_menu:
  #Upon initialisation
  def __init__(self):

    #Create, name and size the window
    self.main_window = Tk()
    self.main_window.title("Main Menu")
    self.main_window.geometry("360x320")

    #Initialise and assign variables and lists
    description = "Welcome to Maths Time! This game is designed to help you develop your maths skills and abilities through quizzes."
    button_font = ("Arial", "8", "bold")
    button_fg = "#000000"
    selected_level = StringVar()
    selected_level.set("Select a quiz type")
    level_options = ["Addition", "Subtraction", "Multiplication", "Division"]

    # Set up system to retrieve scores from history file
    with open("history.txt", "r") as history_file:
      history = [int(x) for x in history_file.readlines()]
    # Retrieve high score
    high_score = max(history)
    # Retrieve mean score
    mean_score = round(sum(history) / len(history))

    # Form a frame to place all elements on
    self.main_frame = Frame(padx=10, pady=10)
    self.main_frame.grid()

    # Create and place the heading of the page
    self.main_heading = Label(self.main_frame,
                              text="Maths time!",
                              font=("Arial", "16", "bold"))
    self.main_heading.grid(row=0)

    # Create and place a brief description of the quiz
    self.main_description = Label(self.main_frame,
                                  text=description,
                                  wrap=250,
                                  width=40,
                                  justify="left")
    self.main_description.grid(row=1)

    # Create and place a frame to place the Instructions, Quiz Contents and Settings buttons within
    self.instructions_contents_settings_frame = Frame(self.main_frame)
    self.instructions_contents_settings_frame.grid(row=2)

    # Create and place an instructions button within the previously created frame
    self.instructions_button = Button(
      self.instructions_contents_settings_frame,
      text="Instructions",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=12,
      command=lambda: self.button_pressed("instructions", selected_level.get()
                                          ))
    self.instructions_button.grid(row=0, column=0)

    # Create and place a Quiz Contents button within the previously created frame
    self.quiz_contents_button = Button(
      self.instructions_contents_settings_frame,
      text="Quiz Contents",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=12,
      command=lambda: self.button_pressed("contents", selected_level.get()))
    self.quiz_contents_button.grid(row=0, column=1)

    # Create and place a settings button within the previously created frame
    self.settings_button = Button(
      self.instructions_contents_settings_frame,
      text="Settings",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=12,
      command=lambda: self.button_pressed("settings", selected_level.get()))
    self.settings_button.grid(row=0, column=2)

    #Create and place a drop-down menu with the level options for the quiz
    self.level_input = OptionMenu(self.main_frame, selected_level,
                                  *level_options)
    self.level_input.config(bg="#A1E887",
                            width=42,
                            fg="#000000",
                            font=("arial", "8", "bold"))
    self.level_input.grid(row=3)

    # Create and place a frame to place the quiz type buttons within
    self.quiz_type_frame = Frame(self.main_frame)
    self.quiz_type_frame.grid(row=4)

    # Create and place within the previously created frame a multiple choice button
    self.multiple_choice_button = Button(
      self.quiz_type_frame,
      text="Multiple Choice",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=20,
      command=lambda: self.button_pressed("multiple choice",
                                          selected_level.get()))
    self.multiple_choice_button.grid(column=0, row=0)

    # Create and place within the previously created frame a typed input button
    self.typed_input_button = Button(
      self.quiz_type_frame,
      text="Typed Input",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=20,
      command=lambda: self.button_pressed("typed input", selected_level.get()))
    self.typed_input_button.grid(column=1, row=0)

    # Check what quiz type was last selected and disable that button
    with open("settings.txt") as file:
      settings_list = file.readlines()
    if settings_list[0] == "quiz mode: multiple choice\n":
      self.multiple_choice_button.config(state=DISABLED)
    elif settings_list[0] == "quiz mode: typed input\n":
      self.typed_input_button.config(state=DISABLED)

    # Create and place a Begin Quiz button]
    self.begin_quiz_button = Button(
      self.main_frame,
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

    # Create and display a label with the high score
    self.high_score_display = Label(self.history_close_frame,
                                    text="High Score: {}".format(high_score),
                                    fg="#9C0000")
    self.high_score_display.grid(row=0, column=0)

    # Create and display a label with the mean score
    self.mean_score_display = Label(
      self.history_close_frame,
      text="Average Score: {}".format(mean_score),
      fg="#9C0000")
    self.mean_score_display.grid(row=0, column=1)

    # Create and place a history/export button within the previously created frame
    self.history_button = Button(
      self.history_close_frame,
      text="History/Export",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=20,
      command=lambda: self.button_pressed("history", selected_level.get()))
    self.history_button.grid(row=1, column=0)

    # Create and place a Close button within the previously created frame
    self.close_button = Button(
      self.history_close_frame,
      text="Close",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=20,
      command=lambda: self.button_pressed("close", selected_level.get()))
    self.close_button.grid(row=1, column=1)

    #Set up an output that will tell the user to select a level if they haven't
    self.error_label = Label(self.main_frame,
                             text="",
                             font=("Arial", "10"),
                             fg="#FF0000")
    self.error_label.grid(row=8)

  #Set up a function to output commands based on what button's been pressed
  def button_pressed(self, button, level):
    #Nested if statements in order to determine the button pressed, destroy the main window and send the program to the appropriate class
    with open("settings.txt", "r") as file:
      settings_list = [x for x in file.readlines()]

    settings_list[1] = "level selected: {}\n".format(level)
    with open("settings.txt", "w") as file:
      file.writelines(settings_list)

    if button == "instructions":
      self.main_window.destroy()
      instructions()
    elif button == "contents":
      self.main_window.destroy()
      contents()
    elif button == "settings":
      self.main_window.destroy()
      settings()
    elif button == "history":
      self.main_window.destroy()
      history()
    elif button == "start":
      #Check if user has chosen a quiz level; if they have go to the quiz, if not ask them to.
      if settings_list[1] != "level selected: Select a quiz type\n":
        self.main_window.destroy()
        quiz(level)
      else:
        self.error_label.config(text="Please select a level")
    elif button == "close":
      # Close window without opening a new one
      self.main_window.destroy()
    #Invert state of buttons multiple choice and typed input
    elif button == "multiple choice" or button == "typed input":

      # assign first line of settings to the selected quiz type
      settings_list[0] = "quiz mode: {}\n".format(button)

      # write new settings list back to file
      with open("settings.txt", "w") as file:
        file.writelines(settings_list)

      if button == "multiple choice":
        self.multiple_choice_button.config(state=DISABLED)
        self.typed_input_button.config(state=NORMAL)

      else:
        self.typed_input_button.config(state=DISABLED)
        self.multiple_choice_button.config(state=NORMAL)

      # assign first line of settings to the selected quiz type
      settings_list[0] = "quiz mode: {}\n".format(button)

      # write new settings list back to file
      with open("settings.txt", "w") as file:
        file.writelines(settings_list)


# Create instructions class
class instructions:

  def __init__(self):

    button = ""
    self.instructions_window = Tk()
    print("instructions")

    self.instructions_frame = Frame(padx=10, pady=10)
    self.instructions_frame.grid()

    self.home_button = Button(self.instructions_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda: self.home_button_pressed("home"))
    self.home_button.grid(row=0)

  def home_button_pressed(self, button):
    if button == "home":
      self.instructions_window.destroy()
      main_menu()


# Create contents class
class contents:

  def __init__(self):

    button = ""
    self.contents_window = Tk()
    print("contents")

    self.contents_frame = Frame(padx=10, pady=10)
    self.contents_frame.grid()

    self.home_button = Button(self.contents_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda: self.home_button_pressed("home"))
    self.home_button.grid(row=0)

  def home_button_pressed(self, button):
    if button == "home":
      self.contents_window.destroy()
      main_menu()


# Create settings class
class settings:

  def __init__(self):

    button = ""
    self.settings_window = Tk()
    print("instructions")

    self.settings_frame = Frame(padx=10, pady=10)
    self.settings_frame.grid()

    self.home_button = Button(self.settings_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda: self.home_button_pressed("home"))
    self.home_button.grid(row=0)

  def home_button_pressed(self, button):
    if button == "home":
      self.settings_window.destroy()
      main_menu()


# Create quiz class
class quiz:

  def __init__(self, level):

    # Initialise variables
    start_time = time.time()
    score = 0
    question = "question"
    with open("settings.txt", "r") as file:
      settings_list = [x for x in file.readlines()]
    #Create window
    self.quiz_window = Tk()
    self.quiz_window.title("Quiz")
    #self.quiz_window.geometry("360x320")

    #Create frame to place elements in
    self.quiz_frame = Frame(padx=10, pady=10)
    self.quiz_frame.grid()

    #Create label to place question in
    self.question_label = Label(self.quiz_frame,
                                text=question,
                                wrap=250,
                                width=10,
                                height=2,
                                justify="left",
                                font=("arial", "20", "bold"))
    self.question_label.grid(row=0)

    with open("settings.txt", "r") as file:
      settings_list = [x for x in file.readlines()]

    if settings_list[0] == "quiz mode: multiple choice\n":
      self.choice_button_1 = Button(self.quiz_frame,
                                    text="option one",
                                    bg="#A1E887",
                                    fg="#000000",
                                    font=("Arial", "8", "bold"),
                                    width=20)
      self.choice_button_1.grid(row=1)

      self.choice_button_2 = Button(self.quiz_frame,
                                    text="option two",
                                    bg="#A1E887",
                                    fg="#000000",
                                    font=("Arial", "8", "bold"),
                                    width=20)
      self.choice_button_2.grid(row=2)

      self.choice_button_3 = Button(self.quiz_frame,
                                    text="option three",
                                    bg="#A1E887",
                                    fg="#000000",
                                    font=("Arial", "8", "bold"),
                                    width=20)
      self.choice_button_3.grid(row=3)

      self.choice_button_4 = Button(self.quiz_frame,
                                    text="option four",
                                    bg="#A1E887",
                                    fg="#000000",
                                    font=("Arial", "8", "bold"),
                                    width=20)
      self.choice_button_4.grid(row=4)
      
      self.output_label = Label(self.quiz_frame,
                           text="",
                           font=("Arial", "8", "bold"),
                           fg="#000000")
      self.output_label.grid(row=5)

    else:
      self.answer_entry = Entry(self.quiz_frame,
                                bg="#FFFFFF",
                                font=("Arial", "8", "bold"),
                                fg="#000000",
                                width=20)
      self.answer_entry.grid(row=1)

      self.output_label = Label(self.quiz_frame,
                           text="",
                           font=("Arial", "8", "bold"),
                           fg="#000000")
      self.output_label.grid(row=2)

      self.submit_button = Button(self.quiz_frame,
                                  text="Submit",
                                  bg="#A1E887",
                                  fg="#000000",
                                  font=("Arial", "8", "bold"),
                                  width=20)
      self.submit_button.grid(row=3)

    
    self.home_button = Button(self.quiz_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda:self.home_button_pressed("home"))

    self.home_button.grid(row=10)
    self.generate_question(settings_list, start_time, score)

  def generate_question(self, settings_list, start_time, score):
    self.output_label.config(text="")
    red_herrings = [
      -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)

    if settings_list[1] == "level selected: Addition\n":
      number_3 = number_1 + number_2
      question_list = [number_2, "+", number_1, number_3]

    elif settings_list[1] == "level selected: Subtraction\n":
      if number_1 > number_2:
        number_3 = number_1 - number_2
        question_list = [number_1, "-", number_2, number_3]
      else:
        number_3 = number_2 - number_1
        question_list = [number_2, "-", number_1, number_3]

    elif settings_list[1] == "level selected: Multiplication\n":
      number_3 = number_1 * number_2
      question_list = [number_1, "x", number_2, number_3]

    elif settings_list[1] == "level selected: Division\n":
      number_3 = number_1 * number_2
      question_list = [number_3, "÷", number_2, number_1]

    self.question_label.config(text="{} {} {} = ?".format(
      question_list[0], question_list[1], question_list[2]))

    print(question_list)
    if settings_list[0] == "quiz mode: multiple choice\n":
      random.shuffle(red_herrings)
      answers = [
        question_list[3], question_list[3] + red_herrings[0],
        question_list[3] + red_herrings[1], question_list[3] + red_herrings[2]
      ]
      random.shuffle(answers)

      self.choice_button_1.config(command=lambda: self.check_answer(
        answers[0], question_list, settings_list, start_time, score),
                                  text="{}".format(answers[0]),
                                  state=NORMAL)
      self.choice_button_2.config(command=lambda: self.check_answer(
        answers[1], question_list, settings_list, start_time, score),
                                  text="{}".format(answers[1]),
                                  state=NORMAL)
      self.choice_button_3.config(command=lambda: self.check_answer(
        answers[2], question_list, settings_list, start_time, score),
                                  text="{}".format(answers[2]),
                                  state=NORMAL)
      self.choice_button_4.config(command=lambda: self.check_answer(
        answers[3], question_list, settings_list, start_time, score),
                                  text="{}".format(answers[3]),
                                  state=NORMAL)

    else:
      self.answer_entry.delete(0, END)
      self.submit_button.config(command=lambda: self.check_answer(
        self.answer_entry.get(), question_list, settings_list, start_time, score), state=NORMAL)

  def check_answer(self, submitted_answer, question_list, settings_list, start_time, score):
    if settings_list[0] == "quiz type: multiple choice\n":    
      self.choice_button_1.config(state=DISABLED)
      self.choice_button_2.config(state=DISABLED)
      self.choice_button_3.config(state=DISABLED)
      self.choice_button_4.config(state=DISABLED)
    elif settings_list[0] == "quiz type: typed input\n":
      self.submit_button.config(state=DISABLED)

    try:
      if int(submitted_answer) == question_list[3]:
        print("Correct!")
        self.output_label.config(text="Correct!", fg="#008000")
        score += 1
      else:
        print("incorrect. {} {} {} = {}".format(question_list[0],
                                                question_list[1],
                                                question_list[2],
                                                question_list[3]))
        self.output_label.config(fg="#FF0000", text="incorrect. {} {} {} = {}".format(question_list[0],
                                                question_list[1],
                                                question_list[2],
                                                question_list[3]))
      quiz_time = time.time() - start_time
      if quiz_time <= 20:
        self.quiz_frame.after(2500, lambda: self.generate_question(settings_list, start_time, score))
      else:
        with open("history.txt", "r") as file:
          history_list = file.readlines()
          print(history_list)
        if history_list[0] != "0\n":
          with open("history.txt", "a") as file:
           file.write("\n{}".format(score))
        else:
          with open("history.txt", "w") as file:
            file.writelines("{}".format(score))
        self.quiz_frame.after(2500, self.output_label.config(fg="#FF0000", text="Time up! Score: {}".format(score)))
        #self.output_label.config(fg="#FF0000", text="Time up! Score: {}".format(score))
        self.quiz_frame.after(2500, lambda:self.home_button_pressed("home"))
        #self.home_button_pressed("home")
    except ValueError:
      print("Invalid Value! Did you make a typo?")
      self.output_label.config(text="Invalid Value", fg="#FF0000")

  def home_button_pressed(self, button):
    if button == "home":
      self.quiz_window.destroy()
      main_menu()


# Create history class
class history:

  def __init__(self):

    button = ""
    self.history_window = Tk()
    print("history")

    self.history_frame = Frame(padx=10, pady=10)
    self.history_frame.grid()

    self.home_button = Button(self.history_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda: self.home_button_pressed("home"))
    self.home_button.grid(row=0)

  def home_button_pressed(self, button):
    if button == "home":
      self.history_window.destroy()
      main_menu()


#**************Main Routine******************

# Check that code has been run directly by the interpreter
if __name__ == "__main__":

  #window.configure(bg="#6A8D92")
  # open main menu
  main_menu()

#self.quiz_box.after(2500, lambda: self.quiz_box.destroy())
