"""
Celebrity Detection Service

This module provides a class that integrates with the Groq API
to identify celebrities in images using a multimodal LLM.
"""

import os
import base64
import requests
from app.utils.prompts import IDENTIFY_CELEBRITY_PROMPT

class CelebrityDetector:
    """
    A service class responsible for identifying celebrities from images
    using the Groq Chat Completions API and a vision-capable LLM model.
    """
    def __init__(self):
        """
        Initialize the CelebrityDetector.

        Reads the API key from environment variables and sets
        the Groq API endpoint and model configuration.
        """
        self.api_key = os.getenv("GROQ_API_KEY")
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "meta-llama/llama-4-maverick-17b-128e-instruct"

    def identify_celebrity(self, image_bytes):
        """
        Identify a celebrity from an image.

        The image is encoded in Base64 and sent to the Groq API along
        with a structured prompt that instructs the model to identify
        the person in the image.

        Args:
            image_bytes (bytes): Raw image bytes (JPEG format).

        Returns:
            - str: Full AI-generated response describing the celebrity.
            - str: Extracted celebrity name or "Unknown".
        """
        # Encode image bytes to Base64 for API transmissio
        encoded_image = base64.b64encode(image_bytes).decode()

        # Request headers including authorization
        headers = {
            "Authorization" : f"Bearer {self.api_key}",
            "Content-Type" : "application/json"
        }

        # Construct the multimodal prompt payload
        prompt = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": IDENTIFY_CELEBRITY_PROMPT
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            }
                        }
                    ],
                }
            ],
            "temperature": 0.3,
            "max_tokens": 1024
        }

        # Send request to Groq API
        response = requests.post(self.api_url , headers=headers , json=prompt)

        # Handle successful response
        if response.status_code==200:
            result = response.json()['choices'][0]['message']['content']
            name = self.extract_name(result)

            return result , name  
        
        # Fallback if request fails
        return "Unknown" , ""
    
    def extract_name(self, response_text):
        """
        Extract the celebrity's full name from the model response.

        The method searches for a line that starts with
        '- **Full Name**:' and extracts the value.

        Args:
            response_text (str): AI-generated response text.

        Returns:
            str: Extracted full name or "Unknown" if not found.
        """
        for line in response_text.splitlines():
            if line.lower().startswith("- **full name**:"):
                return line.split(":")[1].strip()
            
        return "Unknown"