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
a_y = 55
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

    a_x = 55*(a_x + 1)
    a_y = 55*(a_y + 1)
    return int(a_x), int(a_y)

model = YOLO("yolov8n.pt")
print("Model loading complete")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # sleep(1)
    ret, frame = cap.read()
    size = (frame.shape[1], frame.shape[0])
    if not ret:
        print("Error: Could not read frame.")
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

    x = model(frame)
    person = x[0].boxes.cls == 0
    box = x[0].boxes.xyxy[person]
    boxes = box.tolist()
    frame, start, end = draw_boxes(frame, boxes)

    cv2.imshow("Testing",frame)

    a_x, a_y = angles(start, end, size)

    rotateservo(pin1, a_y)
    rotateservo(pin2, a_x)
    print(a_x, a_y)