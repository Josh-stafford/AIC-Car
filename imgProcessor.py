import cv2

cap = cv2.VideoCapture(0)

def getImage():
    ret,frame = cap.read()
    _frame = cv2.resize(frame,(32,32))
    return _frame


def frame():
    frame = getImage()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flat = []
    for x in range(0, len(gray_image)):
        for y in range(len(gray_image[0])):
            val = gray_image[x][y]
            flat.append(val)
    print(len(flat))
    return flat
