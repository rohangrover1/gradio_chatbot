import os
import sys
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import langchain


# create the chatbot class
class chatbot():
    def __init__(self, llm_model):
          self.open_ai_key_str = None
          self.chat = None
          self.chat_personality = None
          self.llm_model = llm_model
          self.template_string = ""
          self.prompt_template = None
          self.debug = False

    def set_open_ai_key(self, key):
         self.open_ai_key_str = key
         print("open_ai key set")

    def set_chatbot_personality(self, personality):
         self.chat_personality = personality
         print("chatbot personality set")


    def initialize_chatbot(self):
        try:
            if self.open_ai_key_str==None:
                return("please add you open_ai key to proceed")

            self.chat = ChatOpenAI(
                openai_api_key=self.open_ai_key_str,
                temperature=0.0, 
                model=self.llm_model,
                max_tokens=None,
                timeout=None,
                max_retries=2)
             
            if self.chat_personality==None:
                self.template_string = """You are a chatbot. \
                            Answer the question that is delimited by triple backticks.\
                            text: ```{text}```
                          """
            else:
                main_str = f"You are a chatbot behaving as {self.chat_personality}.\n"
                query_str = """Answer the question that is delimited by triple backticks.\
                            text: ```{text}```"""
                self.template_string = main_str + query_str
            
            print(self.template_string)
            self.prompt_template = ChatPromptTemplate.from_template(self.template_string)
            return("chatbot initialized")

        except Exception as e:
                print('file:{} line:{} type:{}, message:{}'.format(
                     os.path.basename(__file__), sys.exc_info()[-1].tb_lineno, type(e).__name__, str(e)))


    def execute_chat(self, input_text):
        try:

            if self.open_ai_key_str==None:
                return("please add you open_ai key in the box above")

            if self.debug:
                 langchain.debug=True

            input_messages = self.prompt_template.format_messages(text=input_text)
            response = self.chat(input_messages)

            if self.debug:
                 langchain.debug=False

            return(response.content)
        except Exception as e:
            print('file:{} line:{} type:{}, message:{}'.format(
                     os.path.basename(__file__), sys.exc_info()[-1].tb_lineno, type(e).__name__, str(e)))




            
        


