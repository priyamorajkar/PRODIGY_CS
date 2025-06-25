import re

def check_password_strength(password):
    # Define criteria
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    errors = {
        "length": length_error,
        "uppercase": uppercase_error,
        "lowercase": lowercase_error,
        "digit": digit_error,
        "special_char": special_char_error
    }

    # Count how many conditions are met
    passed_criteria = sum(not error for error in errors.values())

    # Determine strength
    if passed_criteria == 5:
        strength = "Very Strong"
    elif passed_criteria >= 4:
        strength = "Strong"
    elif passed_criteria == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Give user feedback
    feedback = []
    if length_error:
        feedback.append("Make it at least 8 characters long.")
    if uppercase_error:
        feedback.append("Add at least one uppercase letter.")
    if lowercase_error:
        feedback.append("Add at least one lowercase letter.")
    if digit_error:
        feedback.append("Add at least one number.")
    if special_char_error:
        feedback.append("Include at least one special character (e.g., !, @, #).")

    return strength, feedback


# Test it
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength, suggestions = check_password_strength(user_password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve:")
        for item in suggestions:
            print(f"- {item}")
    else:
        print("Great password!")
