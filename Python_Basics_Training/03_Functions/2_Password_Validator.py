s = input("Enter a password: ")

def validate_password(**kwargs):
    password = kwargs.get('password')  
    if not password:  
        return False
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

print(validate_password(password=s))