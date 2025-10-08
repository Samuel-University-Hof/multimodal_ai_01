from transformers import pipeline
import torch


pipe = pipeline("text-generation", model="google/gemma-3-1b-it", device="cuda", torch_dtype=torch.bfloat16)

def format_question(question:str):
    messages = [
        [
            {
                "role": "system",
                "content": [{"type": "text", "text": "You are a helpful assistant."},] #Tell the model your instructions
            },
            {
                "role": "user",
                "content": [{"type": "text", "text": question},]
            },
        ],
    ]

    return messages

while True:
    question = input("Type your Question: ")
    question_formatted = format_question(question)
    answer = pipe(question_formatted, max_new_tokens=1024)
    print(answer[0][0]["generated_text"][-1]["content"])
    print("-"*30)