import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import pyautogui ## cross-platform for pressing keys


# Webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

# Hand detector
detector = HandDetector(detectionCon=0.8)

# Keyboard layout
keys = [["Q","W","E","R","T","Y","U","I","O","P"],
        ["A","S","D","F","G","H","J","K","L"],
        ["Z","X","C","V","B","N","M"]]

# Button class
class Button():
    def __init__(self,pos,text,size=[85,85]):
        self.pos = pos
        self.size = size
        self.text = text

# Create button list
buttonList = []

for i in range(len(keys)):
    for j,key in enumerate(keys[i]):
        buttonList.append(Button([100*j + 50,100*i + 50],key))

# Function to draw keyboard
def drawAll(img,buttonList):
    for button in buttonList:
        x,y = button.pos
        w,h = button.size

        cv2.rectangle(img,(x,y),(x+w,y+h),(200,200,200),cv2.FILLED)
        cv2.putText(img,button.text,(x+20,y+65),
                    cv2.FONT_HERSHEY_PLAIN,4,(0,0,0),4)
    return img

# Main loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]

        if lmList and len(lmList) >= 13:  # ensure index 8 and 12 exist
            for button in buttonList:
                x, y = button.pos
                w, h = button.size

                # Check if finger is inside button
                if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                    try:
                        l, _, _ = detector.findDistance(8, 12, img, draw=False)
                        if l < 45:
                            pyautogui.press(button.text)
                            cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 0, 255), cv2.FILLED)
                            cv2.putText(img, button.text, (x + 20, y + 65),
                                        cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                            time.sleep(0.25)  # prevent multiple presses
                    except Exception as e:
                        print("Distance error:", e)

    cv2.imshow("Virtual Keyboard", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()