#geometric_shape_area_calculator

import math # DO NOT MODIFY

def main():
    circle_pi = math.pi # DO NOT MODIFY, this line of code is assigning the variable 'circle_pi' equal to Pi ~3.14

    # TODO: In terminal, print Welcome to the geometric shape area calculator!
    # This code just prints a welcome statement in the terminal
    print('Welcome to the geometric area calculator')
    
    # User Options
    #Each variable represent a different value and in this instance a shape which can be chose to calculate.
    Circle = 1
    Rectangle = 2
    Triangle = 3

   
    
    # TODO: Using one print statement, use string concatenation to print the options only 
    # as a single string (make sure to add a space between each option)
 
    # Here I am just using an f string to print my different options all in one string at 1 time which is string concatenation.The value for {circle} is 1, The value for {rectangle} is 2, The value for {triangle} = 3.
    print(f"Circle = {Circle} Rectangle = {Rectangle} Triangle = {Triangle}")

    

    # TODO: In terminal, ask the user "Select a shape by entering 1, 2, or 3' and assign the input to a new variable named 'choice'

    # Here I am giving the user the option to choose a shape by entering 1, 2, or 3. After the user select a number, that number will be stored in the choice variable that I created.
    choice = input("Select a shape by entering 1, 2, 3: ")

    # TODO: Convert the variable 'choice' to an integer data type.
    # Here I am taking my choice variable and turning the value of choice into an integer, by using the integer function/method.
    choice = int(choice)

    # TODO: With one line of code, verify the variable 'choice' is indeed the data type integer, use conditional logic and print the output.  If converted correctly, the output in Terminal should read 'True'.

    # Here I am using an if/else statement to either print true if my choice variable is storing an integer or print false if choice does not return an integer.
    if type(choice) is int:
     print(True)
    else:
     print(False)
  
    if choice == 1:  #DO NOT REMOVE THE 'IF'
        # Calculate the area of a circle
        #Here This is an if statement that checks if the user's choice is equal to 1, which corresponds to calculating the area of a circle.

        # TODO: Assign a new variable named 'radius' and ask for the user's input for the radius of the circle.
       
        # TODO: Convert 'radius' to float.
         radius = float(input("Enter the radius of the circle: ")) 
         # Here This code asks the user to enter the radius of the circle and stores their input as a string. Then, it converts the input to a floating-point number using float() and assigns it to the 'radius' variable.

        # TODO: Assign a new variable named 'area' and implement the logic to calculate the area of a circle.
         # Here I am calculating the area of circle using the formula

         area = circle_pi * radius**2
        # HINT 1 : The formula to find area of a circle: 'circle_pi' times radius squared.  
        # Hint 2 : circle_pi is a variable that has been assigned on Line 9 and equals Pi in math.  

    elif choice == 2: # DO NOT REMOVE THE 'ELIF'
        # Here I have an elif statement that checks to see if choice is equal to 2, which represent rectangle.
        # Calculate the area of a rectangle
        # TODO: Assign new variables 'length' and 'width' and ask for the user's input for the length and width of the rectangle.
        # TODO: Convert both 'length' and 'width' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a rectangle.
        # HINT: The formula to find the area of a rectangle: length times width

        # Here These lines ask the user to enter the length and width of the rectangle and store their input as strings. Then, it convert the inputs to floating-point numbers and assign them to the 'length' and 'width' variables.
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

       # Here I am  calculating the area of the rectangle using the formula for the area of a rectangle.
        area = length * width

        print(f"The area of the rectangle is: {area:.2f} square units.")
        
    elif choice == 3: #DO NOT REMOVE THE 'ELIF'
        # Here my elif statement checks to if choice is equal to 3 and since it is, it runs the code below.
        # Calculate the area of a triangle
        # TODO: Assign new variables 'base' and 'height' and ask for the user's input for the base length and height of the triangle.
        # TODO: Convert both 'base' and 'height' to float.
        # TODO: Assign a new variable 'area' and implement the logic to calculate the area of a triangle.
        # HINT: The formula to find the area of a Triangle: half times base times height

        # Here I have a base and height variable which is storing the value of a float received after an input is given
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))

        # Here I am calculating to find the area of a triangle. Below is the formula used to find the area of triangle.
        area = 0.5 * base * height

    else:
        # TODO: If the user enters anything other than 1, 2 or 3, print statement "Invalid choice ."
     print("Invalid choice .")
     # Below will give the user an error because I have not included any number besides 1, 2 and 3 as an option for the user to select in the input.

    if choice in [1, 2, 3]: # DO NOT MODIFY
        print(f"The area is: {area:.2f} square units.") # DO NOT MODIFY

    # TODO: Print a statement explaining each step required to find and complete your technical assignments.  Be specific. 


if __name__ == "__main__": # DO NOT MODIFY
    main() # DO NOT MODIFY
