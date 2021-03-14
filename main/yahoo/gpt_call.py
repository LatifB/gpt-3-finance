import os
import openai

class OpenAi():

    def __init__(self, engine='davinci', temperature=0.3, max_tokens=60, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0):
        self.token = os.environ["OPEN_AI_TOKEN"]
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

        openai.api_key = self.token
    
    def sum_call(prompt):
        response = openai.Completion.create(
        engine=self.engine,
        prompt=prompt,
        temperature=self.temperature,
        max_tokens=self.max_tokens,
        top_p=self.top_p,
        frequency_penalty=self.frequency_penalty,
        presence_penalty=self.presence_penalty)

        return response.replace('\n', '').split().join(' ')

    def sent_call(prompt):
        response = openai.Completion.create(
        engine=self.engine,
        prompt=prompt,
        temperature=self.temperature,
        max_tokens=self.max_tokens,
        top_p=self.top_p,
        frequency_penalty=self.frequency_penalty,
        presence_penalty=self.presence_penalty)
        stop=['\n']

        return response
