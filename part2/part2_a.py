from PIL import Image

import numpy


def main():
    numpy.set_printoptions(threshold=numpy.inf)

    matrix = numpy.asarray(Image.open('A.png'))
    array = numpy.asarray(matrix).flatten()
    array = sorted(array, reverse=True)

    print(str(array))


if __name__ == "__main__":
    main()
