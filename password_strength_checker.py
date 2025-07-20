import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @!#$%^&*()_+=\-{}[\]|:;\"'<>,.?/]", password) is None
    common_passwords = ['password', '123456', 'qwerty', 'abc123', 'admin']
    common_error = password.lower() in common_passwords

    errors = {
        'Length': length_error,
        'Digit': digit_error,
        'Uppercase': uppercase_error,
        'Lowercase': lowercase_error,
        'Symbol': symbol_error,
        'Common Password': common_error
    }

    strong = not any(errors.values())

    return strong, errors

# Main program
password = input("Enter your password to check: ")
strength, details = check_password_strength(password)

if strength:
    print("✅ Your password is strong.")
else:
    print("❌ Your password is weak due to:")
    for issue, occurred in details.items():
        if occurred:
            print(f" - {issue}")