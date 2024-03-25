from openai import OpenAI

def create_file(client:OpenAI,file_path):
    file = client.files.create(file=open(file_path, "rb"), purpose="assistants")
    return file

