#!/usr/bin/env python

import openai
import os
import argparse
from src.stream import MarkfownStream, KeyboardStream, PlainStream

openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = "gpt-3.5-turbo"
system_prompt = """
Your are a bash command expert. You take user's question as input, and output the CLI command as answer. 
For example, if the user asks "How to list all files in a directory?", you should output `ls -l`. 
If the question is not about cli, you should output "Sorry, I don't know the answer to that question.".
"""

conditional_prompt = """
ONLY output the command itself. Do not output any other text
"""

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
        help="type the command directly to the terminal",
    )
    parser.add_argument(
        "-i", "--info", action="store_true", default=True, help="get the information about the command"
    )
    parser.add_argument(
        "-m", "--markdown", action="store_true", help="show markdown syntax hightlighting"
    )
    parser.add_argument("text", nargs="+", help="the question to ask")

    args = parser.parse_args()

    text = " ".join(args.text)
    
    if args.command:
        stream = KeyboardStream()
    elif args.markdown:
        stream = MarkfownStream()
    else:
        stream = PlainStream()

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

    for chunk in completion:
        if "content" in chunk.choices[0].delta.keys():
            stream.output(chunk.choices[0].delta.content)

    stream.close()

if __name__ == "__main__":
    main()
