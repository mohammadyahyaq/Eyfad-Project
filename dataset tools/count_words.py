import os
import re

counter = 0
for word in os.listdir("eifad dataset (initial version)/test"):
    counter += len(os.listdir("eifad dataset (initial version)/test/" + word))

writers = []
for word in os.listdir("eifad dataset (initial version)/test"):
    for image in os.listdir("eifad dataset (initial version)/test/" + word):
        image_name, _ = os.path.splitext(image)
        if image_name.startswith("005"):
            writer_id = re.split("[_-]", image_name)[0][-4:]
            if writer_id not in writers:
                writers.append(writer_id)


print("Number of images: " + str(counter))
print("Number of folders: " + str(len(os.listdir("eifad dataset (initial version)/test"))))
print("Number of writers: " + str(len(writers)))
print()
# print(writers)