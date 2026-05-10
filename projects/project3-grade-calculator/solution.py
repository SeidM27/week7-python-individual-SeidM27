# Project 3 — Grade Calculator
# Author: your name here

scores = []

# TODO: use a for loop to collect 5 scores and append each to the list

# TODO: calculate the average using sum() and len()

# TODO: determine the grade with if/elif/else (A/B/C/D/F)

# TODO: print the average (1 decimal place) and the grade
#   Hint: f"{average:.1f}" formats to 1 decimal place
# Project 3 - Grade Calculator
# Author: Seid Mamuti
scores = []
# Ask the user to enter 5 scores
for i in range(5):
score = float(input(f"Enter score {i + 1}: "))
scores.append(score)
# Calculate the average
average = sum(scores) / len(scores)
# Determine the letter grade
if average >= 90:
grade = "A"
elif average >= 80:
grade = "B"
elif average >= 70:
grade = "C"
elif average >= 60:
grade = "D"
else:
grade = "F"
# Print the result
print(f"Average: {average:.1f}")
print(f"Grade: {grade}")
