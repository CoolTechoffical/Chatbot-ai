# bot.py
import os
import openai

# Load environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")
api_hash = os.environ.get("API_HASH")
api_id = os.environ.get("API_ID")
bot_token = os.environ.get("BOT_TOKEN")

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
    )
    return response.choices[0].text.strip()

def main():
    print("ChatGPT Bot: Hello! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("ChatGPT Bot: Goodbye!")
            break
        
        prompt = f"You: {user_input}\nChatGPT Bot:"
        bot_response = chat_with_gpt(prompt)
        
        print(f"ChatGPT Bot: {bot_response}")

if __name__ == "__main__":
    main()
