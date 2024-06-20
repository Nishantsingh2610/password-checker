import re

def assess_password_strength(password):
    # Minimum criteria
    length_min = 8
    uppercase_min = 1
    digit_min = 1
    special_min = 1

    # Regular expressions for character classes
    uppercase_regex = r"[A-Z]"
    digit_regex = r"\d"
    special_regex = r"[!@#$%^&*()-_=+[\]{};:'\",.<>/?]"

    # Initialize strength score and feedback list
    strength_score = 0
    feedback = []

    # Check length
    if len(password) >= length_min:
        strength_score += 1
    else:
        feedback.append("Password should be at least {} characters long.".format(length_min))

    # Check uppercase letters
    if re.search(uppercase_regex, password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check digits
    if re.search(digit_regex, password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check special characters
    if re.search(special_regex, password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine strength level based on score
    if strength_score == 4:
        strength_level = "Strong"
    elif strength_score >= 2:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    # Print feedback
    if feedback:
        print("\n".join(feedback))
    else:
        print("Password meets all criteria.")

    return strength_level

# Example usage:
password = "Nishant@123"
strength = assess_password_strength(password)
print("Password strength level:", strength)

