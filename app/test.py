from openai import OpenAI
import os
from ruamel.yaml import YAML
import base64
#from prompt.img_exract import img2md
from chat.chat import Chat
from prompt.translation import translate

#环境代理设置
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
CHAT_CONFIG_PATH  = "./app/configs/apiconfig.yaml"

if __name__ == "__main__":
    chat_config =  YAML().load(open(CHAT_CONFIG_PATH))
    api_key = chat_config['API_KEY']
    talk = Chat(api_key=api_key)
    talk.ask_txt(translate('我的窗前有两颗树，一颗是枣树，另一棵也是枣树','English'))
    #talk.ask_txt(translate('my name is mike','Chinese'))
    #talk.ask_images(img2md('./1.png'),model='gpt-4-vision-preview')
    #talk.ask_txt('输出一张猫的照片',model= 'gpt-4-vision-preview')