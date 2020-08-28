import os

count=0
for dirname in os.listdir("C:/Users/LENOVO/Downloads/words/words"):
    print(dirname)


    for i, filename in enumerate(os.listdir("C:/Users/LENOVO/Downloads/words/words/"+dirname)):
            print(i)
            Newfilename=filename
            if len(filename) > 4:
                Newfilename = filename[:12]

            i += 1 #عشلن اتفادى رقم صفر
            os.rename("C:/Users/LENOVO/Downloads/words/words/"+dirname + "/" + filename, "C:/Users/LENOVO/Downloads/words/words/"+dirname + "/" +Newfilename+"_"+str(i) + ".tiff")
            #to count the number of Image
            count+=1



print(count)