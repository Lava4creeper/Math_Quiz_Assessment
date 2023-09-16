# Import statements
from tkinter import *
import random
import time


# Create main menu class
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

    # Check for empty score lists so they can be ignored when calculating mean score
    invalid_scores = 0
    if addition_history[0] == 0:
      invalid_scores += 1
    if subtraction_history[0] == 0:
      invalid_scores += 1
    if multiplication_history[0] == 0:
      invalid_scores += 1
    if division_history[0] == 0:
      invalid_scores += 1
      
    # Attempt to calculate the mean score by adding every score, then dividing by the amount of scores saved minus the amount of empty lists
    try:
      mean_score = round((sum(addition_history) + sum(subtraction_history) + sum(multiplication_history) + sum(division_history)) / (len(addition_history) + len(subtraction_history) + len(multiplication_history) + len(division_history) - invalid_scores))
    # If there are no scores finding the mean score will be dividing by zero which will throw an error; catch that error and set mean score to zero.
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
    self.first_button_frame = Frame(self.main_frame)
    self.first_button_frame.grid(row=2)

    # Create and place an instructions button within the frame
    self.instructions_button = Button(self.first_button_frame,
      text="Instructions",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=12,
      command=lambda: self.button_pressed("instructions", selected_level.get()))
    self.instructions_button.grid(row=0, column=0)

    # Create and place a Quiz Contents button within the frame
    self.quiz_contents_button = Button(self.first_button_frame,
      text="Quiz Contents",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=12,
      command=lambda: self.button_pressed("contents", selected_level.get()))
    self.quiz_contents_button.grid(row=0, column=1)

    # Create and place a anaylytics button within the frame
    self.analytics_button = Button(self.first_button_frame,
      text="Analytics",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=12,
      command=lambda: self.button_pressed("analytics", selected_level.get()))
    self.analytics_button.grid(row=0, column=2)

    #Create, configure and place a drop-down menu with the type options for the quiz
    self.level_input = OptionMenu(self.main_frame, selected_level, *level_options)
    self.level_input.config(bg="#A1E887",
                            width=42,
                            fg="#000000",
                            font=("arial", "8", "bold"))
    self.level_input.grid(row=3)

    # Create and place a frame to place the quiz type buttons within
    self.quiz_type_frame = Frame(self.main_frame)
    self.quiz_type_frame.grid(row=4)

    # Create and place within the frame a multiple choice button
    self.multiple_choice_button = Button(self.quiz_type_frame,
      text="Multiple Choice",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=20,
      command=lambda: self.button_pressed("multiple choice",
                                          selected_level.get()))
    self.multiple_choice_button.grid(column=0, row=0)

    # Create and place within the frame a typed input button
    self.typed_input_button = Button(self.quiz_type_frame,
      text="Typed Input",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=20,
      command=lambda: self.button_pressed("typed input", selected_level.get()))
    self.typed_input_button.grid(column=1, row=0)

    # Retrieve a list of settings
    with open("files/settings.txt") as file:
      settings_list = file.readlines()
    # If the quiz type is currently multiple choice, disable that button
    if settings_list[0] == "quiz mode: multiple choice\n":
      self.multiple_choice_button.config(state=DISABLED)
    # If the quiz type is currently typede input, disable that button
    elif settings_list[0] == "quiz mode: typed input\n":
      self.typed_input_button.config(state=DISABLED)

    # Create and place a Begin Quiz button
    self.begin_quiz_button = Button(self.main_frame,
      text="Begin Quiz",
      bg="#80B192",
      fg=button_fg,
      font=("Arial", "30", "bold"),
      width=11,
      command=lambda: self.button_pressed("start", selected_level.get()))
    self.begin_quiz_button.grid(row=5)

    # Create and place a frame for the history and close buttons
    self.second_button_frame = Frame(self.main_frame)
    self.second_button_frame.grid(row=7, column=0)

    # Create and display a label with the high score
    self.high_score_display = Label(self.second_button_frame,
                                    text="High Score: {}".format(high_score),
                                    fg="#9C0000")
    self.high_score_display.grid(row=0, column=0)

    # Create and display a label with the mean score
    self.mean_score_display = Label(self.second_button_frame,
      text="Average Score: {}".format(mean_score),
      fg="#9C0000")
    self.mean_score_display.grid(row=0, column=1)

    # Create and place a history button within the previously created frame
    self.history_button = Button(self.second_button_frame,
      text="History",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=20,
      command=lambda: self.button_pressed("history", selected_level.get()))
    self.history_button.grid(row=1, column=0)

    # Create and place a Close button
    self.close_button = Button(self.second_button_frame,
      text="Close",
      bg="#A1E887",
      fg=button_fg,
      font=button_font,
      width=20,
      command=lambda: self.button_pressed("close", selected_level.get()))
    self.close_button.grid(row=1, column=1)

    # Create and place an output that will remind the user to select a level
    self.error_label = Label(self.main_frame,
                             text="",
                             font=("Arial", "10"),
                             fg="#FF0000")
    self.error_label.grid(row=8)

  # Create a function to output commands based on what button's been pressed
  def button_pressed(self, button, level):
    # Retrieve settings list
    with open("files/settings.txt", "r") as file:
      settings_list = file.readlines()

    # Set quiz type to the selected one from the dropdown
    settings_list[1] = "{}\n".format(level)

    # Write new settings back to the file
    with open("files/settings.txt", "w") as file:
      file.writelines(settings_list)

    #Set of if statements sensing which button was pressed to send the user to the right place
    
    # If intructions button was pressed, destroy window and open the instructions window
    if button == "instructions":
      self.main_window.destroy()
      instructions()
      
    # If contents button was pressed, destroy the window and open the contents window
    elif button == "contents":
      self.main_window.destroy()
      contents()
      
    # If analytics button was pressed, destroy the window and open the anayltics window
    elif button == "analytics":
      self.main_window.destroy()
      analytics()
      
    # If history button was pressed, destroy the window and open the history window
    elif button == "history":
      self.main_window.destroy()
      history()
      
    # If begin quiz button was pressed
    elif button == "start":
      #Check if user has chosen a quiz level; if they have go to the quiz, if not ask them to.
      if settings_list[1] != "Select a quiz type\n":
        self.main_window.destroy()
        quiz(level)
      else:
        self.error_label.config(text="Please select a quiz type")
        
    # If close button pressed
    elif button == "close":
      # Close window
      self.main_window.destroy()
      
    # If multiple choice or typed input button was pressed
    elif button == "multiple choice" or button == "typed input":

      # assign first line of settings to the selected quiz mode
      settings_list[0] = "quiz mode: {}\n".format(button)

      # Disable the active button, and enable the inactive button
      if button == "multiple choice":
        self.multiple_choice_button.config(state=DISABLED)
        self.typed_input_button.config(state=NORMAL)
      else:
        self.typed_input_button.config(state=DISABLED)
        self.multiple_choice_button.config(state=NORMAL)

      # write new settings list back to file
      with open("files/settings.txt", "w") as file:
        file.writelines(settings_list)


