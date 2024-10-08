import requests
import os
from tqdm import tqdm
import pandas as pd
from test import query



audio_directory = os.listdir(os.path.join("en_test_0"))
audio_path_list = []
for audio_path in audio_directory:
    audio_path_list.append(os.path.join("en_test_0", audio_path))





df = pd.read_csv("test.tsv", sep='\t')
path = df["path"].values
sentences = df["sentence"].values
path = [os.path.join("en_test_0", audio_path) for audio_path in path]
label = {audio_path : sentence for audio_path, sentence in zip(path, sentences)}

transcriptions = []

for path in tqdm(audio_path_list[171:200]):
    ans = query(path)["text"]
    transcriptions.append({"prediction": ans, "path": path, "correct_label": label[path]})


another_df = pd.DataFrame(transcriptions)

another_df.to_csv("transcriptions5.tsv", sep='\t', index=False)
