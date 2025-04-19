print("WELLCOME TO AGE CALLCULATER")
from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Ask user for their age
age = int(input("Enter your age: "))

# Calculate year of birth
year_of_birth = current_year - age

# Display the result
print(f"You were born in the year {year_of_birth}.")
