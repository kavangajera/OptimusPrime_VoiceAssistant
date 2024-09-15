"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
import json
import os
import google.generativeai as genai
with open("cred.json") as f:
  config = json.load(f)
  
GENAI_KEY = config["GENAI_KEY"]
  
genai.configure(api_key=GENAI_KEY)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "what is capital of india?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hi there! How can I help you today? \n",
      ],
    },
  ]
)

response = chat_session.send_message("what is capital of Gujarat?")

print(response.text)