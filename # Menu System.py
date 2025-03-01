# Menu System
def menu_choice():
   print("©~~~~~~~~~~~~~~~~~~~~~~©\n|                      |")
   print("|         MENU         |\n|                      |")
   print("|  1.  Wordle          |")
   print("|  2.  Trivia Quiz     |")
   print("|  3.  Exit            |")
   print("|  4.  About the Devs  |\n|                      |")
   print("©~~~~~~~~~~~~~~~~~~~~~~©")


   try:
       user_input = int(input("\nHello there! Please choose an option: "))
       if user_input == 1:
           choice_wordle()
       elif user_input == 2:
           choice_trivia()
       elif user_input == 3:
           print("Thanks for playing. Goodbye!")
       elif user_input == 4:
           developers_profile()
       else:
           print("Invalid input. Please enter a number between 1-4.")
   except ValueError:
       print("Invalid input. Please enter a number.")


# Wordle
def choice_wordle():
   print("\nWELCOME TO WORDLE! \n")


   print("Rules:")
   print("Each guess must be a valid five or seven-letter word.")
   print("Your input must be in UPPERCASE LETTER only.")
   print("If the tile 🟩, the letter is in the correct spot.")
   print("If the tile 🟨, the letter is in the word, but it is not in the correct spot.")
   print("If the tile 🟥, the letter is not in the word. \n")


   print("Select your category:\n1. Countries\n2. Animals\n3. Colors\n")


   category_input = int(input("Enter the category number: "))


   while category_input < 1 or category_input > 3:
       print("Invalid category selection. Please choose a valid category.")
       category_input = int(input("Enter the category number: "))


   print("Select your word:\n1. Word 1\n2. Word 2\n3. Word 3\n4. Word 4\n5. Word 5 \n")


   word_input = int(input("Enter your chosen number: "))


   while word_input < 1 or word_input > 5:
       print("Invalid word selection. Please choose a valid word number.")
       word_input = int(input("Enter your chosen number: "))


   game_wordle(category_input - 1, word_input - 1)


def game_wordle(category, word):
   country = ["JAPAN", "ITALY", "MOROCCO", "FINLAND", "EGYPT", "PAKISTAN", "VIETNAM"]
   animal = ["VULTURE", "TIGER", "EAGLE", "LIZARD", "SHARK", "GIRAFFE", "TURTLE"]
   color = ["YELLOW", "BLACK", "WHITE", "VIOLET", "ORANGE", "FUCHSIA", "MAROON"]


   list_of_categories = ["COUNTRIES", "ANIMALS", "COLORS"]
   categories = [country, animal, color]


   chosen_category = categories[category]


   max_attempts = 0
   blank_space = ["_ _ _ _ _", "_ _ _ _ _ _", "_ _ _ _ _ _ _"]


   secret_word = chosen_category[word]


   print("Category:", list_of_categories[category], "\n")


   if len(secret_word) == 5:
       print("     ", blank_space[0], " \n")
   elif len(secret_word) == 6:
       print("     ", blank_space[1], " \n")
   elif len(secret_word) == 7:
       print("     ", blank_space[2], " \n")


   while max_attempts < 5:
       user_guess = (input("Enter a word: "))


       if not user_guess.isupper():
           print("Invalid Input. Please enter the word in UPPERCASE letters only. \n")
           continue


       if len(user_guess) != len(secret_word):
           print("Invalid Input. Please input a", len(secret_word), end="-LETTER word only.\n")
           continue


       verify = []
       feedback = []


       for i in range(len(secret_word)):
           if user_guess[i] == secret_word[i]:
               verify.append("🟩")
               feedback.append(user_guess[i])
           elif user_guess[i] in secret_word:
               verify.append("🟨")
               feedback.append("_")
           else:
               verify.append("🟥")
               feedback.append("_")


       max_attempts += 1
       print(verify)
       print(feedback)


       if user_guess == secret_word:
           print("Correct! You have guessed the word.")
           break
       elif max_attempts == 5:
           print("Game over. The correct word is", secret_word, ".")


   continue_choice = input("\nWould you like to continue playing? (YES/NO): ").strip().upper()
   if continue_choice == "YES":
       choice_wordle()
   else:
       menu_choice()


# Trivia Quiz
def choice_trivia():
   print("\nWELCOME TO TRIVIA QUIZ! \n")
   category_choice = select_category()
   category_questions = quiz_data[category_choice]["questions"]
   category_options = quiz_data[category_choice]["options"]
   new_game(category_questions, category_options)
   if play_again():
       choice_trivia()
   else:
       menu_choice()


