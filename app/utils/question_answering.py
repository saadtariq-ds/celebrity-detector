"""
Celebrity Question & Answer Engine
"""

import os
import requests
from app.utils.prompts import CELEBRITY_QA_PROMPT

class QAEngine:
    """
    A Question & Answer engine for responding to queries about celebrities
    using a large language model hosted on Groq.
    """
    def __init__(self):
        """
        Initialize the QAEngine.

        Loads the Groq API key from environment variables and sets
        the API endpoint and model configuration.
        """
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model  = "meta-llama/llama-4-maverick-17b-128e-instruct"

    def ask_about_celebrity(self,name,question):
        """
        Ask a question about a specific celebrity.

        The method constructs a concise prompt instructing the AI
        to answer accurately about the given celebrity.

        Args:
            name (str): Name of the celebrity.
            question (str): Question to ask about the celebrity.

        Returns:
            str: AI-generated answer, or a fallback message if the request fails.
        """
        # Prepare request headers with authentication
        headers = {
            "Authorization" : f"Bearer {self.api_key}",
            "Content-Type" : "application/json"
        }

        # Build the prompt for the LLM
        prompt = CELEBRITY_QA_PROMPT.format(name=name, question=question)

        # Prepare the request payload
        payload  = {
            "model" : self.model,
            "messages" : [{"role" : "user" , "content" : prompt}],
            "temperature" :  0.5,
            "max_tokens" : 512
        }

        # Send the request to Groq API
        response = requests.post(self.api_url , headers=headers , json=payload)

        # Return the model's response if successful
        if response.status_code==200:
            return response.json()['choices'][0]['message']['content']
        
        # Fallback response in case of failure
        return "Sorry I couldn't find the answer"