import json
import pandas as pd
from collections import Counter
import re
import uuid


with open('src/resources/input/input_data.json', 'r') as json_file:
    json_data = json.load(json_file)

# Beautify the input format
petitions_data = [
    {
        "label": petition_data["label"]["_value"],
        "abstract": petition_data["abstract"]["_value"],
        "numberOfSignatures": petition_data["numberOfSignatures"]
    }
    for petition_data in json_data
]


# Find the words that have 5 or more letters
def get_words(text):
    return re.findall(r"\b\w{5,}\b", text.lower())

def generate_records():
    words = []

    for petition in petitions_data:
        words.extend(get_words(petition["label"]))
        words.extend(get_words(petition["abstract"]))
    # Count the occurence of words that have 5 or more letter
    words_count = Counter(words)

    # Find 20 most common words
    top_20_words = [word for word, count in words_count.most_common(20)]

    data = []

    # Petition_id generation and petition word count
    for petition in petitions_data:
        record = {"petition_id": str(uuid.uuid4())}
        Petition_words = get_words(petition["label"]) + get_words(petition["abstract"])
        petition_words_counter = Counter(Petition_words)

        for word in top_20_words:
            record[word] = petition_words_counter[word]

        data.append(record)
    
    # Use panda to create dataFrame and save in petitions_out.csv file
    df = pd.DataFrame(data)
    print(df)
    df.to_csv('src/resources/output/petitions_output.csv')


if __name__ == "__main__":
    generate_records()