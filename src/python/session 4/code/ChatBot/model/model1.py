'''
file for the Function to get a response based on user input
'''



import random
import json

with open("C:/Users/Froze/OneDrive/Attachments/Desktop/cairo_depi-ai/CA-R5-S2S2-AI/src/python/session 4/code/ChatBot/model/data.json", "r") as file:
    responses = json.load(file)

def get_response(user_input):
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])