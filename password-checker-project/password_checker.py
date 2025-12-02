import string

def check_password_strength(password):
    score = 0
    suggestions = []
    #  check for length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase the lenght of your password to at least 8 characters")

    
    #  check for upper case
    if any(char.isupper() for char in password):
        score +=1
    else:
        suggestions.append("add at least one uppercase letter")

    #  check for lower case
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("add at least one lowercase letter")

    #  digit check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("add at least one digit")
    
    # symbol check
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("add at least one special character")

    return score, suggestions


# main
password = input("Enter your password: ")
score, suggestions = check_password_strength(password)

print(f"Password Strength Score: {score}/5")

if score == 5:
    print("Strong passsword!")
else:
    print("weak password. Suggestions to improve:")
    for suggestion in suggestions:
        print(f"- {suggestion}")