# Create instructions class
class instructions:
  # Upon initialisation
  def __init__(self):
    # Create instructions block of text
    instructions = "Welcome to Maths Time! This is a collection of addition, subtraction, multiplication and division questions to test your maths ability and knowledge.\n\nAfter selecting a quiz type and either multiple choice or typed input, you can select 'Begin Quiz.' This will take you to your quiz.\n\nIf you have selected multiple choice, you will be given a question along with a selection of four possible answers. Simply click the answer you think is right, and you will receive immediate feedback.\n\nIf you have selected typed input, you will be given a question and a text box, which you must input your answer to and then press the submit button. You will then receive immediate feedback.\n\nUpon running out of time you will be allowed to finish the question you are on; you may also press the home button to end quiz. You will be returned to the home screen, and your score will be saved. You will then be able to see it from the history screen, where you will also be able to export all score data to a text document or clear the saved history. "

    # Create and name the instructions window
    self.instructions_window = Tk()   
    self.instructions_window.title("Instructions")

    # Create a frame to place elements within
    self.instructions_frame = Frame(padx=10, pady=10)
    self.instructions_frame.grid()

    # Create the title of the instructions page
    self.instructions_title = Label(self.instructions_frame,
                                   text="Instructions",
                                   font=("Arial", "12", "bold"),
                                   width=20)
    self.instructions_title.grid(row=0)

    # Create the label to place the previous block of text in
    self.instructions_label = Label(self.instructions_frame,
                                   text=instructions,
                                    wrap=300,
                                   font=("Arial", "8", "bold"),
                                   width=50)
    self.instructions_label.grid(row=1)

    # Create the home button
    self.home_button = Button(self.instructions_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda: self.home_button_pressed("home"))
    self.home_button.grid(row=2)

  # Create the function to send the user to the main menu
  def home_button_pressed(self, button):
    # Check the function is being called from the home button being pressed
    if button == "home":
      #Destroy the window and send the user to the main menu
      self.instructions_window.destroy()
      main_menu()


