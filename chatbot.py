import random

user_needs = {
    "greeting": ["hello", "hi", "hey"],
    "farewell": ["goodbye", "bye", "see you"],
    "purpose": ["tell a joke", "provide information", "chat"]
}

personality = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you today?"],
    "farewell": ["Goodbye!", "Have a great day!", "See you later!"],
    "purpose": [
        "Sure, I can tell you a joke. Why did the chicken cross the road? To get to the other side!",
        "Of course! What information do you need?",
        "Let's chat! How's your day going?"
    ]
}


def chatbot_response(user_input):
    for intent, keywords in user_needs.items():
        if any(keyword in user_input.lower() for keyword in keywords):
            return random.choice(personality[intent])
    return "I'm not sure how to respond to that."

print("Chatbot: Hi there! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ").lower()
    if user_input == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
