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
    high_scores = [0, 0, 0, 0]

    # Retrieve previous scores from file
    with open("files/Addition_scores.txt", "r") as history_file:
      addition_history = [int(x) for x in history_file.readlines()]
    with open("files/Subtraction_scores.txt", "r") as history_file:
      subtraction_history = [int(x) for x in history_file.readlines()]
    with open("files/Multiplication_scores.txt", "r") as history_file:
      multiplication_history = [int(x) for x in history_file.readlines()]
    with open("files/Division_scores.txt", "r") as history_file:
      division_history = [int(x) for x in history_file.readlines()]
      
    # Find the highest scores in each quiz type
    high_scores[0] = max(addition_history)
    high_scores[1] = max(subtraction_history)
    high_scores[2] = max(multiplication_history)
    high_scores[3] = max(division_history)

    # Find the highest score overall
    high_score = max(high_scores)

    # Check for empty 
    invalid_scores = 0
    if addition_history[0] == 0:
      invalid_scores += 1
    if subtraction_history[0] == 0:
      invalid_scores += 1
    if multiplication_history[0] == 0:
      invalid_scores += 1
    if division_history[0] == 0:
      invalid_scores += 1
      
    # Retrieve mean score
    try:
      mean_score = round((sum(addition_history) + sum(subtraction_history) + sum(multiplication_history) + sum(division_history)) / (len(addition_history) + len(subtraction_history) + len(multiplication_history) + len(division_history) - invalid_scores))
    except ZeroDivisionError:
      mean_score = 0
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

    # Create and place a frame to place the Instructions, Quiz Contents and Analytics buttons within
    self.instructions_contents_analytics_frame = Frame(self.main_frame)
    self.instructions_contents_analytics_frame.grid(row=2)

    # Create and place an instructions button within the previously created frame
    self.instructions_button = Button(
      self.instructions_contents_analytics_frame,
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
      self.instructions_contents_analytics_frame,
      text="Quiz Contents",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=12,
      command=lambda: self.button_pressed("contents", selected_level.get()))
    self.quiz_contents_button.grid(row=0, column=1)

    # Create and place a anaylytics button within the previously created frame
    self.analytics_button = Button(
      self.instructions_contents_analytics_frame,
      text="Analytics",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=12,
      command=lambda: self.button_pressed("analytics", selected_level.get()))
    self.analytics_button.grid(row=0, column=2)

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
    with open("files/settings.txt") as file:
      settings_list = [x for x in file.readlines()]
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
    with open("files/settings.txt", "r") as file:
      settings_list = file.readlines()

    settings_list[1] = "{}\n".format(level)
    with open("files/settings.txt", "w") as file:
      file.writelines(settings_list)

    if button == "instructions":
      self.main_window.destroy()
      instructions()
    elif button == "contents":
      self.main_window.destroy()
      contents()
    elif button == "analytics":
      self.main_window.destroy()
      analytics()
    elif button == "history":
      self.main_window.destroy()
      history()
    elif button == "start":
      #Check if user has chosen a quiz level; if they have go to the quiz, if not ask them to.
      if settings_list[1] != "Select a quiz type\n":
        self.main_window.destroy()
        quiz(level)
      else:
        self.error_label.config(text="Please select a quiz type")
    elif button == "close":
      # Close window without opening a new one
      self.main_window.destroy()
    #Invert state of buttons multiple choice and typed input
    elif button == "multiple choice" or button == "typed input":

      # assign first line of settings to the selected quiz type
      settings_list[0] = "quiz mode: {}\n".format(button)

      if button == "multiple choice":
        self.multiple_choice_button.config(state=DISABLED)
        self.typed_input_button.config(state=NORMAL)

      else:
        self.typed_input_button.config(state=DISABLED)
        self.multiple_choice_button.config(state=NORMAL)

      # assign first line of settings to the selected quiz type
      settings_list[0] = "quiz mode: {}\n".format(button)

      # write new settings list back to file
      with open("files/settings.txt", "w") as file:
        file.writelines(settings_list)


