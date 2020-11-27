# WebCam Image Capture

import cv2
import matplotlib.pyplot as plt


def main():
    cap = cv2.VideoCapture(0)  # (0) means if there are multiple cams attach then it will select the 1st webcam

    # check and read the if the cam is works or no
    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)  # returns True/False
        print(frame)  # returns some values
    else:
        ret = False
        print(ret)

    # Normal Img
    plt.imshow(frame)
    plt.title('Normal cv2 Image Capture')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    # Color Img
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title('Color Image Capture')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    cap.release()  # Releases the associated webcam


if __name__ == '__main__':
    main()