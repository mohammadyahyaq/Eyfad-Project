import os

images=[]
groundtruth=[]
path1='pictures' #need to have folder call pictures
#path11='pictures/الخليج'
path2='GroundTruth' #need to have folder call Groundtruth

def Num_of_dots(word):
    Dictionary_dots = {"ب": 1, "ت": 2, "ث": 3,
                       "ج": 1, "خ": 1, "ذ": 1, "ز": 1,
                       "ش": 3, "ض": 1,
                       "ظ": 1, "غ": 1,
                       "ف": 1, "ق": 2,
                       "ن": 1, "ي": 2
                       }

    count=0
    for x in word:
        if x in Dictionary_dots:
            count+=Dictionary_dots[x]

    print("Number of dots:",count)

    return count

def Num_of_possition(word):
    Dictionary_letters = {"أ": 1, "ا": 1, "آ": 1,"ء": 1, "إ": 1
                        ,"ب": 2, "ت": 3, "ث": 4,
                          "ج": 5, "ح": 6, "خ": 7,
                          "د": 8, "ذ": 9, "ر": 10, "ز": 11,
                          "س": 12, "ش": 13, "ص": 14, "ض": 15,
                          "ط": 16, "ظ": 17, "ع": 18, "غ": 19,
                          "ف": 20, "ق": 21, "ك": 22, "ل": 23,
                          "م": 24, "ن": 25, "ه": 26, "و": 27, "ي": 28
                          }
    string_possition=""
    for x in word:
        if x in Dictionary_letters:
            string_possition+= str(Dictionary_letters[x]) + "-"

    string_possition= string_possition[:-1]
    print(string_possition)
    return string_possition

myList = os.listdir(path1)
myList2 = os.listdir(path2)
noOfClasses = len(myList)
print("total number of classes detected",len(myList))
for x in myList:
    i =0
    y = path1+"/"+str(x)
    print("y",y)
    print("x", x)
    os.mkdir(path2+"/"+str(x))
    myPicList = os.listdir(path1 + "/" + str(x))

    print(x)
    myPicList = os.listdir(path1+"/"+str(x))
    for z in myPicList:

        z2= os.path.splitext(os.path.basename(z))[0]
        numberOfDot = Num_of_dots(x)
        numberOfPosition = Num_of_possition(x)
        file = open(path2 + "/" + str(x) + "/" + z2 + ".txt", "w" ,encoding='utf-8')
        file.write('Word: '+x+'\n'
                   +'Image Name: '+z+'\n'
                   +'Number of letters: '+str(len(x))+"\n"
                   +"Number of dots: "+str(numberOfDot)+'\n'
                   +'Position of letters: '+numberOfPosition)

        file.close()
    print("ww",myPicList[i])
    print("this ",os.listdir(path1+"/"+str(x)))

print("-----------------")
