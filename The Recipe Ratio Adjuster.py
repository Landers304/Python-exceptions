# Task 1:


def get_number_of_servings(prompt):
    while True:
        try:
            servings = int(input(prompt))
            if servings <= 0:
                print("Enter a positive number of servings.")
            else:
                return servings
        except ValueError:
            print("Invalid entry. Please enter a valid number.")

try:
    original_servings = get_number_of_servings("Enter the number of servings in the original recipe: ")
    desired_servings = get_number_of_servings("Enter the number of servings you wish to make: ")
    
    print("Original servings:", original_servings)
    print("Desired servings:", desired_servings)
    
except KeyboardInterrupt:
    print("\nOperation interrupted by the user.")




#Task 2:


def get_number_of_servings(prompt):
    while True:
        try:
            servings = int(input(prompt))
            if servings <= 0:
                print("Please enter a positive number of servings.")
            else:
                return servings
        except ValueError:
            print("Invalid entry. Please enter a valid number.")

try:
    original_servings = get_number_of_servings("Enter the number of servings in the original recipe: ")
    desired_servings = get_number_of_servings("Enter the number of servings you wish to make: ")
    
    print("Original servings:", original_servings)
    print("Desired servings:", desired_servings)
    
    try:
        adjustment_factor = desired_servings / original_servings
        print("Adjustment factor:", adjustment_factor)
    except ZeroDivisionError:
        print("Error: The original number of servings cannot be zero.")
    except ArithmeticError as e:
        print("Arithmetic error occurred:", e)
    
except KeyboardInterrupt:
    print("\nOperation interrupted by the user.")




#Task 3:


def get_number_of_servings(prompt):
    while True:
        try:
            servings = int(input(prompt))
            if servings <= 0:
                print("Please enter a positive number of servings.")
            else:
                return servings
        except ValueError:
            print("Invalid input. Please enter a valid number.")

try:
    original_servings = get_number_of_servings("Enter the number of servings in the original recipe: ")
    desired_servings = get_number_of_servings("Enter the number of servings you wish to make: ")
    
    print("Original servings:", original_servings)
    print("Desired servings:", desired_servings)
    
    try:
        adjustment_factor = desired_servings / original_servings
        print("Adjustment factor:", adjustment_factor)
        
        print("Adjusted recipe quantities:")
        
    except ZeroDivisionError:
        print("Error: The original number of servings cannot be zero.")
    except ArithmeticError as e:
        print("Arithmetic error occurred:", e)
    
finally:
    print("Enjoy your cooking!")
