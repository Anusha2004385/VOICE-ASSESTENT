def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: BMI = weight (kg) / (height (m) ^ 2)
    """
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """
    Classify the BMI into categories based on predefined ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Prompt the user for weight and height
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        # Validate input
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Classify BMI
        category = classify_bmi(bmi)

        # Display the result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

# Run the program
if __name__ == "__main__":
    main()

