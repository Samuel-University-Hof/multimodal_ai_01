import requests

api_token = None
url = None
with open("api_token.txt", encoding="UTF-8") as rf:
    api_token = rf.read().strip()

with open("url.txt", encoding="UTF-8") as rf:
    url = rf.read().strip()


def ask_lisa(question: str) -> str:
    global url
    global api_token

    model: str = "qwen/qwen3-next-80b"
    headers = {'Authorization': f'Bearer {api_token}',
                "Content-Type": "application/json"}
    data = {
        "model": model,
        "messages": [
        {
          "role": "user",
          "content": question
        }
      ]
    }
    response = requests.post(url, json=data, headers=headers)

    print("Response status code:", response.status_code)

    data = response.json()["choices"][0]["message"]["content"]

    return str(data)

while True:
    question = input("Type your Question: ")
    answer = ask_lisa(question)
    print(answer)
    print("-"*30)