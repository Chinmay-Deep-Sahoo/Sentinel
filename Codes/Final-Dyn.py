from ultralytics import YOLO
import cv2
from pyfirmata import Arduino, SERVO, util
from time import sleep

port = 'COM6'
pin1 = 10
pin2 = 9
board = Arduino(port)

board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO

def rotateservo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

a_x = 55
a_y = 25
rotateservo(pin1, a_y)
rotateservo(pin2, a_x)

def draw_boxes(image, boxes, color=(0, 255, 0), thickness=2):
    start = (0,0)
    end = (0,0)
    for box in boxes:
        x_min, y_min, x_max, y_max = box
        L, W, _ = image.shape
        start = (W/2, L/2)
        end = ((x_max + x_min)/2, (y_max + y_min)/2)
        start = (int(start[0]), int(start[1]))
        end = (int(end[0]), int(end[1]))
        cv2.rectangle(image, (int(x_min), int(y_min)), (int(x_max), int(y_max)), color, thickness)
    return image, start, end

def angles(s, e, img_shape, max_x = 90, max_y = 30):
    X, Y = img_shape
    X, Y = int(X/2), int(Y/2)
    a_x = -1*(e[0] - s[0])/X
    a_y = -1*(s[1] - e[1])/Y
    a_x = a_x*max_x
    a_y = a_y*max_y

    # a_x = 55*(a_x + 1)
    # a_y = 55*(a_y + 1)
    return int(a_x), int(a_y)

model = YOLO("yolov8n-face.pt")
print("Model loading complete")

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error: Could not open USB camera trying default camera.")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open default camera.")
        exit()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')    
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

ctr = 0

while True:
    ctr += 1
    ctr = ctr%5
    # sleep(0.1)
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        rotateservo(pin1, 44)
        rotateservo(pin2, 55)
        break

    out.write(frame)
    size = (frame.shape[1], frame.shape[0])
    cv2.imshow("Testing",frame)

    if ctr == 1:
        x = model(frame)
        person = x[0].boxes.cls == 0
        box = x[0].boxes.xyxy[person]
        boxes = box.tolist()
        frame, start, end = draw_boxes(frame, boxes)

        delta_x, delta_y = angles(start, end, size, max_x=5, max_y=5)
        if abs(delta_x) > 1:
            a_x = min(a_x + delta_x, 270)
            a_x = max(0, a_x) 
        if abs(delta_y) > 1:
            a_y = min(a_y + delta_y, 270) 
            a_y = max(0, a_y)
        rotateservo(pin1, a_y)
        rotateservo(pin2, a_x)
        print(a_x, a_y)

cap.release()
out.release()
cv2.destroyAllWindows()