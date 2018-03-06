import cv2

cap = cv2.VideoCapture(0)

def getImage():
    ret,frame = cap.read()
    _frame = cv2.resize(frame,(32,32))
    return _frame


def frame():
    frame = getImage()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray_image
