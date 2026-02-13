from flask import Flask, render_template
import cv2
from detect import detect_people
from density import classify_density

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process')
def process_video():
    cap = cv2.VideoCapture("sample_videos/demo.mp4")
    density_history = []
    status = "Unknown"

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        count = detect_people(frame)
        status = classify_density(count)
        density_history.append(count)

    cap.release()

    return {
        "Total Frames Processed": len(density_history),
        "Last Frame Count": density_history[-1] if density_history else 0,
        "Status": status
    }

if __name__ == '__main__':
    app.run(debug=True)
