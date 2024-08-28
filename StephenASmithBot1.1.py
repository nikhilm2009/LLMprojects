from openai import OpenAI
import gradio as gr

#OPENAI_API_KEY
client = OpenAI()
GPT_MODEL = "gpt-4o"
messages = [
    {"role": "system", "content": "You are Stephen A Smith from ESPN's first take.answer everything with Basketball references and ramble a bit"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = client.chat.completions.create(
            model=GPT_MODEL, 
            messages=messages, 
            temperature=0.9
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply
    
inputs = gr.Textbox(lines=7, label="Chat with Nikhils Mark Robe Chatbot ")
outputs = gr.Textbox(label="Reply")


gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Nikhil's MarkRobot  ",
             description="Ask anything you want",
             theme="compact").launch(share=True)
