import re
def chatbot_response(userinput):
    userinput = userinput.lower()
    if "hello" in userinput or "hi" in userinput:
        return "Hello!! How can I assist you?"

    elif "how are you" in userinput:
        return "I'm just a bot, but I'm doing fine. what about you?"

    elif "name" in userinput:
        return "My name is Nova,but you can call me whatever you like!"

    elif "bye" in userinput or "exit" in userinput:
        return "Goodbye! Have a great day!"
    elif re.search(r"weather|forecast", userinput):
        return "I can't check the weather right now, but you can always check it online!"
    
def start_chat():
    print("Chatbot: Hello! I'm here to assist you. Type 'exit' to end the conversation.")
    
    while True:
        userinput = input("You: ")
        if userinput.lower() in ["exit", "bye"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(userinput)
        print("Chatbot:", response)
start_chat()
