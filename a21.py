from ai21 import AI21Client
from ai21.models.chat import UserMessage
import json
with open('cred.json') as f:
    config = json.load(f)
# Initialize the AI21 client with the API key
API_KEY = config["AI21_KEY"]
client = AI21Client(api_key=API_KEY)

def single_message_instruct(question):
    messages = [
        UserMessage(
            content=question
        )
    ]

    response = client.chat.completions.create(
        model="jamba-1.5-large",
        messages=messages,
        top_p=1.0
    )

    # Extracting the content from the response
    answer = response.choices[0].message.content
    return answer

ans = single_message_instruct("Explain photosynthesis.")


