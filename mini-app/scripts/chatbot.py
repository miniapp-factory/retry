#!/usr/bin/env python3
"""
A simple chatbot that responds with predefined answers.
"""

import sys

RESPONSES = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bunch of code, but thanks for asking!",
    "what is your name": "I'm Chatbot, your friendly assistant.",
    "bye": "Goodbye! Have a great day!",
}

def get_response(message: str) -> str:
    key = message.lower().strip()
    return RESPONSES.get(key, "Sorry, I don't understand that.")

def main():
    print("Chatbot is running. Type 'bye' to exit.")
    while True:
        try:
            user_input = input("> ")
        except EOFError:
            break
        if user_input.lower().strip() == "bye":
            print(get_response(user_input))
            break
        print(get_response(user_input))

if __name__ == "__main__":
    main()
