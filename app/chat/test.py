from .gpt import get_completion
from .gpt import get_stream_completion
from openai import OpenAI

client = OpenAI(api_key = "xxx")
def task1():
    text = f"""
    You should express what you want a model to do by providing instructions \
    that are as clear and specific as you can possibly make them.This will guide the model towards the \
    desired output,and reduce the chances of receiving irrelevantor incorrect responses,Don't confuse writing \
    aclear prompt with writing a short prompt.In many cases,longer prompts provide more clarityand context for the model,  \
    which can lead to more detailed and releant outputs.
    """
    
    prompt = f"""
    Summarize the text delimited by triple backticks into a single sentence.
    ```{text}```
    """
    response = get_completion(client,prompt)
    print(response.choices[0])

def task2():

    prompt = f"""
    Generate a list of three made-up book titles along with their authors and genres. \
    Provide them in JSON format with the following keys:book id,title,author,genre.
    """
    get_stream_completion(client,prompt)



if __name__ == '__main__':
    task2()