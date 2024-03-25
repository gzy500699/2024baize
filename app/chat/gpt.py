from openai import OpenAI
from .gpt_utils import create_file

'''
简单的API调用
'''
# 单条信息对话
def get_completion(client:OpenAI,prompt,model,temperature):
    messages = [{"role":"user","content":prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature = temperature
    )
    # print(response.choices[0].message.content)
    return response

# 上下文对话
def get_completion_from_messages(client:OpenAI,messages,model,temperature):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature= temperature
    )
    # print(response.choices[0].message.content)
    return response

#使用stream接收
def get_stream_completion(client:OpenAI,prompt,model,temperature):
    messages = [{"role":"user","content":prompt}]
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        stream = True,
        temperature = temperature
    )
    for chunk in response:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content,end='')
    return response
    
    
#使用stream的上下文对话

#输入图像和文字的对话
def get_completion_from_images(client:OpenAI,prompt,model="gpt-4-vision-preview",temperature = 0.7):
    response = client.chat.completions.create(
        model=model,
        messages=prompt,
        temperature = temperature,
        max_tokens= 3000,
    )

    return response


'''
ASSISTANTS API相关
'''
#设置代理机器人
def create_assistants(client:OpenAI, instructions, model, tools=[], file_path= [], name = "Help assistant"):
    if file_path != []:
        file_ids = create_file(file_path)
    else:
        file_ids = []
    assistant = client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=tools,
        model=model,
        file_ids=file_ids,
    )
    return assistant

#创建线程
def create_thread(client:OpenAI,prompt,file_ids=[]):
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
                "file_ids": file_ids,
            }
        ]
    )
    return thread
    
#运行线程和助手
def run_assistant(client:OpenAI,thread, assistant):
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )
    return run

#返回run相关信息
def retrieve_run(client:OpenAI,thread, run):
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    return run

#返回run的每一步
def list_run_steps(client:OpenAI,thread, run):
    run_steps = client.beta.threads.runs.steps.list(
        thread_id=thread.id,
        run_id=run.id,
    )
    return run_steps

#返回信息
def list_messages(client:OpenAI,thread):
    thread_messages = client.beta.threads.messages.list(thread_id=thread.id)
    return thread_messages