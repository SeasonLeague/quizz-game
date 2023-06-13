#-------------------------------------

def new_game():
	
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------------")
        print(key)

        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -----------------------------------
def check_answer(answer, guess):
	
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0
# -----------------------------------
def display_score(correct_guesses, guesses):
    print("-----------------------------------")
    print("RESULTS")
    print("-----------------------------------")
    
    print("ANSWERS: ", end = "")
    for i in questions:
        print(questions.get(i), end = " ")
    print()

    print("Guesses: ", end = "")
    for i in guesses:
        print(i, end = " ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")

def play_again():
    response = input("Do you want to play again?   (yes or no): ")
    response = response.upper()

    if response == 'YES':
        import sys 
        import os 
        from time import sleep
        if sys.platform.startswith("win32"):
            os.system("cls")
            sleep(1)
        elif sys.platform.startswith('linux'):
            os.system('clear')
            sleep(1)
        else:
            print("Can't get machine operating system...")
        return True 
    else:
        return False

questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "What is the latest version of Python? ": "C",
    "What type of programming language is Python?: ": "C",
    "What are the two main types of loops in Python?: ": "D",
    "How do you open a file in Python?: ": "A",
    "How do you handle exceptions in Python?: ": "D",
    "What is the purpose of the 'if __name__ == '__main__':' condition in Python?: ": "C",
    "What is a module in Python?: ": "C",
    "What is the difference between a tuple and a list in Python?: ": "A."
}


options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ['A. 1989', 'B. 1991', 'C. 1987', 'D. 1980'],
          ["A. Python 2.11.2", "Python 3.10", "C. Python 3.11.2", "Python 2.10.1"],
          ["A. Python is a high-level", "B. Python is interpreted programming language", "C. A and B", "D. None of the above"],
          ["A. for loops", "B. while loops", "C. None of the above", "D. A and B"],
          ["A. Open() function", "B. for loops", "C. with while loops", "D. None of the above"],
          ["A. try block only", "B. except blocks only", "C. None of the listed", "D. try-except blocks"],
          ["A. Execute when imported and when  run as a script", "B. Nothing happens to the script", "C. Condition only executes code when script is run directly.", "D. None listed"],
          ["A. Modules are files contain python code", "B. Modules are highly used codes", "C. Modules are files that contain Python definitions, statements, and functions."],
          ["A. Tuples are immutable and List are mutable", "B. Tuples are mutable while list are immutable", "C. Tuples are mutable while list is also mutable", "D. Both are immutable"]]

new_game()

while play_again():
    new_game().run()

print("\nByeeeee!")