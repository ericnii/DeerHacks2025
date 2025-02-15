from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='deepseek-r1:8b', messages=[
  {
    'role': 'user',
    'content': 'who is the president of the philippines?',
  },
])
# print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)