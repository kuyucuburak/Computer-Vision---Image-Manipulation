from PIL import Image


def main():
    width, height = (50, 50)

    new_image = Image.new('L', (width, height))
    image = Image.open('A.png')
    data = new_image.load()

    for y in range(height):
        for x in range(width):
            data[(x, y)] = image.getpixel((x, 49+y))

    new_image.save('result_d.png', 'png')
    new_image.show()
    print("\"result_d.png\" has been created successfully!")


if __name__ == "__main__":
    main()
