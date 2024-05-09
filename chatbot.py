import random
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "who are you": ["I am Chatbot!", "AI"],
    "who is created you":["Utkarsh Barapatre"],
    "told some about him":["Sorry, I am not provied any personal information about him"],
    "how are you": ["I'm good, thanks!", "I'm doing well, thank you!"],
    "ok":["ok", "ok!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    
    "default": ["Sorry, I don't understand.", "Could you please repeat that?", "I'm not sure what you mean."]
}

def get_response(message):
    message = message.lower()
    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

def main():
    print("Welcome to the ChatBot!")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print(get_response("bye"))
            break
        else:
            print("Bot:", get_response(user_input))

if __name__ == "__main__":
    main()
