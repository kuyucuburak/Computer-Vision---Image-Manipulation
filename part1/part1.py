from PIL import Image

import numpy


def main():
    global resultNumber
    resultNumber = 1

    print("Please enter the rate of the first pictures (0-100):")
    rate = input()

    firstRate = float(rate) / 100
    secondRate = (100 - float(rate)) / 100

    print("\nRate of the first pictures is: " + str(firstRate))
    print("Rate of the second pictures is: " + str(secondRate) + "\n")

    if int(rate) < 0 or int(rate) > 100:
        print("Error! Please enter between 0 and 100.")
        return 0

    image_1 = Image.open('1-1.bmp')
    image_2 = Image.open('1-2.bmp')

    if image_1.size != image_2.size:
        print("Error! Size of the images are not equal.")
        return 0

    processImage('1-1.bmp', '1-2.bmp', firstRate, secondRate)
    processImage('2-1.bmp', '2-2.bmp', firstRate, secondRate)
    processImage('3-1.bmp', '3-2.bmp', firstRate, secondRate)
    processImage('4-1.bmp', '4-2.bmp', firstRate, secondRate)
    processImage('5-1.bmp', '5-2.bmp', firstRate, secondRate)

    print("\nTask is completed successfully!")


def processImage(image1Name, image2Name, firstRate, secondRate):
    global resultNumber

    array_1 = numpy.asarray(Image.open(image1Name))
    array_2 = numpy.asarray(Image.open(image2Name))

    array_1 = array_1 * firstRate
    array_2 = array_2 * secondRate

    finalArray = array_1 + array_2

    image = Image.fromarray(numpy.uint8(finalArray))
    image.save("result_" + str(resultNumber) + ".bmp")

    print("\"result_" + str(resultNumber) + ".bmp\" " + "has been created " + "from \"" + image1Name + "\" and \"" + image2Name + "\"")
    resultNumber = resultNumber + 1


if __name__ == "__main__":
    main()
