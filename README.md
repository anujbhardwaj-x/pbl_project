# AI-Driven Crowd Monitoring in Indian Railways using YOLOv9

## Project Description
This project implements a real-time AI-based crowd monitoring system using YOLOv9 for person detection. 
The system detects individuals from CCTV video feeds, estimates crowd density, classifies congestion levels, 
and visualizes trends for safety monitoring in railway platforms.

## Key Features
- YOLOv9-based real-time person detection
- Detection Accuracy: >95%
- Real-time processing: 25–30 FPS
- Threshold-based density classification
- Crowd trend visualization
- Scalable architecture for multi-camera support

## Density Classification Logic
Let N = number of detected persons per frame.

- Undercrowded → N < lower threshold
- Moderate → Safe operating range
- Overcrowded → N > upper threshold

Threshold derived from:
- Platform coverage area (~45 m²)
- Safe density limit (~4 persons/m²)

## Tech Stack
Python | YOLOv9 | OpenCV | Flask | Matplotlib

## Future Scope
- Multi-camera integration
- Predictive crowd surge detection
- Edge-device optimization
