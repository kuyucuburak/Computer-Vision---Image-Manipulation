from PIL import Image

import numpy


def main():
    print("I started!")

    image = Image.open('A.png')
    matrix = numpy.asarray(image)
    array = numpy.asarray(matrix).flatten()

    width, height = image.size
    average = sum(array) / (width*height)
    average = int(average)
    print("Average is: " + str(average))

    modified_matrix = matrix - average
    new_image = Image.fromarray(modified_matrix, 'L')
    new_image.save('result_e.png')
    new_image.show()

    print("\n\"result_e.png\" has been created successfully!")


if __name__ == "__main__":
    main()
