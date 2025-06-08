import cv2
import easyocr
import numpy as np
import pyttsx3

# Instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Capture video from camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

threshold = 0.25
spoken_texts = set()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Detect text on frame
    text_ = reader.readtext(frame)

    # Draw bbox and text
    for t_, t in enumerate(text_):
        bbox, text, score = t

        if score > threshold:
            bbox = np.array(bbox).astype(int)
            cv2.rectangle(frame, bbox[0], bbox[2], (0, 255, 0), 2)
            cv2.putText(frame, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

            # Speak the detected text if not spoken before
            if text not in spoken_texts:
                spoken_texts.add(text)
                engine.say(text)
                engine.runAndWait()

    # Display the resulting frame
    cv2.imshow("Text Detection", frame)

    # Terminate run when "Q" is pressed
    if cv2.waitKey(1) == ord("q"):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
