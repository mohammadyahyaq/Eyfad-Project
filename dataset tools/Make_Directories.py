import os

while True:
    word = input("Enter the word: ")
    os.mkdir("eifad dataset (initial version)/test/" + word)
    os.mkdir("eifad dataset (initial version)/metaData/" + word)