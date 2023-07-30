

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            # Not a prime
    if is_prime:
        print("It is a prime number.")
    else:
        print("It is not a prime number.")

# given code:

n = int(input("Check this number: "))
prime_checker(number=n)
