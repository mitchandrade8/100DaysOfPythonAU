
# Your life in weeks

maxAge = 90

age = input("What is your current age? ")

timeRemaining = maxAge - int(age)

timeRemaining_conversion_days = round(timeRemaining*365)
print(f"{timeRemaining_conversion_days} days remaining in your life ")

timeRemaining_conversion_weeks = round((timeRemaining*365)/4)
print(f"{timeRemaining_conversion_weeks} weeks remaining in your life ")


timeRemaining_conversion_months = round(timeRemaining*365)
print(f"{timeRemaining} years left to live ")