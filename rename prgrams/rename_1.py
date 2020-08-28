import os
import re
import numpy as np
import cv2


def get_word_number(ds_word):
    for original_file_word in os.listdir("test"):
        if original_file_word == ds_word:
            return len(os.listdir("test/" + word)) + 1
    print("Error 12: the word " + ds_word + " is not found on the dataset folder")
    exit()


# this function will return the template number and for each word
def get_template_number(image_np):
    list_of_images = os.listdir("list_of_images")
    for image in list_of_images:
        original_image = cv2.imread("list_of_images/" + image)
        comparison = original_image == image_np
        print(comparison)
        if comparison.all():
            print("found")
            tmp_number = re.split("-", image)[0]
            return tmp_number
    print("Error 23: image not found on the original file")
    exit()


words_files_list = os.listdir("Handwritten_Arabic_Dataset/test")  # this list contain the list of words on the dataset
writer_id = "2006"

for word in words_files_list:
    images_for_each_word = os.listdir("Handwritten_Arabic_Dataset/test" + "/" + word)
    if len(images_for_each_word) > 0:
        print(word)
        for ds_image in images_for_each_word:
            image_array = cv2.imread("Handwritten_Arabic_Dataset/test" + "/" + word + "/" + ds_image)

            template_number = get_template_number(image_array).zfill(4)
            number_of_templates = "01"

            folder_number = get_word_number(word)

            new_name = "005" + template_number + number_of_templates + writer_id + "_" + str(folder_number) + ".jpg"
            os.rename("Handwritten_Arabic_Dataset/" + word + "/" + ds_image, "Handwritten_Arabic_Dataset/" + word + "/" + new_name)