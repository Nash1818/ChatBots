# pip install openai package from the terminal....

import openai

with open('hidden.txt') as file:
    openai.api_key = file.read()

def get_api_response(prompt: str) -> str or None:
    text: str or None = None

    try:
        response: dict = openai.Completion.create(
            model = 'gpt-3.5-turbo', # the name of the model
            prompt = prompt,
            temperature = 0.9,
            max_tokens = 150,  # kind of a maximum length for the response
            top_p = 1,
            frequency_penalty = 0.0, # reduces the verbatum line repetition
            presence_penalty = 0.6, # reduces the repetition of the same idea
            stop = [' Human:', ' AI:'] # stop the response at the end of the line
        )

        """ print(response) """
        
        choices: dict = response.get('choices')[0]
        text = choices.get('text')

    except Exception as e:
        print ("UH OH: ", e)

    return text

def update_list(message: str, pl: list[str]):
    pl.append(message)

def create_prompt(message: str, pl: list[str]) -> str:
    pmessage: str = f'\nHuman: {message}'
    update_list(pmessage, pl)
    prompt: str = ''.join(pl)
    return prompt


def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)

    if bot_response:
        update_list(bot_response, pl)
        pos: int = bot_response.find('\nAI: ')
        bot_response = bot_response[pos+5:] # so that everything appears clean..
    else:
        bot_response = ' Sorry mate something went wrong.. '
    
    return bot_response

def main():
    # Now for training the bot for eg. you can make it a cool guy saying samjha kya at the end every time..
    prompt_list: list[str] = ['You will pretend to be a Cool Indian guy that says "Samjha kya" at the end of every response',
                              '\nHuman: Hi, I am KingZzee',
                              '\nAI: Yo Waddup, samjha kya']
    
    # Waits for your input and executes the command
    while True:
        user_input: str = input('You: ')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Bot: {response}')
        # print(prompt_list) -> In order to display the prompts already done...
        # It also uses it for its training of its api..
if __name__ == '__main__':
    main()


"""if __name__ == '__main__':
    prompt = " Howdie fella I am KingZzee .. "
    print(get_api_response(prompt))"""
