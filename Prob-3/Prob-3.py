# Module 7
#   Programming Assignment 10
#     Prob-3.py

# Brandon Norton

def main():
    # your code here
    sum = 0.0
    x = float(input("Please enter a positive number: "))

    while True:
        sum = sum + x
        x = float(input("Please enter a positive number: "))

        if x <= 0:
            break
    
    print("\nYour Total sum is:", sum)


main()    