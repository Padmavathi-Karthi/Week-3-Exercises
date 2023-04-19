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

print(" ")

# Fill in the blanks to complete the “counter” function. This function should count down from the “start” to “stop” variables when “start” is bigger than “stop”. Otherwise, it should count up from “start” to “stop”. Complete the code so that a function call like “counter(3, 1)” will return “Counting down: 3, 2, 1” and “counter(2, 5)” will return “Counting up: 2, 3, 4, 5”.

def counter(start, stop):
    number = start
    return_string = " "
    if start > stop:
        return_string = "Counting down: "
        while number >= stop: # Complete the while loop
            return_string += str(number) # Add the numbers to the "return_string"
            if start > stop:
                return_string += ','
            number -= 1 # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while number <= stop: # Complete the while loop
            return_string += str(number) # Add the numbers to the "return_string"
            if start < stop:
                return_string += ','
            number += 1 # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

print(" ")