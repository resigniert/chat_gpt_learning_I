import openai
import os
import input


my_secret = os.environ['open_ai_GPT_key_I']
openai.api_key = my_secret


response = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  messages = [
    {
      "role": "user",
      "content": input.input_I
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

response_message = response["choices"][0]["message"]["content"]

print(response_message)