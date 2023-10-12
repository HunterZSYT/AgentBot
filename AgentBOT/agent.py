import openai
openai.api_type = "azure"
openai.api_base = "https://huntergpt.cognitiveservices.azure.com/"
openai.api_version = "2023-07-01-preview"
openai.api_key = "2263b46af7724eb7a3e611fd828a4379"

    

response = openai.ChatCompletion.create(
    engine="HunterOAI",
    messages=[{"role": "system", "content": "You are an AI assistant that helps people find information."}],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)

if 'text' in response['choices'][0]:
    print(response['choices'][0]['text'])
else:
    print("No text returned by the API.")

