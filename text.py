# install textblob    :     pip install textblob
from textblob import TextBlob
def correct_grammer(text):
    blob = TextBlob(text)
    correct_text = str(blob.correct())
    return correct_text
# using example
text = input("Enter your sentence: ")
correct_text = correct_grammer(text)
print(f"Original: {text}")
print(f"Corrected: {correct_text}")