print("Welcome to BuggyBot! (type 'bye' to exit)")

user_input = ""   # Initialize
while user_input != "bye":
    user_input = input("You: ")  
    
    if user_input == "hi" or user_input == "hello":   
        print("Bot: Hello there!")
    elif user_input == "bye":
        print("Bot: Goodbye!")
    else:
        print("Bot: I don’t understand.")