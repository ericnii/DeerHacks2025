from openai import OpenAI

client = OpenAI(
    api_key=''
)

prompt = "who is the president of Canada?"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role":"user",
            "content":"prompt"
        }
    ],
    model="gpt-3.5-turbo"

)

print(chat_completion.choices[0].message.content)