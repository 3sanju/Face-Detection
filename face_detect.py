import cv2

# Load the Haar cascade classifier
a = cv2.CascadeClassifier("/path/to/haarcascade_frontaldetect_default.xml")

# Start video capture from the default webcam
b = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, d_image = b.read()

    # Check if the frame was successfully captured
    if not ret:
        break

    # Convert the frame to grayscale
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    f = a.detectMultiScale(e, 1.3, 6)

    # Draw rectangles around detected faces
    for (x1, y1, w1, h1) in f:
        cv2.rectangle(d_image, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 5)

    # Display the frame with detected faces
    cv2.imshow('img', d_image)

    # Break the loop if the 'esc' key is pressed (key code 27)
    h = cv2.waitKey(40) & 0xff
    if h == 27:
        break

# Release the webcam and destroy all OpenCV windows
b.release()
cv2.destroyAllWindows()
