import os

with open("selected words.txt", "w", encoding= "utf-8") as writer:
    for word in os.listdir("eifad dataset (initial version)/test"):
        writer.write(word + "\n")