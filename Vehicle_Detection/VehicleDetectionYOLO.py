import cv2
import numpy as np
import math

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

class_time_map = {
    "car": 2,
    "van": 3,
    "jeep": 5,
    "bus": 10,
    "motorbike": 1,
    "truck": 8,
    "tuk tuk": 4,
}

image = cv2.imread("test6.jpg")
height, width, _ = image.shape
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)

layer_names = net.getUnconnectedOutLayersNames()
outs = net.forward(layer_names)
class_ids = []
confidences = []
boxes = []
total_time = 0
total_vehicles = 0

for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5:
            label = str(classes[class_id])

            if label in class_time_map:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

                time = class_time_map[label]
                total_time += time
                total_vehicles += 1

average_time = math.ceil(total_time / total_vehicles) if total_vehicles > 0 else 0
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(len(boxes)):
    if i in indices:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confidences[i]
        color = (0, 255, 0)
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        time_label = f"{class_time_map.get(label, 'Unknown')} minutes"
        cv2.putText(image, time_label, (x, y - 10), font, 0.5, color, 2)

average_time_label = f"Average Time: {average_time} minutes"
cv2.putText(image, average_time_label, (10, 30), font, 1, (0, 255, 0), 2)
cv2.imshow("Vehicle Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
