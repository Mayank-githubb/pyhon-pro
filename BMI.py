def calculate_bmi(weight, height):
  """
  Calculates the Body Mass Index (BMI) for a given weight and height.

  Args:
      weight: The weight in kilograms (kg).
      height: The height in meters (m).

  Returns:
      The calculated BMI as a float.
  """
  return weight / (height * height)

def interpret_bmi(bmi):
  """
  Interprets the BMI value based on standard WHO classifications.

  Args:
      bmi: The calculated BMI value.

  Returns:
      A string describing the BMI category.
  """
  if bmi <= 18.5:
    return "Underweight"
  elif bmi <= 24.9:
    return "Normal weight"
  elif bmi <= 29.9:
    return "Overweight"
  elif bmi <= 34.9:
    return "Obese (Class I)"
  elif bmi <= 39.9:
    return "Obese (Class II)"
  else:
    return "Severely obese (Class III)"

# Get user input
weight = float(input("Enter your weight in kilograms (kg): "))
height = float(input("Enter your height in meters (m): "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Print BMI and interpretation
print(f"Your BMI is: {bmi:.2f}")  # Format BMI to two decimal places
print(interpret_bmi(bmi))