# Create instructions class
class instructions:

  def __init__(self):

    button = ""
    instructions = "Welcome to Maths Time! This is a collection of addition, subtraction, multiplication and division questions to test your maths ability and knowledge.\n\nAfter selecting a quiz type and either multiple choice or typed input, you can select 'Begin Quiz.' This will take you to your quiz.\n\nIf you have selected multiple choice, you will be given a question along with a selection of four possible answers. Simply click the answer you think is right, and you will receive immediate feedback.\n\nIf you have selected typed input, you will be given a question and a text box, which you must input your answer to and then press the submit button. You will then receive immediate feedback.\n\nUpon running out of time you will be allowed to finish the question you are on; you may also press the home button to end quiz. You will be returned to the home screen, and your score will be saved. You will then be able to see it from the history screen, where you will also be able to export all score data to a text document or clear the saved history. "
    self.instructions_window = Tk()
    self.instructions_window.title("Instructions")
    print("instructions")

    self.instructions_frame = Frame(padx=10, pady=10)
    self.instructions_frame.grid()

    self.instructions_title = Label(self.instructions_frame,
                                   text="Instructions",
                                   font=("Arial", "12", "bold"),
                                   width=20)
    self.instructions_title.grid(row=0)

    self.instructions_label = Label(self.instructions_frame,
                                   text=instructions,
                                    wrap=300,
                                   font=("Arial", "8", "bold"),
                                   width=50)
    self.instructions_label.grid(row=1)
    
    self.home_button = Button(self.instructions_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda: self.home_button_pressed("home"))
    self.home_button.grid(row=2)

  def home_button_pressed(self, button):
    if button == "home":
      self.instructions_window.destroy()
      main_menu()


# Create contents class
class contents:

  def __init__(self):

    contents = "This quiz can contain any combination of 1600 questions across the 4 operations that you can test yourself on. In addition and multiplication, the two numbers in the question will be between 1 and 20. In subtraction and division, the second term will always be between 1 and 20, and so will the answer."
    button = ""
    self.contents_window = Tk()
    self.contents_window.title("Contents")
    print("contents")

    self.contents_frame = Frame(padx=10, pady=10)
    self.contents_frame.grid()

    self.contents_title = Label(self.contents_frame, 
                               text="Contents",
                               font=("Arial", "12", "bold"),
                               width=20)
    self.contents_title.grid(row=0)

    self.contents_label = Label(self.contents_frame, 
                               text=contents,
                               font=("Arial", "8", "bold"),
                               width=40,
                               wrap=250)
    self.contents_label.grid(row=1)
    
    self.home_button = Button(self.contents_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda: self.home_button_pressed("home"))
    self.home_button.grid(row=2)

  def home_button_pressed(self, button):
    if button == "home":
      self.contents_window.destroy()
      main_menu()


# Create analytics class
class analytics:

  def __init__(self):

    button = ""
    self.analytics_window = Tk()
    self.analytics_window.title("Analytics")
    print("Analytics")

    self.analytics_frame = Frame(padx=10, pady=10)
    self.analytics_frame.grid()

    self.analytics_title = Label(self.analytics_frame,
                                text="Analytics",
                                font=("Arial", "12", "bold"),
                                padx=10, pady=10)
    self.analytics_title.grid(row=0)

    self.analytics_text = Label(self.analytics_frame,
                               text="Last 5 wrong answers:",
                               font=("Arial", "8", "bold"),
                               width=30)
    self.analytics_text.grid(row=1)

    self.error_one = Label(self.analytics_frame,
                          text="",
                          font=("Arial", "8", "bold"),
                          width=30)
    self.error_one.grid(row=2)
    
    self.error_two = Label(self.analytics_frame,
                          text="",
                          font=("Arial", "8", "bold"),
                          width=30)
    self.error_two.grid(row=3)
    
    self.error_three = Label(self.analytics_frame,
                          text="",
                          font=("Arial", "8", "bold"),
                          width=30)
    self.error_three.grid(row=4)
    
    self.error_four = Label(self.analytics_frame,
                          text="",
                          font=("Arial", "8", "bold"),
                          width=30)
    self.error_four.grid(row=5)
    
    self.error_five = Label(self.analytics_frame,
                          text="",
                          font=("Arial", "8", "bold"),
                          width=30)
    self.error_five.grid(row=6)
    
    self.error_label = Label(self.analytics_frame,
                            text="",
                            font=("Arial", "8", "bold"),
                            fg="#FF0000")
    self.error_label.grid(row=7)
    
    self.export_button = Button(self.analytics_frame,
                               text="Export",
                               bg="#A1E887",
                               fg="#000000",
                               font=("Arial", "8", "bold"),
                               width=20,
                               command=lambda:self.export_data("export"))
    self.export_button.grid(row=8)

    self.clear_button = Button(self.analytics_frame,
                              text="Clear",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda:self.clear_data("clear"))
    self.clear_button.grid(row=9)

    
    self.home_button = Button(self.analytics_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda: self.home_button_pressed("home"))
    self.home_button.grid(row=10)
    self.retrieve_errors()
  def retrieve_errors(self):
    with open("files/wrong_questions.txt", "r") as file:
      errors = []
      for x in file:
        x = x.strip()
        errors.append(x)
    errors.reverse()
    if errors[0] == "0":
      self.error_label.config(text="No data to show")
    else:
      try:
        self.error_one.config(text="{}".format(errors[0]))
        self.error_two.config(text="{}".format(errors[1]))
        self.error_three.config(text="{}".format(errors[2]))
        self.error_four.config(text="{}".format(errors[3]))
        self.error_five.config(text="{}".format(errors[4]))
      except IndexError:
        self.error_label.config(text="No further data to show")
    
  def export_data(self, button):
    if button == "export":
      with open("files/wrong_questions.txt", "r") as file:
        errors = file.readlines()
      errors.reverse()
      with open("exported_errors.txt", "w") as file:
        file.writelines("Past errors:\n\n")
        for x in errors:
          file.writelines(x)
        
        
  def clear_data(self, button):
    if button == "clear":
      with open("files/wrong_questions.txt", "w") as file:
        file.write("0")
      self.analytics_window.destroy()
      analytics()
  def home_button_pressed(self, button):
    if button == "home":
      self.analytics_window.destroy()
      main_menu()


