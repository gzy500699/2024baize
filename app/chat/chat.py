from openai import OpenAI
from .gpt import get_completion_from_messages
from .gpt import get_completion_from_images
import httpx
class Chat:
    def __init__(self, api_key = None, memory= False,system_settings=[],) -> None:
        self.conversation_list = system_settings  # 初始化对话列表，可以引入初始化prompt
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
        self.memory = memory

    # 打印对话
    def show_conversation(self, msg_list):
        for msg in msg_list[-2:]:
            if msg['role'] == 'user':  # 如果是用户的话
                # print(f"\U0001f47b: {msg['content']}\n")
                pass
            else:  # 如果是机器人的话
                message = msg['content']
                print(f"{message}")
    '''
    通过简单的API调用GPT
    '''
    def ask_txt(self, prompt,model="gpt-3.5-turbo",temperature = 0.7):
        self.conversation_list.append({"role": "user", "content": prompt})
        response = get_completion_from_messages(self.client, self.conversation_list,model,temperature)
        answer = response.choices[0].message.content
        if self.memory == False:
            print(answer)
            del self.conversation_list[-1]
        else:
            #将回答加入列表中
            self.conversation_list.append({"role": "assistant", "content": answer})
            self.show_conversation(self.conversation_list)
    
    #带图片的调用
    def ask_images(self,massage:list,model="gpt-4-vision-preview",temperature = 0.7):
        prompt=[{"type": "text", "text": massage[0]},
                {"type": "image_url","image_url":{"url":f"data:image/png;base64,{massage[1]}"}}]
    
        self.conversation_list.append({"role": "user", "content": prompt})
        response = get_completion_from_images(self.client, self.conversation_list,model,temperature)
        answer = response.choices[0].message.content
        if self.memory == False:
            print(answer)
            del self.conversation_list[-1]
        else:
            #将回答加入列表中
            self.conversation_list.append({"role": "assistant", "content": answer})
            self.show_conversation(self.conversation_list)

    #带插件的调用 
    def ask_tools(self,tool,prompt,image_path = None):
        pass



def main():
    api_key = "xxx"
    talk = Chat(api_key=api_key)
    print()
 
    count = 0
    count_limit = eval(input("你想要对话的次数是多少呢？\n(请输入数字即可)"))
    while count < count_limit:
        if count < 1:
            words = input("请问有什么可以帮助你的呢？\n(请输入您的需求或问题)：")
        else:
            words = input("您还可以继续与我交流，请您继续说：\n(请输入您的需求或问题)：")
        print()
        talk.ask_txt(words)
 
if __name__ == "__main__":
    main()