import os
import re
import numpy as np
import cv2


def get_pos_letters(arabic_word):
    numbers_list = ""
    for letter in arabic_word:
        if ord(letter) < ord("ب"):
            numbers_list += "1-"
        elif letter == "ب":
            numbers_list += "2-"
        elif letter == "ت":
            numbers_list += "3-"
        elif letter == "ث":
            numbers_list += "4-"
        elif letter == "ج":
            numbers_list += "5-"
        elif letter == "ح":
            numbers_list += "6-"
        elif letter == "خ":
            numbers_list += "7-"
        elif letter == "د":
            numbers_list += "8-"
        elif letter == "ذ":
            numbers_list += "9-"
        elif letter == "ر":
            numbers_list += "10-"
        elif letter == "ز":
            numbers_list += "11-"
        elif letter == "س":
            numbers_list += "12-"
        elif letter == "ش":
            numbers_list += "13-"
        elif letter == "ص":
            numbers_list += "14-"
        elif letter == "ض":
            numbers_list += "15-"
        elif letter == "ط":
            numbers_list += "16-"
        elif letter == "ظ":
            numbers_list += "17-"
        elif letter == "ع":
            numbers_list += "18-"
        elif letter == "غ":
            numbers_list += "19-"
        elif letter == "ف":
            numbers_list += "20-"
        elif letter == "ق":
            numbers_list += "21-"
        elif letter == "ك":
            numbers_list += "22-"
        elif letter == "ل":
            numbers_list += "23-"
        elif letter == "م":
            numbers_list += "24-"
        elif letter == "ن":
            numbers_list += "25-"
        elif letter == "ه":
            numbers_list += "26-"
        elif letter == "و":
            numbers_list += "27-"
        elif letter == "ي" or letter == "ى":
            numbers_list += "28-"
    return numbers_list[:-1]

# this method will find the number for the word inside the selected words.txt file
def get_word_number(word):
    with open("selected words.txt", "r", encoding='UTF8') as reader:
        counter = 1
        for line in reader:
            # print(counter, line[:-1])
            if line[:-1] == word:
                return counter
            counter += 1
        return -1


# # this peace of code for testing purposes
# while True:
#     word_number = get_word_number(input("Enter a word: "))
#     print(word_number)

writer_id = int(input("Enter the writer id: "))
# set_type = input("Enter the set type: ").strip()  # this gonna contain the set type (test, train, ...)
set_type = "test"

list_of_images = os.listdir("list_of_images")  # this list gonna contain
# print(list_of_images)

report_list = []  # this list gonna cotain the result of each image to report it at the end of the program
for image in list_of_images:
    assert os.path.exists("list_of_images/" + image), "an image is not found"
    image_array = cv2.imread("list_of_images/" + image)
    cv2.imshow("Word", image_array)
    cv2.waitKey(0)

    word_number = -1
    is_misspelled = False  # this variable will be used to know if the word is misspelled or not
    user_word = ""
    while True:
        user_word = input("Enter the word you have seen: ").strip()
        word_number = get_word_number(user_word)
        if user_word == "0":
            is_misspelled = True
            break
        if word_number != -1:
            break
        else:
            print("\nThe word " + user_word + " is not exist on the dataset selected words...")
            print("Try again\n")
            cv2.imshow("Word", image_array)
            cv2.waitKey(0)

    template_number, _ = os.path.splitext(image)
    template_number = re.split("-", template_number)[0].replace(" ", "").zfill(4)
    if user_word != "0":
        number_of_words = len(os.listdir("eifad dataset (initial version)/" + set_type + "/" + user_word)) + 1
    if is_misspelled or os.path.exists("eifad dataset (initial version)/" + set_type + "/" + user_word + "/" + "005" + template_number + "01" + str(writer_id) + "-" + str(number_of_words) + ".tiff"):
        print("Image " + image + " is discarded")
        os.rename("list_of_images/" + image, "misspelled and repeated/" + image)
        continue
    assert word_number != -1 and user_word != "", "word number is not calculated properly"

    # There is an issue if write the image in arabic folder because the OpenCV library doesn't support UTF-8
    # To solve this problem we have to extract the image anywhere and then we gonna move it using os.rename()
    cv2.imwrite("eifad dataset (initial version)/image.jpg", image_array)
    os.rename("eifad dataset (initial version)/image.jpg", "eifad dataset (initial version)/" + set_type + "/" + user_word + "/" + "005" + template_number + "01" + str(writer_id) + "-" + str(number_of_words) + ".tiff")
    print("Image " + "005" + template_number + "01" + str(writer_id) + "-" + str(number_of_words) + ".tiff" + " has been added")

    # now we will generate the ground truth
    with open("eifad dataset (initial version)/metaData/" + user_word + "/" + "005" + template_number + "01" + str(writer_id) + "-" + str(number_of_words) + ".txt", "w", encoding="utf-8") as ground_truth:
        ground_truth.write("Word: " + user_word + "\n")
        ground_truth.write("Volunteer Identifier: " + "005" + template_number + "01" + str(writer_id) + "\n")
        ground_truth.write("Image Name: " + "005" + template_number + "01" + str(writer_id) + "-" + str(number_of_words) + ".tiff" + "\n")
        ground_truth.write("Number of letters: " + str(len(user_word)) + "\n")
        ground_truth.write("Number of dots: " + str(len(re.findall("[بجخذزضظغفن]", user_word)) + 2 * len(re.findall("[تقية]", user_word)) + 3 * len(re.findall("[ثش]", user_word))) + "\n")
        ground_truth.write("Position of letters: " + get_pos_letters(user_word))

    os.remove("list_of_images/" + image)