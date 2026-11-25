from quize_question import questions
from quize_functions import show_question, check_answer, calculate_percentage
import numpy as np
import pandas as pd

# Heading
print("================================")
print("      QUIZ MANAGEMENT SYSTEM")
print("================================")


# Category Selection
print("\nChoose Quiz Category:")

print("1. Python")
print("2. C++")
print("3. Java")
print("4. DBMS")
print("5. DSA")

try:
    choice = int(input("\nEnter your choice (1-5): "))

except ValueError:
    print("Please enter a valid number!")
    exit()


if choice == 1:
    category = "python"

elif choice == 2:
    category = "cpp"

elif choice == 3:
    category = "java"

elif choice == 4:
    category = "dbms"

elif choice == 5:
    category = "dsa"

else:
    print("Invalid category!")
    exit()


print("\nYou selected:", category.upper())


# Difficulty Selection
print("\nChoose Difficulty:")

print("1. Easy")
print("2. Medium")
print("3. Hard")

try:
    difficulty_choice = int(
        input("\nEnter difficulty (1-3): ")
    )

except ValueError:
    print("Please enter a valid number!")
    exit()


if difficulty_choice == 1:
    difficulty = "easy"

elif difficulty_choice == 2:
    difficulty = "medium"

elif difficulty_choice == 3:
    difficulty = "hard"

else:
    print("Invalid difficulty!")
    exit()


print("\nDifficulty:", difficulty.upper())


# Filter Questions According to Difficulty
selected_questions = []

for question in questions[category]:

    if question["difficulty"] == difficulty:

        selected_questions.append(question)


# Check if questions are available
if len(selected_questions) == 0:

    print("No questions available for this category and difficulty.")

    exit()


# Start Quiz
score = 0
for i, question in enumerate(selected_questions, start=1):

    show_question(question, i)

    try:
        answer = int(input("Enter your answer (1-4): "))

        if answer < 1 or answer > 4:
            print("Please enter a number between 1 and 4.")
            continue

    except ValueError:
        print("Please enter a number between 1 and 4.")
        continue

    if check_answer(question, answer):

        print("Correct! ✓")
        score += 1

    else:

        print("Wrong! ✗")
        print("Correct answer:", question["answer"])



# Calculate Result
percentage = calculate_percentage(
    score,
    len(selected_questions)
)


# Result
print("\n================================")
print("           QUIZ RESULT")
print("================================")

print("Category:", category.upper())
print("Difficulty:", difficulty.upper())

print("Total Questions:", len(selected_questions))

print("Correct Answers:", score)

print(
    "Wrong Answers:",
    len(selected_questions) - score
)

print("Percentage:", percentage, "%")

# Save result to file


with open("results.txt", "a") as file:

    file.write("Quiz Result\n")
    file.write("-------------------------\n")
    file.write("Category: " + category.upper() + "\n")
    file.write("Difficulty: " + difficulty.upper() + "\n")
    file.write("Total Questions: " + str(len(selected_questions)) + "\n")
    file.write("Correct Answers: " + str(score) + "\n")
    file.write("Wrong Answers: " + str(len(selected_questions) - score) + "\n")
    file.write("Percentage: " + str(percentage) + "%\n")
    file.write("-------------------------\n\n")

print("\nResult saved successfully!")

# NumPy Score Analysis

scores = np.array([score])

print("\n===== SCORE ANALYSIS =====")

print("Highest Score:", np.max(scores))
print("Lowest Score:", np.min(scores))
print("Average Score:", np.mean(scores))

# Performance
if percentage >= 80:

    print("Excellent performance!")

elif percentage >= 60:

    print("Good performance!")

elif percentage >= 40:

    print("You passed!")

else:

    print("You need more practice.")

# Pandas Result Table

data = {
    "Category": [category.upper()],
    "Difficulty": [difficulty.upper()],
    "Total Questions": [len(selected_questions)],
    "Correct Answers": [score],
    "Wrong Answers": [len(selected_questions) - score],
    "Percentage": [percentage]
}

df = pd.DataFrame(data)

print("\n===== QUIZ RESULT TABLE =====")
print(df)    