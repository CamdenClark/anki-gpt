import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def swap_user_assistant(message):
    message["role"] = "user" if message["role"] == "assistant" else "assistant"
    return message


def get_completion(messages):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=messages)
    return completion.choices[0].message


def continue_conversation(messages):
    messages = list(map(swap_user_assistant, messages))
    messages += [get_completion(messages)]
    return messages


def create_message(content):
    return {"role": "user", "content": content}


def start_conversation(prompt):
    return get_completion([create_message(prompt)])


# let's start

with open('creator.md', 'r') as file:
    creator_prompt = file.read()

first_card = start_conversation(creator_prompt)
print(first_card["content"])

with open('critic.md', 'r') as file:
    critic_prompt = file.read()
    critic_prompt += "\n" + first_card["content"]

critic_response = start_conversation(critic_prompt)
critic_response["content"] += "\nRemember to output your card in json format."
print(critic_response["content"])

final_card = continue_conversation([create_message(creator_prompt)] +
                                   [first_card] +
                                   [critic_response])[-1]["content"]
print(final_card)
