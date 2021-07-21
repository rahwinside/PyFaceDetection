import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('compress.jpg')

cv2.imshow('Deni rocks!', image)

cv2.waitKey()

print("Execution complete.")
