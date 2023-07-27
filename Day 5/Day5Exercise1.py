
# Average height exercise

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# easy way to solve problem
##total_height = sum(student_heights)
##number_of_students = len(student_heights)
##average_height = round(total_height / number_of_students)
##print(average_height)

# under the hood 
    # use a for loop
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

