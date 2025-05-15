print("BPassword Strength Checker")

# Ask user to enter a password
password = input("Enter your password: ")

# Just show what was typed
print(f"You entered: {password}")

# Check password length
if len(password) < 8:
    print("Warning: Your password is too short. Try to use at least 8 characters.")
else:
    print("Length OK.")

    import string

# Initialize score and flags
score = 0

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in string.punctuation for char in password)

# Check each type and update score
if has_upper:
    score += 1
    print("Contains uppercase letter.")
else:
    print("No uppercase letter.")

if has_lower:
    score += 1
    print("Contains lowercase letter.")
else:
    print("No lowercase letter.")

if has_digit:
    score += 1
    print("Contains a digit.")
else:
    print("No digit.")

if has_symbol:
    score += 1
    print("Contains a symbol.")
else:
    print("No symbol.")

    # Final rating
print("\n🔎 Password Strength:")

if score <= 2 or len(password) < 8:
    print("Weak")
elif score == 3:
    print("Medium")
elif score == 4 and len(password) >= 12:
    print("Strong 💪")
else:
    print("Fair, improve length or add more variety")