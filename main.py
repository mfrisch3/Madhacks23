import openai
# from dotenv import load_dotenv

import os


# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = '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'
try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Translate the following English text to French: 'Hello, how are you?'",
        max_tokens=60
    )

    generated_text = response['choices'][0]['text']
    print(generated_text)

except Exception as e:
    print(f"An error occurred: {e}")
