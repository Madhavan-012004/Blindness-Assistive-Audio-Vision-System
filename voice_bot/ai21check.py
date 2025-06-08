import requests

AI21_API_KEY = "Your API Key"
AI21_API_URL = "https://api.ai21.com/studio/v1/j2-ultra/completion"

def get_ai21_response(prompt):
    headers = {
        "Authorization": f"Bearer {AI21_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "numResults": 1,
        "maxTokens": 50,
        "temperature": 0.7
    }
    
    response = requests.post(AI21_API_URL, json=data, headers=headers)
    
    print("API Response Code:", response.status_code)
    print("API Response Body:", response.text)  # Debugging output

    if response.status_code == 200:
        try:
            return response.json()["completions"][0]["data"]["text"].strip()
        except KeyError:
            return "Invalid API response format."
    else:
        return f"Error {response.status_code}: {response.text}"
