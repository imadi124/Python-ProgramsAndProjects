#22.Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
def calculate_animals(heads, legs):
    # Validate inputs
    if legs % 2 != 0 or heads <= 0 or legs <= 0:
        return "Invalid input. Legs must be an even number, and heads/legs must be positive."

    # Solve for chickens and dogs
    chickens = (2 * heads - legs // 2)
    dogs = heads - chickens

    if chickens < 0 or dogs < 0:
        return "No solution. Check the input values."
    return f"Number of Chickens: {chickens}, Number of Dogs: {dogs}"

# Input total heads and legs
try:
    heads = int(input("Enter the total number of heads: "))
    legs = int(input("Enter the total number of legs: "))
    result = calculate_animals(heads, legs)
    print(result)
except ValueError:
    print("Please enter valid integers for heads and legs.")
