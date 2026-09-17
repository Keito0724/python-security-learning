def has_number(password):
    for char in password:
        if char.isdigit():
            return True

    return False


def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True

    return False


def has_lowercase(password):
    for char in password:
        if char.islower():
            return True

    return False


def has_symbol(password):
    for char in password:
        if not char.isalnum():
            return True

    return False


def check_strength(password):
    password_length = len(password)

    number = has_number(password)
    upper = has_uppercase(password)
    lower = has_lowercase(password)
    symbol = has_symbol(password)

    if password_length >= 12 and number and upper and lower and symbol:
        return "Strong"
    elif password_length >= 8 and number and upper and lower and symbol:
        return "Medium"
    else:
        return "Weak"


password = input("Password: ")

result = check_strength(password)

print(f"Result: {result}")