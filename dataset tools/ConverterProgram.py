import numpy as np
import cv2
import os

import math

files_list = os.listdir('template images')
# print(files_list)

for template in files_list:
    counter = 1
    imageCounter = 1
    with open("template images/" + template) as reader:
        for line in reader:
            name_pattern = template[8:-4] + "-" + str(imageCounter)

            if counter % 3 == 1:
                image_list = list(eval(line)[:-1])  # this line of code will save the image into a list
                edge_size = int(math.sqrt(len(image_list)))  # we need this variable for reshape the numpy list
                image_np = np.array(image_list, np.uint8)
                image_np = image_np.reshape(edge_size,
                                            edge_size)  # now we reshaped the image to let it have the original dimensions
                # image_np = fix_rows(image_np)
                image_np = np.transpose(image_np)
                # image_np = fix_rows(image_np)
                # file_path = "list_of_images/" + str(name_pattern) + "a.png"
                # cv2.imwrite(file_path, image_np)
                # image_np = np.where(image_np == 0, 255, image_np)
                file_path = "list_of_images/" + name_pattern + ".jpg"
                cv2.imwrite(file_path, image_np)
                imageCounter += 1
            counter += 1
