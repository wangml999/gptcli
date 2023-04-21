#!/usr/bin/env python

import sys
from pynput.keyboard import Controller
import openai
import os
import re
import argparse
import functools

openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = "gpt-3.5-turbo"
system_prompt = """
Your are a bash command expert. You take user's question as input, and output the CLI command as answer. 
For example, if the user asks "How to list all files in a directory?", you should output `ls -l`. 
If the question is not about cli, you should output "Sorry, I don't know the answer to that question.".
"""

conditional_prompt = """
ONLY output the command itself. DO NOT output anything else other than the command.
"""

keyboard = Controller()

def generate_prompt(text, only_command=False):
    prompt = system_prompt
    if only_command:
        prompt += conditional_prompt

    return [
        {"role": "system", "content": prompt},
        {"role": "user", "content": text},
    ]


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "-c",
        "--command",
        action="store_true",
        help="Type the command directly to the terminal",
    )
    parser.add_argument(
        "-i", "--info", action="store_true", default=True, help="Get information about the command"
    )
    parser.add_argument("text", nargs="+", help="The question to ask")

    args = parser.parse_args()

    if len(args.text) == 0:
        print("Please provide a question.")
        return

    text = " ".join(args.text)

    prompt = generate_prompt(text, args.command)
    completion = openai.ChatCompletion.create(
        model=model_name,
        messages=prompt,
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0,
        stream=True,
    )

    if args.command:
        output_func = functools.partial(keyboard.type)
    else:
        output_func = functools.partial(print, end="", flush=True)

    for chunk in completion:
        if "content" in chunk.choices[0].delta.keys():
            output_func(chunk.choices[0].delta.content)

    if not args.command:
        print()
        
if __name__ == "__main__":
    main()
