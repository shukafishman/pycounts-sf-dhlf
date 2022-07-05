from string import punctuation
from collections import Counter


INPUT_FILE = "zen.txt"

def load_text(input_file):
    """Load text from a text file and return as a string"""
    with open(input_file, "r") as file:
       text = file.read()
    return text 

def clean_text(text):
    """Lower case and remove punctuation from a string"""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text

def count_words(input_file):
    """Count unique words in a file"""
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)

