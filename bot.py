# bot.py
import openai

openai.api_key = "YOUR_API_KEY"  # Replace with your OpenAI API key

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
