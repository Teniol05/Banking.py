def login():
    password_verified = False
    username_verified = False

    while not password_verified:
        password = input("choose password: ")
        verify_password = input("Verify password: ")

        if password == verify_password:
            password_verified = True
        else:
            print("Invalid password. Please try again.")

    while not username_verified:
        username = input("choose  username: ")
        verify_username = input("Verify username: ")

        if username == verify_username:
            username_verified = True
        else:
            print("Invalid username. Please try again.")

    while True:
        entered_username = input("Enter username: ")
        entered_password = input("Enter password: ")

        if entered_username == username and entered_password == password:
            print("Successfully logged in!")
            break0
        else:
            print("Incorrect username or password. Please try again.")

