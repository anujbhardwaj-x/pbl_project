import cv2
import torch

model = torch.hub.load('WongKinYiu/yolov9', 'custom', path='yolov9.pt')

def detect_people(frame):
    results = model(frame)
    detections = results.xyxy[0]
    person_count = 0

    for *box, conf, cls in detections:
        if int(cls) == 0 and conf > 0.5:
            person_count += 1

    return person_count
