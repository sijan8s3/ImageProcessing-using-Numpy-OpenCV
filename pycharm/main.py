import cv2

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()

    if ret:
        faces = classifier.detectMultiScale(frame)
        for face in faces:
            x, y, w, h = face
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)

        cv2.imshow("My window", frame)

    # wait for another picture
    key = cv2.waitKey(30)

    # if q is pressed on keyboard break the while loop
    # and release camera and destroy windows od cv2
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
