# Function to get and display person's information
def person_info():
    # Taking input from user
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email ID: ")
    phone = input("Enter your phone number: ")
    
    # Displaying the entered information
    print("\n--- Person's Information ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email ID: {email}")
    print(f"Phone Number: {phone}")

# Calling the function
person_info()