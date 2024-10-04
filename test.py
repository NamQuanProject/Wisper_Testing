import requests




def query(filename):
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
    headers = {"Authorization": "Bearer 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"}
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

path = "Errors_Example/coffee_shop_noise.webm"
print(query(path))