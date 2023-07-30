
import math

# You are painting a wall. The instructions on the paint can says that '1 can of paint can cover 5 square meters' of wall. 
# given a random height and width of wall, calculate how many cans of paint you'll need to buy

# number of cans = (wall height X wall width) % coverage per can

# example: Height = 2, Width = 4, Coverage = 5
# number of cans = (2 x 4) % 5 = '1.6'

# Since you can't buy 0.6 of paint, the result should be rounded up to 2 cans.

print("Hello, please help us calculate how many cans of paint you need by providing height and width!")

def paint_calculation(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"You will need {number_of_cans} cans of paint.")



test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calculation(height=test_h, width=test_w, cover = coverage)




