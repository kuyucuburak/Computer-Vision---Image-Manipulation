import matplotlib.pyplot as plt
import cv2


def main():
    image = cv2.imread('A.png')
    values = image.mean(axis=2).flatten()
    plt.hist(values, 20)
    plt.xlim([0, 255])
    plt.savefig('result_b.png')
    print("\n\"result_b.png\" has been created successfully!")
    plt.show()


if __name__ == "__main__":
    main()
