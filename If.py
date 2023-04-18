# Fill in the blanks to complete the function “digits(n)” to count how many digits the given number has. For example: 25 has 2 digits and 144 has 3 digits. 
# Tip: you can count the digits of a number by dividing it by 10 once per digit until there are no digits left.

def digits(n):
    count = 0
    if n == 0:
      count += 1
    while n >= 1: # Complete the while loop condition
        # Complete the body of the while loop. This should include 
        # performing a calculation and incrementing a variable in the
        # appropriate order.  
        n = n/10
        count += 1
    return count
    
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1