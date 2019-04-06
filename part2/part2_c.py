from PIL import Image


def main():
    threshold = 120
    print("Threshold is: " + str(threshold))

    image = Image.open('A.png')
    width, height = image.size

    new_image = Image.new('RGB', (width, height))
    pix2 = new_image.load()

    for x in range(width):
        for y in range(height):
            if image.getpixel((x, y)) > threshold:
                pix2[x, y] = (255, 0, 0)
            else:
                pix2[x, y] = (0, 0, 0)

    new_image.save('result_c.png', 'png')
    new_image.show()
    print("\n\"result_c.png\" has been created successfully!")


if __name__ == "__main__":
    main()
