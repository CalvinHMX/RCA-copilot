from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "can you tell how to fine tuning llm."}
  ]
)

print(completion.choices[0].message)



# def example():
#     instrctuction='i want to learn AIGC'
#     prompt=f"""{instrctuction}"""
#     response = getResponse(prompt)
#     print(response)

# def getResponse(prompt, model='gpt-3.5-turbo'):
#     messages =[{
#         "role": "system", "content": "You are a assistant.",
#         'role':'user',
#         'content':prompt
#     }] 
#     response = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=0.7
#     )
#     return response.choices[0].message
# example()