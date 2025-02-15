from openai import OpenAI

client = OpenAI(
    api_key='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'
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