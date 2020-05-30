# Module 7
#   Programming Assignment 10
#     Prob-1.py

# Brandon Norton

def main():
    sum = 0.0
    
    x = float(input("Please enter a number. (Enter a Negative number to quit program. >> "))
   
    while x >= 0:
        sum = sum + x
        x = float(input("Please enter a number. (Enter a Negative number to quit program. >> "))
   
    print("\nThe sum of the numbers is", sum)
    
main()    