# Create contents class
class contents:
  # Upon initialisation
  def __init__(self):
    # Create block of text to show the user
    contents = "This quiz can contain any combination of 1600 questions across the 4 operations that you can test yourself on. In addition and multiplication, the two numbers in the question will be between 1 and 20. In subtraction and division, the second term will always be between 1 and 20, and so will the answer."

    # Create and name the contents window
    self.contents_window = Tk()
    self.contents_window.title("Contents")

    # Create a frame to place elements in
    self.contents_frame = Frame(padx=10, pady=10)
    self.contents_frame.grid()

    # Create the title of the contents page
    self.contents_title = Label(self.contents_frame, 
                               text="Contents",
                               font=("Arial", "12", "bold"),
                               width=20)
    self.contents_title.grid(row=0)

    # Create a label to display the block of text seen previously
    self.contents_label = Label(self.contents_frame, 
                               text=contents,
                               font=("Arial", "8", "bold"),
                               width=40,
                               wrap=250)
    self.contents_label.grid(row=1)

    # Create a home button
    self.home_button = Button(self.contents_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda: self.home_button_pressed("home"))
    self.home_button.grid(row=2)

  # Create a function for when the home button is pressed
  def home_button_pressed(self, button):
    # Check the function is being called because the home button was pressed
    if button == "home":
      # Destroy the window and send the user to the main menu
      self.contents_window.destroy()
      main_menu()


# Create analytics class
class analytics:
  # Upon initialisation
  def __init__(self):

    # Create and title analytics window
    self.analytics_window = Tk()
    self.analytics_window.title("Analytics")

    # Create a frame to place elements within
    self.analytics_frame = Frame(padx=10, pady=10)
    self.analytics_frame.grid()

    # Create a title for the analytics window
    self.analytics_title = Label(self.analytics_frame,
                                text="Analytics",
                                font=("Arial", "12", "bold"),
                                padx=10, pady=10)
    self.analytics_title.grid(row=0)

    # Create a label to inform the user the last 5 wrong answers are displayed
    self.analytics_text = Label(self.analytics_frame,
                               text="Last 5 wrong answers:",
                               font=("Arial", "8", "bold"),
                               width=30)
    self.analytics_text.grid(row=1)

    # Create five labels that will show the last 5 scores; upon creation these will be blank
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

    # Create a label to inform the user when there is less than 5 errors to display
    self.error_label = Label(self.analytics_frame,
                            text="",
                            font=("Arial", "8", "bold"),
                            fg="#FF0000")
    self.error_label.grid(row=7)

    # Create a button to export data
    self.export_button = Button(self.analytics_frame,
                               text="Export",
                               bg="#A1E887",
                               fg="#000000",
                               font=("Arial", "8", "bold"),
                               width=20,
                               command=lambda:self.export_data("export"))
    self.export_button.grid(row=8)

    # Create a button to clear data
    self.clear_button = Button(self.analytics_frame,
                              text="Clear",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda:self.clear_data("clear"))
    self.clear_button.grid(row=9)

    # Create a button to send the user to the main menu
    self.home_button = Button(self.analytics_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda: self.home_button_pressed("home"))
    self.home_button.grid(row=10)

    # Call the retrieve errors function
    self.retrieve_errors()

  # Create a function to retrieve errors
  def retrieve_errors(self):
    # Place past errors into a list from file
    with open("files/wrong_answers.txt", "r") as file:
      errors = []
      # When placing items into list remove new line characters
      for x in file:
        x = x.strip()
        errors.append(x)
    # Reverse the order of the errors list to place most recent errors at the beginning of the list
    errors.reverse()
    # Check if there are any errors saved
    if errors[0] == "0":
      # If there are no scores saved, inform the user
      self.error_label.config(text="No data to show")
    else:
      # If there are scores saved, attempt to place 5 most recent scores into the 5 labels
      try:
        self.error_one.config(text="{}".format(errors[0]))
        self.error_two.config(text="{}".format(errors[1]))
        self.error_three.config(text="{}".format(errors[2]))
        self.error_four.config(text="{}".format(errors[3]))
        self.error_five.config(text="{}".format(errors[4]))
      # If there are less than 5 scores to display, inform the user
      except IndexError:
        self.error_label.config(text="No further data to show")

  # Create a function to export data
  def export_data(self, button):
    # Check that the function was called when the export button was pressed
    if button == "export":
      # Retrieve past errors and place them in a list
      with open("files/wrong_answers.txt", "r") as file:
        errors = file.readlines()
      # Reverse list order so it is from most recent to least recent
      errors.reverse()
      # Create or edit the exported errors file with the current saved errors
      with open("exported_errors.txt", "w") as file:
        file.writelines("Past errors:\n\n")
        for x in errors:
          file.writelines(x)

  # Create a function to clear data
  def clear_data(self, button):
    # Check the function was called by the clear button being pressed
    if button == "clear":
      # Overwrite the wrong questions file with a "0"
      with open("files/wrong_answers.txt", "w") as file:
        file.write("0")
      # Destroy the window and call the class again; this has the effect of refreshing the screen
      self.analytics_window.destroy()
      analytics()

  # Create a function to send the user to the main menu
  def home_button_pressed(self, button):
    # Check the function was called when the user pressed the home button
    if button == "home":
      # Destroy the window and send the user to the main menu 
      self.analytics_window.destroy()
      main_menu()


      
