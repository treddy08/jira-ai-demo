"""
Simple authentication module for demo purposes
"""

def validate_login(username, password):
    """Validate user login credentials"""
    if username == "" or password == "":
        return False

    # TODO: Add actual password validation
    if username == "admin" and password == "password":
        return True

    return False


def main():
    print("Authentication Demo")
    result = validate_login("admin", "password")
    print(f"Login result: {result}")


if __name__ == "__main__":
    main()
