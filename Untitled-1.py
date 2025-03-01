#-------------------------------
def new_game():
   guesses = []
   correct_guesses = 0
   question_num = 1




   for key in questions:
       print("-------------------------------")
       print(key)
       for i in options[question_num - 1]:
           print(i)
       guess = input("Enter (A, B, C, D): ").upper()
       guesses.append(guess)




       correct_guesses += check_answer(questions.get(key), guess)
       question_num += 1




   display_score(correct_guesses, guesses)




#-------------------------------
def check_answer(answer, guess):

   if answer == guess:
       print("CORRECT!")
       return 1
   else:
       print("INCORRECT")
       return 0




#-------------------------------
def display_score(correct_guesses, guesses):
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




   score = int((correct_guesses / len(questions)) * 100)
   print("your score is: "+ str(score) + "%")




#-------------------------------
def play_again():
   response = input("do you want to play again? (yes or no): ").upper()
   return response == "YES"


#-------------------------------




questions = {
   "how many hearts does an octopus have?": "B",
   "which animal is the fastest on the land": "D",
   "what is the closest living relative to the T-Rex?": "A",
   "what is the largest land predator?": "B",
   "what bird cannot move their eyeballs?": "C"
}




options = [["A. 4", "B. 3", "C. 6", "D. 5"],
       ["A. ostrich", "B. tiger", "C. buffalo", "D. cheetah"],
       ["A. chicken", "B. bee", "C. duck", "D. cow"],
       ["A. elepant", "B. polar bear", "C. lion", "D. hippopotamus"],
       ["A. emu", "B. parrot", "C. owls", "D. falcons"]]




new_game ()




while play_again():
   new_game()