# Create quiz class
class quiz:
  # Upon initialisation
  def __init__(self, level):

    # Initialise variables
    score = 0
    question = "question"
    # Retrieve settings list from file
    with open("files/settings.txt", "r") as file:
      settings_list = [x for x in file.readlines()]
    # Measure the current time
    start_time = time.time()
    
    #Create and title quiz window
    self.quiz_window = Tk()
    self.quiz_window.title("Quiz")

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

    # Check whether quiz type is multiple choice or typed input
    if settings_list[0] == "quiz mode: multiple choice\n":
      # If quiz mode is multiple choice
      # Create four buttons with potential answers
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

      # Create a label to provide feedback to the user
      self.output_label = Label(self.quiz_frame,
                           text="",
                           font=("Arial", "8", "bold"),
                           fg="#000000")
      self.output_label.grid(row=5)

    else:
      # If quiz mode is typed input
      # Create a text box the user can type into
      self.answer_entry = Entry(self.quiz_frame,
                                bg="#FFFFFF",
                                font=("Arial", "8", "bold"),
                                fg="#000000",
                                width=20)
      self.answer_entry.grid(row=1)

      # Create a label to provide feedback to the user - this is done above in multiple choice but is redone here because in typed input there is an element below it, so it cannot be shared between quiz modes
      self.output_label = Label(self.quiz_frame,
                           text="",
                           font=("Arial", "8", "bold"),
                           fg="#000000")
      self.output_label.grid(row=2)

      # Create a submit button for the user
      self.submit_button = Button(self.quiz_frame,
                                  text="Submit",
                                  bg="#A1E887",
                                  fg="#000000",
                                  font=("Arial", "8", "bold"),
                                  width=20)
      self.submit_button.grid(row=3)

    # Create a button to send the user to main menu
    self.home_button = Button(self.quiz_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=20,
                              command=lambda:self.send_home("home", score, settings_list))
    self.home_button.grid(row=10)

    # Generate the first question
    self.generate_question(settings_list, start_time, score)

  # Create a function to generate questions
  def generate_question(self, settings_list, start_time, score):
    # Make sure the output label is set to blank
    self.output_label.config(text="")
     # Initialise variables including two random integers between 1 and 20
    red_herrings = [
      -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    ]
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)

    # Check for quiz type and generate a question using the two previously generated integers and the quiz type
    # If the quiz type is addition, add the two numbers together. The question will be first number + second number
    if settings_list[1] == "Addition\n":
      number_3 = number_1 + number_2
      question_list = [number_2, "+", number_1, number_3]

    # If the quiz type is subtraction, subtract the smaller one from the larger one. The question will be larger - smaller
    elif settings_list[1] == "Subtraction\n":
      if number_1 > number_2:
        number_3 = number_1 - number_2
        question_list = [number_1, "-", number_2, number_3]
      else:
        number_3 = number_2 - number_1
        question_list = [number_2, "-", number_1, number_3]

    # If the quiz type is multiplication, multiply the two numbers. The question will be first number x second number
    elif settings_list[1] == "Multiplication\n":
      number_3 = number_1 * number_2
      question_list = [number_1, "x", number_2, number_3]

    # If the quiz type is division, multiply the two numbers. The question will be product ÷ second number
    elif settings_list[1] == "Division\n":
      number_3 = number_1 * number_2
      question_list = [number_3, "÷", number_2, number_1]

    # Output the question
    self.question_label.config(text="{} {} {} = ?".format(
      question_list[0], question_list[1], question_list[2]))

    # If the quiz mode is multiple choice, generate three distinct false answers within ± 10 of the original by shuffling the red herrings list
    if settings_list[0] == "quiz mode: multiple choice\n":
      random.shuffle(red_herrings)
      answers = [
        question_list[3], question_list[3] + red_herrings[0],
        question_list[3] + red_herrings[1], question_list[3] + red_herrings[2]
      ]
      # Shuffle the answers so they are shown in a random order
      random.shuffle(answers)

      # Make the four generated answers the text of the answer buttons, make their command check answer with the parameters of the current answer and enable them
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

    # If quiz mode is typed input
    else:
      # Clear the answer box
      self.answer_entry.delete(0, END)
      # Make the submit button call check answer with the parameters of the current text box content
      self.submit_button.config(command=lambda: self.check_answer(self.answer_entry.get(), question_list, settings_list, start_time, score), state=NORMAL)

  # Create a function to check answers
  def check_answer(self, submitted_answer, question_list, settings_list, start_time, score):
    # Check answer assuming it is an integer
    try:
      # Compare the submitted answer to the correct answer
      # If submitted answer is correct
      if int(submitted_answer) == question_list[3]:
        # Inform the user they are correct
        self.output_label.config(text="Correct!", fg="#008000")
        # Increase score by one
        score += 1
        # Update home button command with current score in case it is pressed
        self.home_button.config(command=lambda:self.send_home("home", score, settings_list))
      # If submitted answer is incorrect
      else:
        # save current saved wrong answers to a list
        with open("files/wrong_answers.txt", "r") as file:
          wrong_answers = file.readlines()
        # If wrong answers list is currently empty
        if wrong_answers[0] == "0":
          # Overwrite contents of wrong answers with submitted answer
          with open("files/wrong_answers.txt", "w") as file:
            file.writelines("question: {} {} {} = {}. input: {}\n".format(question_list[0], question_list[1], question_list[2], question_list[3], submitted_answer))
        # If wrong answers list is not empty
        else:
          # Append wrong answers file with submitted answer
          with open("files/wrong_answers.txt", "a") as file:
            file.write("question: {} {} {} = {}. input: {}\n".format(question_list[0], question_list[1], question_list[2], question_list[3], submitted_answer))
            # Inform the user they were incorrect and inform them of the correct answer
        self.output_label.config(fg="#FF0000", text="incorrect. {} {} {} = {}".format(question_list[0],
                                                question_list[1],
                                                question_list[2],
                                                question_list[3]))

      # If the quiz mode is multiple choice
      if settings_list[0] == "quiz mode: multiple choice\n":
        # Disable all answer buttons
        self.choice_button_1.config(state=DISABLED)
        self.choice_button_2.config(state=DISABLED)
        self.choice_button_3.config(state=DISABLED)
        self.choice_button_4.config(state=DISABLED)
      # If the quiz mode is typed input
      elif settings_list[0] == "quiz mode: typed input\n":
        # Disable the submit button
        self.submit_button.config(state=DISABLED)
      # Work out how much time has passed
      quiz_time = time.time() - start_time
      # If less than a minute has passed, continue
      if quiz_time <= 30:
        # Wait a second and a half, then generate a new question
        self.quiz_frame.after(1500, lambda: self.generate_question(settings_list, start_time, score))
      # If time has run out
      else:
        # Inform user that time is up and of their score
        self.output_label.config(fg="#FF0000", text="Time up! Score: {}".format(score))
        # Wait 2 and a half seconds, then send the user back to the main menu
        self.quiz_frame.after(2500, lambda:self.send_home("home", score, settings_list))
    # If the user entered an invalid value (This can only occur in typed input)
    except ValueError:
      # Inform the user of their invalid value; they are able to fix this for this question
      self.output_label.config(text="Invalid Value", fg="#FF0000")

  # Create a function to send the user back to main menu
  def send_home(self, button, score, settings_list):
    # Retrieve the quiz type and remove any new line characters
    quiz_type = settings_list[1].strip()
    # If the users score isn't zero (zero scores won't be saved)
    if score != 0:
      # Read the scores file for the selected quiz type and assign it to a list
      with open("files/{}_scores.txt".format(quiz_type), "r") as file:
        history_list = file.readlines()
      # If there are past scores saved
      if history_list[0] != "0":
        # Append scores file with new score
        with open("files/{}_scores.txt".format(quiz_type), "a") as file:
         file.write("\n{}".format(score))
      # If there are no past scores saved
      else:
        # Overwrite scores file with new scores
        with open("files/{}_scores.txt".format(quiz_type), "w") as file:
          file.writelines("{}".format(score))
    # Check that function was called appropriately (By button or time up)
    if button == "home":
      # Destroy the quiz window and open the main menu
      self.quiz_window.destroy()
      main_menu()


      
