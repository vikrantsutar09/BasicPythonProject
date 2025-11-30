
questions = ("Q1. What is the output of: print(type([]))?",
             "Q2. Which keyword is used to create a function in Python?",
             "Q3. Which operator is used for exponentiation in Python?",
             "Q4. What does len('Hello') return?",
             "Q5. What is the correct file extension for Python files?")

options =  (("A) <class 'tuple'>", "B) <class 'list'>", "C) <class 'set'>", "D) <class 'dict'>"),
           ("A) func", "B) method", "C) def", "D) function"), 
           ("A) ^", "B) **", "C) *", "D) //"), 
           ("A) 4", "B) 6", "C) 5", "D) 3"),
           ("A) .py", "B) .pt", "C) .pyt", "D) .python"))

answers = ("B", "C", "B", "C", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------\n")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")


    question_num += 1

print("----------------------\n")
print("         RESULT          ")
print("----------------------\n")

print("Answers: ", end =" ")
for answer in answers:
    print(answer, end = " ")
print()

print("Gueesses: ", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()


score  = int(score / len(questions) * 100)
print(f"Your score is: {score}%")