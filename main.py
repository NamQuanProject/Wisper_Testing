import requests
import os
from tqdm import tqdm
import pandas as pd

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-base"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

audio_directory = os.listdir(os.path.join("en_test_0"))
audio_path_list = []
for audio_path in audio_directory:
    audio_path_list.append(os.path.join("en_test_0", audio_path))


# print(query("record2.webm"))



df = pd.read_csv("test.tsv", sep='\t')
path = df["path"].values
sentences = df["sentence"].values
path = [os.path.join("en_test_0", audio_path) for audio_path in path]
label = {audio_path : sentence for audio_path, sentence in zip(path, sentences)}

transcriptions = []

for path in tqdm(audio_path_list[131:161]):
    ans = query(path)["text"]
    transcriptions.append({"prediction": ans, "path": path, "correct_label": label[path]})


another_df = pd.DataFrame(transcriptions)

another_df.to_csv("transcriptions4.tsv", sep='\t', index=False)