# Create history class
class history:
  # Upon initialisation
  def __init__(self):
    
    # Create and title the history window
    self.history_window = Tk()
    self.history_window.title("History")

    # Create a frame to place elements in
    self.history_frame = Frame(padx=10, pady=10)
    self.history_frame.grid()

    # Create a title for the history page
    self.title_label = Label(self.history_frame,
                             text="History",
                             font=("Arial", "12", "bold"),
                             fg="#000000")
    self.title_label.grid(row=0)

    # Create a frame to place scores in =
    self.score_frame = Frame(self.history_frame, padx=10, pady=10)
    self.score_frame.grid(row=1)

    # Create four titles - One for addition, subtraction, multiplication and division
    self.addition_title = Label(self.score_frame, text="Addition\nScores:", font=("Arial", "8", "bold"), fg="#000000")
    self.addition_title.grid(row=0, column=0)

    self.subtraction_title = Label(self.score_frame, text="Subtraction\nScores:", font=("Arial", "8", "bold"), fg="#000000")
    self.subtraction_title.grid(row=0, column=1)

    self.multiplication_title = Label(self.score_frame, text="Multiplication\nScores:", font=("Arial", "8", "bold"), fg="#000000")    
    self.multiplication_title.grid(row=0, column=2)
    
    self.division_title = Label(self.score_frame, text="Division\nScores:", font=("Arial", "8", "bold"), fg="#000000")  
    self.division_title.grid(row=0, column=3)

    # Create labels for each of the most recent scores; four for each type of quiz, so 16 in total
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

    # Create a label that spans the four columns informing the user the following scores are high scores
    self.high_score_label = Label(self.score_frame, text="High scores:", font=("Arial", "12", "bold"))
    self.high_score_label.grid(row=5, columnspan=4)

    # Create labels displaying high scores for each quiz type; four in total
    self.high_score_a = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.high_score_a.grid(row=6, column=0)

    self.high_score_s = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.high_score_s.grid(row=6, column=1)

    self.high_score_m = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.high_score_m.grid(row=6, column=2)

    self.high_score_d = Label(self.score_frame, text="0", font=("Arial", "8", "bold"))
    self.high_score_d.grid(row=6, column=3)

    # Create a frame to place buttons in
    self.button_frame = Frame(self.history_frame, padx=10, pady=10)
    self.button_frame.grid(row=2)

    # Create a button to export scores
    self.export_button = Button(self.button_frame, 
                               text="Export",
                               bg="#A1E887",
                               fg="#000000",
                               font=("Arial", "8", "bold"),
                               width=10,
                               command=lambda:self.export_history("export"))
    self.export_button.grid(row=0, column=0)

    # Create a button to clear scores
    self.clear_button = Button(self.button_frame,
                               text="Clear",
                               bg="#A1E887",
                               fg="#000000",
                               font=("Arial", "8", "bold"),
                               width=10,
                               command=lambda:self.clear_history("clear"))
    self.clear_button.grid(row=0, column=1)

    # Create a button to send the user to the main menu
    self.home_button = Button(self.button_frame,
                              text="Home",
                              bg="#A1E887",
                              fg="#000000",
                              font=("Arial", "8", "bold"),
                              width=10,
                              command=lambda:self.home_button_pressed("home"))
    self.home_button.grid(row=0, column=2)

    # Call the function to retrieve scores from file
    self.retrieve_scores()

  # Create a function to retrieve scores from file
  def retrieve_scores(self):
    # Retrieve scores from each of the four history files as lists of integers
    with open("files/Addition_scores.txt", "r") as history_file:
      addition_history = [int(x) for x in history_file.readlines()]
    with open("files/Subtraction_scores.txt", "r") as history_file:
      subtraction_history = [int(x) for x in history_file.readlines()]
    with open("files/Multiplication_scores.txt", "r") as history_file:
      multiplication_history = [int(x) for x in history_file.readlines()]
    with open("files/Division_scores.txt", "r") as history_file:
      division_history = [int(x) for x in history_file.readlines()]

    # Reverse each list so it runs from most recent to least recent
    addition_history.reverse()
    subtraction_history.reverse()
    multiplication_history.reverse()
    division_history.reverse()

    # Attempt to assign four addition scores to the four labels
    try:
      self.addition_score_one.config(text=addition_history[0])    
      self.addition_score_two.config(text=addition_history[1])    
      self.addition_score_three.config(text=addition_history[2])
      self.addition_score_four.config(text=addition_history[3])
    # If there are not enough scores to fill the four labels, fill what can be filled and move on
    except IndexError:
      pass
    # Attempt to assign four subtraction scores to the four labels
    try:
      self.subtraction_score_one.config(text=subtraction_history[0])
      self.subtraction_score_two.config(text=subtraction_history[1])
      self.subtraction_score_three.config(text=subtraction_history[2])
      self.subtraction_score_four.config(text=subtraction_history[3])
    # If there are not enough scores to fill the four labels, fill what can be filled and move on
    except IndexError:
      pass
    # Attempt to assign four multiplication scores to the four labels
    try: 
      self.multiplication_score_one.config(text=multiplication_history[0])
      self.multiplication_score_two.config(text=multiplication_history[1])
      self.multiplication_score_three.config(text=multiplication_history[2])
      self.multiplication_score_four.config(text=multiplication_history[3])
    # If there are not enough scores to fill the four labels, fill what can be filled and move on
    except IndexError:
      pass
    # Attempt to assign four division scores to the four labels
    try:
      self.division_score_one.config(text=division_history[0])
      self.division_score_two.config(text=division_history[1])
      self.division_score_three.config(text=division_history[2])
      self.division_score_four.config(text=division_history[3])
    # If there are not enough scores to fill the four labels, fill what can be filled and move on
    except IndexError:
      pass

    # Assign the high scores for each type to output
    self.high_score_a.config(text=max(addition_history))
    self.high_score_s.config(text=max(subtraction_history))
    self.high_score_m.config(text=max(multiplication_history))
    self.high_score_d.config(text=max(division_history))

  # Create a function to export the history to a file
  def export_history(self, button):
    # Check function was called when the export button was pressed
    if button == "export":
      # Retrieve as lists of integers the the scores saved to the files
      with open("files/Addition_scores.txt", "r") as file:
        scores_a = [int(x) for x in file.readlines()]
      with open("files/Subtraction_scores.txt", "r") as file:
        scores_s = [int(x) for x in file.readlines()]
      with open("files/Multiplication_scores.txt", "r") as file:
        scores_m = [int(x) for x in file.readlines()]
      with open("files/Division_scores.txt", "r") as file:
        scores_d = [int(x) for x in file.readlines()]

      # Reverse the lists so they run from most to least recent
      scores_a.reverse()
      scores_s.reverse()
      scores_m.reverse()
      scores_d.reverse()

      # Create or overwrite the file for exported scores with current data for every type
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

  # Create a function to clear history
  def clear_history(self, button):
    # Check function was called by user pressing clear button
    if button == "clear":
      # Overwrite each file with "0"
      with open("files/Addition_scores.txt", "w") as file:
        file.write("0")
      with open("files/Subtraction_scores.txt", "w") as file:
        file.write("0")
      with open("files/Multiplication_scores.txt", "w") as file:
        file.write("0")
      with open("files/Division_scores.txt", "w") as file:
        file.write("0")
      # Close the window and call the class again; this has the effect of refreshing the page
      self.history_window.destroy()
      history()

  # Create a function to send the user to the main menu when they press the home button
  def home_button_pressed(self, button):
    # Check the function was called when the home button was pressed
    if button == "home":
      # Destroy the window and open the main menu window
      self.history_window.destroy()
      main_menu()



#**************Main Routine******************

# Check that code has been run directly by the interpreter
if __name__ == "__main__":

  # Open main menu
  main_menu()
