#!/usr/bin/env python

import sys
from pynput.keyboard import Controller
import openai
import os
import re

openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = "gpt-3.5-turbo"
system_prompt = """
Your are a bash command expert. You take user's question as input, and output the CLI command as answer. 
For example, if the user asks "How to list all files in a directory?", you should output "ls -l". 
You should ONLY output the command. DO NOT output any other text.
"""

keyboard = Controller()

def get_text():
    # Get all command-line arguments except the first (which is the script name)
    return ' '.join(sys.argv[1:])

def generate_prompt(text):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": text}
    ]

def main():
    text = get_text()
    prompt = generate_prompt(text)
    completion = openai.ChatCompletion.create(
        model=model_name, 
        messages=prompt, 
        max_tokens=1024, 
        n=1, 
        stop=None, 
        temperature=0,
        stream=True
    )

    for chunk in completion:
        if "content" in chunk.choices[0].delta.keys():
            keyboard.type(chunk.choices[0].delta.content)

if __name__ == "__main__":
    main()