def new_game(questions, options):
  guesses = []
  correct_guesses = 0
  question_num = 1
  choices = ["A","B","C","D"]




  for key in questions:
      print("\n-------------------------------\n")
      print(key)
      for i in options[question_num - 1]:
          print(i)


      while True:
          guess = input("Enter (A, B, C, D): ").upper()
          if guess in choices:
              guesses.append(guess)
              break
          else:
              print("Invalid choice.")
      if guess == questions[key]:
          correct_guesses += 1


      question_num += 1


  total_question = len(questions)
  percentage_score = (correct_guesses / total_question) * 100


  print("\n-------------------------------\n")
  print("Results:")
  print(f"Correct Answers: {correct_guesses}/{len(questions)} ({percentage_score:}%)")
  print("Your Choices:", guesses)


#-------------------------------
def select_category():
  print("Choose a Category:")
  print("1. Animals")
  print("2. Python")
  print("3. Science")


  while True:
      try:
          choice = int(input("Enter your chosen category: "))
          if choice == 1:
              return "animals"
          elif choice == 2:
              return "python"
          elif choice == 3:
              return "science"
          else:
              print("Invalid Choice.")
      except ValueError:
          print("Invalid input. Please enter a number.")


#-------------------------------
def play_again():
   while True:
       response = input("Do you want to play again? (YES/NO): ").upper()
       if response in ["YES", "NO"]:
           return response == "YES"
       print("Invalid input. Please enter YES or NO.")


#-------------------------------
quiz_data = {
  "animals": {
      "questions": {
          "How many hearts does an octopus have?": "B",
          "Which animal is the fastest on land?": "D",
          "What is the closest living relative to the T-Rex?": "A",
          "What is the largest land predator?": "B",
          "What bird cannot move their eyeballs?": "C"
      },
      "options": [
          ["A. 4", "B. 3", "C. 6", "D. 5"],
          ["A. Ostrich", "B. Tiger", "C. Buffalo", "D. Cheetah"],
          ["A. Chicken", "B. Bee", "C. Duck", "D. Cow"],
          ["A. Elephant", "B. Polar Bear", "C. Lion", "D. Hippopotamus"],
          ["A. Emu", "B. Parrot", "C. Owl", "D. Falcon"]
      ]
  },
  "python": {
      "questions": {
          "Who is the creator of the Python programming language?": "B",
          "What is the syntax to print 'hello world!' in Python?": "C",
          "What is the correct operator for power(x^y)?": "B",
          "What does the 'len()' function return to?": "A",
          "Which of the following operators is used to find the remainder in Python?": "B"
      },
      "options": [
          ["A. Albert Einstein", "B. Guido Van Rossum", "C. Tim Berners-Lee", "D. Grace Hopper"],
          ["A. 'Hello World!'", "B. echo('Hello World!')", "C. print('Hello World!')", "D. Hello World!:"],
          ["A. x^y", "B. x**y", "C. x*y", "D. x^^y"],
          ["A. Length", "B. Integer", "C. String", "D. Error"],
          ["A. .", "B. //", "C. &", "D. %"]
          ]
  },
  "science": {
      "questions": {
          "What is the hottest planet in our solar system?": "D",
          "What is the most common eye color in humans?": "A",
          "What is the chemical equation for water?": "B",
          "What is the scientific way to define push or pull?": "C",
          "How many continents are there on earth": "A"
      },
      "options": [
          ["A. Jupiter", "B. Mars", "C. Mercury", "D. Venus"],
          ["A. Brown", "B. Black", "C. Blue", "D. Hazel"],
          ["A. O2", "B. H20","C. H2", "D. CH4"],
          ["A. Mass", "B. Tension", "C. Force", "D. Gravity"],
          ["A. 7", "B. 3", "C. 5", "D. 9"]
      ]
  }
}


# Developers
def developers_profile():
   print("\nDEVELOPERS PROFILE\n")
   print("Name: Ace Francis V. Agustin")
   print("Birthday: October 9, 2006")
   print("Contribution: \n")
   print("Name: Gelai C. Bacle-an")
   print("Birthday: August 10, 2005")
   print("Contribution: \n")
   print("Name: Kyrie Eleison Q. Tubog")
   print("Birthday: August 11, 2005")
   print("Contribution: \n")
   print("Name: Samantha Angel E. Valderama")
   print("Birthday: April 29, 2005")
   print("Contribution: \n")
   print("Created by BSCpE 1-6, Group 2. 2024-2025")


   exit_choice = input("\nWould you like to continue? (YES/NO): ").strip().upper()
   if exit_choice == "NO":
       print("Thank you! Goodbye!")
       exit()
   else:
       menu_choice()


menu_choice()