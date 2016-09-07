#This program will determine if three lengths will be able to create a triangle.

#define initial variables and their values
runAgain = ' '
side_a = 2
side_b = 2
side_c = 2

#print the initial values for the example
print("As you know, a triangle has three sides.")

#print information about determining if the three lengths can form a triangle.
print("\nThe sum of any two sides cannot be greater than the third side in order to create a triangle. \n")
print("For an example, I will use the following lengths:\n")

print("Side A = "),
print(side_a)
print("Side B = "),
print(side_b)
print("Side C = "),
print(side_c)

print("\nFor this example, the result is: \n")

#define the function to determine if the three lengths can form a triangle
def is_triangle(a,b,c):
    float(side_a)
    float(side_b)
    float(side_c)
    check1 = float(side_a)+float(side_b)
    check2 = float(side_a)+float(side_c)
    check3 = float(side_c)+float(side_b)
    if (check1 > float(c)) and (check2 > float(b)) and (check3 > float(a)):
        print("\nYes, these lengths will form a triangle.")
    else:
        print("\nNo, these lengths will not form a triangle.")


is_triangle(side_a,side_b,side_c)        #call the function

#ask the user if they would like to try again
while runAgain != 'q':                   #entering q will quit the program
    print("Now it is your turn. You will be prompted to enter a number for each side of your proposed triangle.\n")
    print("Enter a length for side A: ") #prompt for input of length for side a
    side_a = raw_input()
    print("Enter a length for side B: ") #prompt for input of length for side b
    side_b = raw_input()
    print("Enter a length for side C: ") #prompt for input of length for side c
    side_c = raw_input()

    print("\nThe result for your input is: ")
    is_triangle(side_a,side_b,side_c)    #call function

    print("\nWould you like to try again? ")  #ask user if they would like to try again
    print("Enter 'q' for 'quit' or press enter to continue: ") #explain how to quit or to continue

    runAgain = raw_input() #accept input to determine if user wants to go again

#program wrap-up
print("\nThanks for running my Triangle program! Goodbye!")