# Create quiz class
class quiz:

  def __init__(self, level):

    # Initialise variables
    start_time = time.time()
    score = 0
    question = "question"
    with open("files/settings.txt", "r") as file:
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
                              command=lambda:self.send_home("home", score, settings_list))

    self.home_button.grid(row=10)
    self.generate_question(settings_list, start_time, score)

  def generate_question(self, settings_list, start_time, score):
    self.output_label.config(text="")
    red_herrings = [
      -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)

    if settings_list[1] == "Addition\n":
      number_3 = number_1 + number_2
      question_list = [number_2, "+", number_1, number_3]

    elif settings_list[1] == "Subtraction\n":
      if number_1 > number_2:
        number_3 = number_1 - number_2
        question_list = [number_1, "-", number_2, number_3]
      else:
        number_3 = number_2 - number_1
        question_list = [number_2, "-", number_1, number_3]

    elif settings_list[1] == "Multiplication\n":
      number_3 = number_1 * number_2
      question_list = [number_1, "x", number_2, number_3]

    elif settings_list[1] == "Division\n":
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
                                  state=NORMAL,)
      self.choice_button_2.config(command=lambda: self.check_answer(
        answers[1], question_list, settings_list, start_time, score),
                                  text="{}".format(answers[1]),
                                  state=NORMAL,)
      self.choice_button_3.config(command=lambda: self.check_answer(
        answers[2], question_list, settings_list, start_time, score),
                                  text="{}".format(answers[2]),
                                  state=NORMAL,)
      self.choice_button_4.config(command=lambda: self.check_answer(
        answers[3], question_list, settings_list, start_time, score),
                                  text="{}".format(answers[3]),
                                  state=NORMAL,)

    else:
      self.answer_entry.delete(0, END)
      self.submit_button.config(command=lambda: self.check_answer(
        self.answer_entry.get(), question_list, settings_list, start_time, score), state=NORMAL)

  def check_answer(self, submitted_answer, question_list, settings_list, start_time, score):
    print("here")
    try:
      if int(submitted_answer) == question_list[3]:
        print("Correct!")
        self.output_label.config(text="Correct!", fg="#008000")
        score += 1
        self.home_button.config(command=lambda:self.send_home("home", score, settings_list))
      else:
        with open("files/wrong_questions.txt", "r") as file:
          wrong_answers = file.readlines()
        if wrong_answers[0] == "0":
          with open("files/wrong_questions.txt", "w") as file:
            file.writelines("question: {} {} {} = {}. input: {}\n".format(question_list[0], question_list[1], question_list[2], question_list[3], submitted_answer))
        else:
          with open("files/wrong_questions.txt", "a") as file:
            file.write("question: {} {} {} = {}. input: {}\n".format(question_list[0], question_list[1], question_list[2], question_list[3], submitted_answer))
        print("incorrect. {} {} {} = {}".format(question_list[0],
                                                question_list[1],
                                                question_list[2],
                                                question_list[3]))
        self.output_label.config(fg="#FF0000", text="incorrect. {} {} {} = {}".format(question_list[0],
                                                question_list[1],
                                                question_list[2],
                                                question_list[3]))
      if settings_list[0] == "quiz mode: multiple choice\n":
        print("there")
        self.choice_button_1.config(state=DISABLED)
        self.choice_button_2.config(state=DISABLED)
        self.choice_button_3.config(state=DISABLED)
        self.choice_button_4.config(state=DISABLED)
      elif settings_list[0] == "quiz mode: typed input\n":
        self.submit_button.config(state=DISABLED)
      quiz_time = time.time() - start_time
      if quiz_time <= 60:
        self.quiz_frame.after(1500, lambda: self.generate_question(settings_list, start_time, score))
      else:
        self.quiz_frame.after(2500, self.output_label.config(fg="#FF0000", text="Time up! Score: {}".format(score)))
        self.quiz_frame.after(2500, lambda:self.send_home("home", score, settings_list))
    except ValueError:
      print("Invalid Value! Did you make a typo?")
      self.output_label.config(text="Invalid Value", fg="#FF0000")

  def send_home(self, button, score, settings_list):
    print(score)
    quiz_type = settings_list[1].strip()
    if score != 0:
      with open("files/{}_scores.txt".format(quiz_type), "r") as file:
        history_list = file.readlines()
      if history_list[0] != "0":
        with open("files/{}_scores.txt".format(quiz_type), "a") as file:
         file.write("\n{}".format(score))
      else:
        with open("files/{}_scores.txt".format(quiz_type), "w") as file:
          file.writelines("{}".format(score))
    if button == "home":
      self.quiz_window.destroy()
      main_menu()


