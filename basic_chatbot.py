# Basic Chatbot

def chatbot():
    print("🤖 Welcome to Simple Chatbot!")
    print("Type 'bye' to exit the chat.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thank you! How about you?")

        elif user == "what is your name":
            print("Bot: My name is Simple Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "what can you do":
            print("Bot: I can answer simple predefined questions.")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()