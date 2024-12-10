def is_prime(num):
    prime_num = True
    for place in range(2,num):
        if numb % place == 0:
            return False
        
    print(prime_num)
is_prime(73)

# way the course completes this challenge:
def is_prime2(num):
    if num == 2:
        return True
    if num == 1:
        return False
 
    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False
 
    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True