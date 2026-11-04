import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    #Check Length
    if len(password)>=8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters.")
    
    #Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Uppercase letters missing")
    
    #Lowercase check
    if re.search(r"[a-z]", password):
        strength+=1
    else:
        feedback.append("lowercase letter missing")
    
    
    if re.search(r"\d",password):
        strength+=1
    else:
        feedback.append("Add at least one digit")
    if re.search(r"[@$!%*?&]", password):
        strength+=1
    else:
        feedback.append("Add one of them [!@#%*?$&] ")
    
    if strength == 5:
        return "Strong Password"
    else:
        return "Weak Password. "+" ".join(feedback)
    

password = input("Enter Your Password: ")

print(check_password_strength(password))