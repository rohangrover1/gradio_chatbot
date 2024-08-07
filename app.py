import os
import sys
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import ChatPromptTemplate
import gradio as gr
from chatbot import chatbot

     
# # get the open_ai api key
# _ = load_dotenv(find_dotenv()) # read local .env file
# openai_api_key_str = os.environ['OPENAI_API_KEY']
# print(openai_api_key_str)

llm_model = "gpt-3.5-turbo"
chatObj = chatbot(llm_model=llm_model)             # create chat object 

# def init_chatbot():
#     try:
#         response = "hello world"
#         #response = chatObj.initialize_chatbot()
#         return(response)
#     except Exception as e:
#             print('line:{} type:{}, message:{}'.format(sys.exc_info()[-1].tb_lineno, type(e).__name__, str(e)))


# def run_chatbot(input_str):
#     try:
#         return(chatObj.execute_chat(input_str))
#     except Exception as e:
#             print('line:{} type:{}, message:{}'.format(sys.exc_info()[-1].tb_lineno, type(e).__name__, str(e)))


if __name__ == "__main__":
    try:
        # setup the gradio chatbot
        with gr.Blocks() as demo:
            with gr.Row():
                with gr.Column(scale=1, variant="compact"):
                    gr.Markdown("Enter you open API key")
                    inp = gr.Textbox(placeholder="open API Key")                
                    btna = gr.Button("Enter")
                btna.click(fn=chatObj.set_open_ai_key, inputs=inp)    

                with gr.Column(scale=1, variant="compact"):
                    gr.Markdown("Enter chatbot personality")
                    inp = gr.Textbox(placeholder="chatbot personality")                
                    btnb = gr.Button("Enter")
                btnb.click(fn=chatObj.set_chatbot_personality, inputs=inp)    

            with gr.Row():
                out_x=gr.Textbox(label="status", scale=1),
            btn1 = gr.Button("Initialize chatbot", scale=1)    
            btn1.click(fn=chatObj.initialize_chatbot, outputs=out_x[0])    

            with gr.Row():
                inputs_x=gr.Textbox(label="what is your question"),
                outputs_x=gr.Textbox(label="answer"),
            btn2 = gr.Button("Run")
            btn2.click(fn=chatObj.execute_chat, inputs=inputs_x[0], outputs=outputs_x[0])

        # demo = gr.Interface(
        #                     fn=get_chat_results,
        #                     inputs=gr.Textbox(label="what is your question"),
        #                     outputs=gr.Textbox(label="answer"),
        #                     )


        demo.launch()

    except Exception as e:
            print('file:{} line:{} type:{}, message:{}'.format(
                     os.path.basename(__file__), sys.exc_info()[-1].tb_lineno, type(e).__name__, str(e)))