# Create history class
class history:

  def __init__(self):

    button = ""
    self.history_window = Tk()
    self.history_window.title("History/Export")
    print("history")

    self.history_frame = Frame(padx=10, pady=10)
    self.history_frame.grid()

    self.title_label = Label(self.history_frame,
                             text="History",
                             font=("Arial", "12", "bold"),
                             fg="#000000")
    self.title_label.grid(row=0)

    self.score_frame = Frame(self.history_frame, padx=10, pady=10)
    self.score_frame.grid(row=1)

    self.addition_title = Label(self.score_frame, text="Addition\nScores:", font=("Arial", "8", "bold"), fg="#000000")
    self.addition_title.grid(row=0, column=0)

    self.subtraction_title = Label(self.score_frame, text="Subtraction\nScores:", font=("Arial", "8", "bold"), fg="#000000")
    self.subtraction_title.grid(row=0, column=1)

    self.multiplication_title = Label(self.score_frame, text="Multiplication\nScores:", font=("Arial", "8", "bold"), fg="#000000")    
    self.multiplication_title.grid(row=0, column=2)
    
    self.division_title = Label(self.score_frame, text="Division\nScores:", font=("Arial", "8", "bold"), fg="#000000")  
    self.division_title.grid(row=0, column=3)

    self.addition_score_one = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.addition_score_one.grid(row=1, column=0)
    
    self.addition_score_two = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.addition_score_two.grid(row=2, column=0)
    
    self.addition_score_three = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.addition_score_three.grid(row=3, column=0)
    
    self.addition_score_four = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.addition_score_four.grid(row=4, column=0)
    
    self.subtraction_score_one = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.subtraction_score_one.grid(row=1, column=1)
    
    self.subtraction_score_two = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.subtraction_score_two.grid(row=2, column=1)
    
    self.subtraction_score_three = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.subtraction_score_three.grid(row=3, column=1)
    
    self.subtraction_score_four = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.subtraction_score_four.grid(row=4, column=1)
    
    self.multiplication_score_one = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.multiplication_score_one.grid(row=1, column=2)
    
    self.multiplication_score_two = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.multiplication_score_two.grid(row=2, column=2)
    
    self.multiplication_score_three = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.multiplication_score_three.grid(row=3, column=2)
    
    self.multiplication_score_four = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.multiplication_score_four.grid(row=4, column=2)
    
    self.division_score_one = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.division_score_one.grid(row=1, column=3)
    
    self.division_score_two = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.division_score_two.grid(row=2, column=3)
    
    self.division_score_three = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.division_score_three.grid(row=3, column=3)
    
    self.division_score_four = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.division_score_four.grid(row=4, column=3)

    self.high_score_label = Label(self.score_frame, text="High scores:", font=("Arial", "12", "bold"))
    self.high_score_label.grid(row=5, columnspan=4)
    
    self.high_score_a = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.high_score_a.grid(row=6, column=0)

    self.high_score_s = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.high_score_s.grid(row=6, column=1)

    self.high_score_m = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.high_score_m.grid(row=6, column=2)

    self.high_score_d = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.high_score_d.grid(row=6, column=3)

    self.button_frame = Frame(self.history_frame, padx=10, pady=10)
    self.button_frame.grid(row=2)

    self.export_button = Button(self.button_frame, 
                               text="Export",
                               bg="#A1E887",
                               fg="#000000",
                               font=("Arial", "8", "bold"),
                               width=10,
                               command=lambda:self.export_history("export"))
    self.export_button.grid(row=0, column=0)

    self.clear_button = Button(self.button_frame,
                               text="Clear",
                               bg="#A1E887",
                               fg="#000000",
                               font=("Arial", "8", "bold"),
                               width=10,
                               command=lambda:self.clear_history("clear"))
    self.clear_button.grid(row=0, column=1)
    
    self.home_button = Button(self.button_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=10,
                              command=lambda:self.home_button_pressed("home"))
    self.home_button.grid(row=0, column=2)

    self.retrieve_scores()

  def retrieve_scores(self):
    # Set up system to retrieve scores from history file
    with open("files/Addition_scores.txt", "r") as history_file:
      addition_history = [int(x) for x in history_file.readlines()]
    with open("files/Subtraction_scores.txt", "r") as history_file:
      subtraction_history = [int(x) for x in history_file.readlines()]
    with open("files/Multiplication_scores.txt", "r") as history_file:
      multiplication_history = [int(x) for x in history_file.readlines()]
    with open("files/Division_scores.txt", "r") as history_file:
      division_history = [int(x) for x in history_file.readlines()]

    addition_history.reverse()
    subtraction_history.reverse()
    multiplication_history.reverse()
    division_history.reverse()

    #Set scores to output
    try:
      self.addition_score_one.config(text=addition_history[0])    
      self.addition_score_two.config(text=addition_history[1])    
      self.addition_score_three.config(text=addition_history[2])
      self.addition_score_four.config(text=addition_history[3])
    except IndexError:
      pass
    try:
      self.subtraction_score_one.config(text=subtraction_history[0])
      self.subtraction_score_two.config(text=subtraction_history[1])
      self.subtraction_score_three.config(text=subtraction_history[2])
      self.subtraction_score_four.config(text=subtraction_history[3])
    except IndexError:
      pass
    try: 
      self.multiplication_score_one.config(text=multiplication_history[0])
      self.multiplication_score_two.config(text=multiplication_history[1])
      self.multiplication_score_three.config(text=multiplication_history[2])
      self.multiplication_score_four.config(text=multiplication_history[3])
    except IndexError:
      pass
    try:
      self.division_score_one.config(text=division_history[0])
      self.division_score_two.config(text=division_history[1])
      self.division_score_three.config(text=division_history[2])
      self.division_score_four.config(text=division_history[3])
    except IndexError:
      pass

    self.high_score_a.config(text=max(addition_history))
    self.high_score_s.config(text=max(subtraction_history))
    self.high_score_m.config(text=max(multiplication_history))
    self.high_score_d.config(text=max(division_history))

  def export_history(self, button):
    if button == "export":
      with open("files/Addition_scores.txt", "r") as file:
        scores_a = [int(x) for x in file.readlines()]
      with open("files/Subtraction_scores.txt", "r") as file:
        scores_s = [int(x) for x in file.readlines()]
      with open("files/Multiplication_scores.txt", "r") as file:
        scores_m = [int(x) for x in file.readlines()]
      with open("files/Division_scores.txt", "r") as file:
        scores_d = [int(x) for x in file.readlines()]

      scores_a.reverse()
      scores_s.reverse()
      scores_m.reverse()
      scores_d.reverse()
      
      with open("exported_scores.txt", "w") as file:
        file.writelines("Addition Scores:")
        for x in scores_a:
          file.writelines("\n{}".format(x))
        file.writelines("\n\nSubtraction Scores:")
        for x in scores_s:
          file.writelines("\n{}".format(x))
        file.writelines("\n\nMultiplication Scores:")
        for x in scores_m:
          file.writelines("\n{}".format(x))
        file.writelines("\n\nDivision Scores:")
        for x in scores_d:
          file.writelines("\n{}".format(x))
  
  def clear_history(self, button):
    if button == "clear":
      with open("files/Addition_scores.txt", "w") as file:
        file.write("0")
      with open("files/Subtraction_scores.txt", "w") as file:
        file.write("0")
      with open("files/Multiplication_scores.txt", "w") as file:
        file.write("0")
      with open("files/Division_scores.txt", "w") as file:
        file.write("0")
      self.history_window.destroy()
      history()
  
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
