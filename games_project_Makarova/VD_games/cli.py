def welcome_user():

    print("brain-games")
    print("Welcome to the Brain Games!")
    
    user_name = input("May I have your name? ").strip()
    if not user_name:
        user_name = "Guest"

    print(f"\n Hello, {user_name}!")
