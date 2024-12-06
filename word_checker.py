import csv
import re

def load_disallowed_words(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # select all words out of the first column of the csv file
        return [row[0].strip().lower() for row in reader]

def count_disallowed_words(text, disallowed_words):
    word_counts = {}
    for word in disallowed_words:
        # regex boundary matching to grab each individual word
        pattern = r'\b' + re.escape(word) + r'\b'
        # grabbing number of times the targeted word was seen
        count = len(re.findall(pattern, text, re.IGNORECASE))
        if count > 0:
            word_counts[word] = count
    return word_counts

def main():
    csv_file = 'disallowed_words.csv'
    text_file = 'document.txt'

    disallowed_words = load_disallowed_words(csv_file)
    
    with open(text_file, 'r') as file:
        text = file.read().lower()
    
    results = count_disallowed_words(text, disallowed_words)

    for word, count in results.items():
        print(f"'{word}' found {count} times.")

if __name__ == "__main__":
    main()
