
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Easy way to solve
print(max(student_scores))

# Under the hood method
    # created a value to store the highest value while we loop through our array of scores
highest_score = 0

for score in student_scores:
    # we check the new value while looping through against the last score to update the highest score
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
