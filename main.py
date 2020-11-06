from PIL import Image
import pytesseract

#array of the location of soon to be processed screenshots
images = []
#the recognized text from the images
recText = ""
#path of the known names
txtFile = ""

#gets inputs
def setup():
    imageCount = 0
    global images, txtFile
    while True:
        imageCount = input("Image count: ")
        try:
            imageCount = int(imageCount)
            break
        except ValueError:
            print("Please input a valid value")
            continue
    for i in range(imageCount):
        images.append(input(f"Image{i + 1} Path: "))
    txtFile = input("Known names text: ")

#recoginizes text from image
def rec(imgUrl):

    try:
        img = Image.open(imgUrl)
        return pytesseract.image_to_string(img)
    except:
        print("Image(s) path(s) is(are) invalid")
        exit()


#reads names from a .txt file, seperates them using the "," and returns the seperated names in array form
def names(knownNamesTextFile):
    tempStr = ""
    f = open(knownNamesTextFile, 'r')
    if not f == None:
        names = f.read().split(",")
        for i in range(len(names)):
            for j in range(len(names[i])):
                if names[i][j].isalpha():
                    tempStr += names[i][j]
            names[i] = tempStr.upper()
            tempStr = ""
        return names
    else:
        print(f"Known names file path <{knownNamesTextFile}> is invalid")
        exit()

#compares the list of names and the recognized text and finds the absentees
def find(names, recognizedText):
    absentees = []
    for i in range(len(names)):
        if not names[i] in recognizedText:
            absentees.append(names[i])
    return absentees

#main execution
if __name__ == "__main__":
    setup()
    #loops through all the images, and adds the text from them to recText
    tempText = ""
    for img in images:
        recText += rec(img)
    #processes recText
    for i in range(len(recText)):
        if recText[i].isalpha():
            tempText += recText[i]
    recText = tempText.upper()

    print(f"absentees: {find(names(txtFile), recText)}")
