"""
Just creating chatbot using LLM API (openai python sdk) with error handling
"""

import os
from dotenv import load_dotenv

from openai import OpenAI, APIConnectionError, RateLimitError, APIStatusError

load_dotenv()


# API_KEY = os.getenv("OPENAI_API_KEY"),
API_KEY = ""
MODEL = os.getenv("MODEL", "gpt-4.1-mini")

if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")

if not MODEL:
    raise ValueError("MODEL not found in environment variables. Please set it in your .env file.")

#create the OPENAI Client
client = OpenAI(api_key=API_KEY)

#define the system prompt
SYSTEM_PROMPT = """
You are a helpful AI assistant and Python teacher.
Explain concepts clearly using beginner-friendly language.
Give practical examples when useful.
If you are unsure about something, say so.

"""

#store converwsation messagees
history = []

def ask_chatbot(question):
    """ 
    Send q question to model and retunr respoonse

    """
    
    #append user question to history
    history.append({"role": "user", "content": question})

    try:
        response = client.responses.create(
            model = MODEL,
            instructions = SYSTEM_PROMPT,
            input = history,
        )

        answer = response.output_text

        #save answer to history
        history.append({"role": "assistant", "content": answer})

        return answer

    except RateLimitError:
        history.pop()
        return "Rate limit exceeded. Please try again later."
    except APIConnectionError:
        history.pop()
        return "Connection error. Please check your internet connection and try again."
    except APIStatusError as e:
        history.pop()
        return f"API status error: {e}. Please try again later."


def main():
    print("=" * 45)
    print("  OPENAI PYTHON CHATBOT")
    print("=" * 45)
    print(f"model: {MODEL}")
    print("Type 'exit' to quit the chatbot.")
    print("Type 'clear' to clear the conversation history.")



    while True:
        question = input("\nYou: ").strip()


        if not question:
            print("Please enter a question.")
            continue

        if question.lower() == "exit":
            print("Exiting the chatbot. Goodbye!")
            break

        if question.lower() == "clear":
            history.clear()
            print("Conversation history cleared.")
            continue
        answer = ask_chatbot(question)
        print(f"\nBot: {answer}")

if __name__ == "__main__":
    main()


