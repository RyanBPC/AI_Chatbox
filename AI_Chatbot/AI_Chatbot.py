# Step 1: Import the libraries
import os
from dotenv import load_dotenv
from groq import Groq

# Step 2: Load API key from Api_Key.env file
load_dotenv()

# Step 3: Connect to Groq
client = Groq()

print("=" * 40)
print("               AI CHATBOT")
print("=" * 40)
print()

# Step 4: Check if API key exists
if not os.getenv("GROQ_API_KEY"):
    print("Error: No API key found!")
    print("Please create a .env file with: GROQ_API_KEY=your_key_here")
    exit()

print("Bot: Hello! \U0001F44B I'm your friendly AI assistant. Type 'bye' to exit.")
print()

# Step 5: Main loop - keeps the chatbot running
while True:
    user_input = input("You: ")

    # Check if user wants to quit the program
    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    try:
        # Step 6: Send message to Groq and get response
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": user_input}]
        )

        # Step 7: Print the AI's response
        bot_response = response.choices[0].message.content
        print(f"Bot: {bot_response}")
        print()

    except Exception as e:
        print(f"Bot: Sorry, something went wrong! Error: {e}")
        print()