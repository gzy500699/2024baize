import base64
"""
translation model
"""
#prompt for system
def translate_init(choice = ['English','chinese'])->dict:
    prompt = f"""\
You should work as a translation experts.\
"""
    return [{'role':'system','content':prompt}]

#prompt for user
def translate(content: str,language) -> dict:
    prompt = f"""\
You should translate the text delimited by triple backticks ``` into {language}.
```{content}```\
    """
    return prompt