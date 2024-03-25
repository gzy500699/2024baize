from openai import OpenAI
from .gpt import  create_assistants,create_thread,run_assistant,retrieve_run,list_run_steps,list_messages
import httpx

class Assistants:
    def __init__(self, api_key:str=None, instructions:str=None,model = 'gpt-3.5-turbo',
                  tools=None, file_path:str = None, name:str = "Help assistant",) -> None:
        if api_key is None:         #初始化Client
            self.client: OpenAI = None
        else :
            self.client = OpenAI(
                base_url="https://api.xiaoai.plus/v1", 
                api_key=api_key,
                http_client=httpx.Client(
                    base_url="https://api.xiaoai.plus/v1",
                    follow_redirects=True, 
                    )
                ,
                )
        #初始化assistant
        if self.client is None:
            self.assistant = None
        else:
            self.assistant = create_assistants(self.client,instructions, model, tools, file_path, name)
        self.thread = []