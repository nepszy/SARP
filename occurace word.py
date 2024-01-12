import os
import spacy
import csv
from collections import Counter


nlp = spacy.load("en_core_sci_sm") 
# path
input_text_file = 'C:/Users/puja/Desktop/csvf/output.txt'

# Output path
output_csv_file = 'C:/Users/puja/Desktop/csvf/top_words.csv'

# preprocess text 
def count_words(text):
    doc = nlp(text)
    words = [token.text.lower() for token in doc if token.is_alpha]
    word_counts = Counter(words)
    return word_counts

# Read the text 
with open(input_text_file, 'r', encoding='utf-8') as file:
    text_content = file.read()

# Counts
word_counts = count_words(text_content)

# top 30  words
top_30_words = word_counts.most_common(30)

with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Word', 'Count'])  # Header
    csv_writer.writerows(top_30_words)

print(f"Top 30 common words and their counts saved in '{output_csv_file}'.")
