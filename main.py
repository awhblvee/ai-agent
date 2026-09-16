import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
import argparse
import prompts
from call_function import available_functions, call_function
import json

def main():
    load_dotenv()
    parser  = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY environment variable is not set. Please set it in your .env file.")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    messages=[
        {"role": "system","content": prompts.system_prompt},
        {"role": "user","content": args.user_prompt},
    ]
    max_iterations = 20
    for i in range(max_iterations):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            temperature=0,
            tools=available_functions
        )
        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            if message.content:
                print(f"Final response: {message.content}")
            else:
                print("Final response: (No content returned)")
            return

        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)
            messages.append(result_message)
            if args.verbose:
                print(f"-> {result_message['content']}")
    print("Error: Reached maximum iterations without a final response.")
    sys.exit(1)

if __name__ == "__main__":
    main()
