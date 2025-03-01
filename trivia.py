#-------------------------------
def new_game(category_questions, category_options):

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in category_questions:
        print("-------------------------------")
        print(key)
        for i in category_options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer("questions.get(key), guess:")
        question_num += 1

    display_score(correct_guesses, guesses)

#-------------------------------
def check_answer(correct_answer, guess):

    if guess == correct_answer:
        print("✅CRRECT!")
        return 1
    else:
        print("❎INCORRECT")
        return 0

#-------------------------------
def display_score(correct_guesses, guesses, questions):
    print("-------------------------------")
    print("RESULTS")
    print("-------------------------------")
    print("answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end=" ")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print(f"Your score is: {correct_guesses}/{len(questions)} ({str(score)}%)")# len(questions), str(score) + "%")


#-------------------------------
def select_category():
    print("Choose a Category")
    print("1. Animals")
    print("2. Python")
    print("3. Science")

    choice = int(input("Enter your chosen category: "))

    if choice == 1:
       return "animals"
    elif choice == 2:
       return "python"
    elif choice == 3:
       return "science"
    else:
       print("Invalid Choice.")
       choice = int(input("Enter your chosen category: "))
#-------------------------------

def play_again():
    response = input("do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
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

while True:
   category_choice = select_category()
   category_questions = quiz_data[category_choice]["questions"]
   category_options = quiz_data[category_choice]["options"]
   new_game(category_questions, category_options)
   if not play_again():
       break