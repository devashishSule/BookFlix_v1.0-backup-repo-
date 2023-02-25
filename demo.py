import openai

API_KEY = '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'
openai.api_key = API_KEY
model='text-davinci-003'
response = openai.Completion.create(
    prompt='How big is the moon',
    model=model,
    max_tokens = 1000,
    temperature = 0.9
)
print(response)