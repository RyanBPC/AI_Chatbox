# AI Chatbot (Python)

An AI chatbot I built because I was curious about how AI APIs actually work. I wanted to know what happens behind the scenes when people use an AI like ChatGPT.

It's a simple command-line chatbot that connects to Groq's free AI API and lets you have a proper conversation with an AI. I added some addition comments throughout the code to support anyone who doesn't understand or is just starting out as a programmer.

---

## What It Does

- Connects to Groq's free AI API
- Has real-time conversations with an AI assistant
- Keeps your API key safe in a '.env' file (don't share with others)
- Has step-by-step comments
- Runs in the command-line

It's just a miniature, text-based chatbot that I built from scratch.

---

## Why I Made It

To be honest, I just wanted to prove to myself that I could:

- Work with a real API
- Handle sensitive stuff like API keys properly
- Get a better grasp of how AI models work

Throughout this project, it taught me a lot about how AI APIs work and how to structure a Python program with AI, other people can use.

---

## How It's Laid Out

```
AI_Chatbot/
│
├─ .env               # Your API key (keep this secret from everyone!)
└─ AI_Chatbot.py      # The main chatbot code file
```

Each file does its own thing, and together they make the chatbot program work.

---

## How To Use It

1. **Download my files off GitHub**
   - Go into the AI_Chatbot folder
   - Download both AI_Chatbot.py and .env files
   - Open both these files in your IDE (I used PyCharm)

2. **Install the dependencies**
   - Open the terminal in your IDE
   - Run this:
     ```bash
     pip install groq python-dotenv
     ```
   - Give it a minute to install

3. **Get your Groq API key**
   - Go to console.groq.com
   - Sign up or log in (it's completely free)
   - Click API Keys
   - Click Create API Key
   - Copy the key (it'll start with the letters gsk_)

4. **Create a .env file**
   - Go into the .env file you downloaded
   - Swap out ```your_groq_api_key_goes_here``` with the key you just made
   - Save it

5. **Run the chatbot**
   - Open the terminal in your IDE
   - Run AI_Chatbot.py
   - The chatbot should then start up

6. **Have a chat with the AI assistant**
   - You'll see something like this:

     <img width="1162" height="197" alt="Chatbot Running" src="https://github.com/user-attachments/assets/ee678740-ff27-42e5-a18e-e67bcb280c8d" />

   - Type your question and hit Enter
   - The AI will then reply!
   - Once your done, type "bye"

---

## If Something Goes Wrong

Problem -> Solution:

```pip is not recognised``` -> Use ```python -m pip install groq python-dotnev``` instead

```No module named 'qroq'``` -> Make sure you ran ```pip install groq python-dotnev```

```Error: No API key found!``` -> Check that your .env file is in the right place

```.env file not working``` -> Make sure it's called exactly .env (not another file name)
  
---

## What A Conversation Looks like

<img width="1502" height="382" alt="Terminal Definition" src="https://github.com/user-attachments/assets/7474602a-8a85-4f36-8574-743c381aabda" />

---

## One Important Thing

Please don't share your own personal .env file or API key with anyone at all!

- Don't upload .env to GitHub
- Don't send screenshots of your personal .env file
- If you do accidentally leak your key, delete the old and make a new one immediately

## Stuff I Might Add Later

- A proper GUI
- Conversation history
- Support for different AI models
- Saving chats between sessions

There's no doubt about it that I can take this even further and I would love to do so in the near future.

---

## Final Thoughts

This was genuinely a fun project to create and it helped me a lot on understanding how AI APIs actually work. Anyone who is looking at my work, thank you for taking your time to check it out. Please leave me any feedback or ideas, since I'm always attempting to learn more!
