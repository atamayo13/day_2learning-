# Ask the user to input the current weather. This can be simplified to three categories for ease: "sunny", "rainy", or "cold".
weather = input("What is the current weather? (sunny, rainy, cold): ")



# Implement the decision structure to advise on what to wear:
# If the weather is "sunny", recommend "wear sunglasses and a hat".
if weather == "sunny":
    print("wear sunglasses and a hat.")
# If the weather is "rainy", recommend "carry an umbrella and wear waterproof boots".
elif weather == "rainy":
    print("carry an umbrella and wear waterproof boots")
# If the weather is "cold", recommend "wear a warm coat and gloves".
elif weather == "cold":
    print("wear a warm coat and gloves")
# If the input doesn't match any category, inform the user with a message saying the input was not recognized.
else:
    print("If the input doesn't match any category, inform the user with a message saying the input was not recognized.")

#Next 
# Ask the user to input their age and location. Assume location to be either "urban" or "rural".
age = int(input("What is your age"))
location = input("What is your location? (urban, rural)")
# Implement the eligibility checks using comparison and logical operators:

#logical and compatison operators examples
# >, <, >=, <=, ==, !=, and, or, not

# Participants must be at least 18 years old.
# Participants must live in an "urban" area.
# Display a message indicating whether the user is eligible or not based on these conditions.
if age >= 18 and location == "urban":
    print("you are eligible to participate")
else:
    print("you are not eligible to participate")


age = int(input("What is your age"))
citizenship = input("Are you a U.S. citizen (yes, no):" ) 

if age >= 18 and citizenship == "yes":
    print("you are not eligible to vote")

else:
     print("you are not eligible to vote")

