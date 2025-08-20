def passwordStrengthChecker(password):
    # write your logic here
    special_chars = "!@#$%^&*"
    if (
        len(password) >= 8
        and any(c in special_chars for c in password)
        and any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
    ):
        return "Strong"
    else:
        return "Weak"


if __name__ == "__main__":
    password = input("Enter password: ")
    result = passwordStrengthChecker(password)
    print(result)
