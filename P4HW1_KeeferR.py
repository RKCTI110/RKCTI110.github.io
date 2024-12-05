 # KeeferR

 # 12 / 5 / 2024

 # P4HW1

 # using statement to collect score then program loop

"""
ALGORITHM:
1. Input number of scores to process
2. Initialize empty scores list
3. For each score (1 to number of scores):
    - Input score
    - While score is invalid (< 0 or > 100):
        * Display error message
        * Input score again
    - Add valid score to list
4. Display results header
5. Find lowest score
6. Remove lowest score from list
7. Calculate average of remaining scores
8. Determine letter grade based on average:
    - A: >= 90
    - B: >= 80
    - C: >= 70
    - D: >= 60
    - F: < 60
9. Display all results
"""

num_scores = int(input("How many scores would you like to enter? "))
scores = []

for i in range(num_scores):
    score = float(input(f"Enter score {i+1}: "))
    while score < 0 or score > 100:
        print("INVALID Score!!!!")
        print("Score should be between 0 and 100.")
        score = float(input(f"Enter score {i+1} again: "))
    scores.append(score)

print("--------------Results--------------")
lowest = min(scores)
print(f"Lowest score: {lowest}")

scores.remove(lowest)
print(f"Scores after dropping lowest: {scores}")

average = sum(scores) / len(scores)
print(f"Average: {average:.2f}")

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Letter grade: {grade}")


