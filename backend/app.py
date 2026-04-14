from flask import Flask, Response
import cv2
import numpy as np
from ultralytics import YOLO
from sort import Sort

app = Flask(__name__)

model = YOLO("yolov8n.pt")
tracker = Sort()
@app.route('/count')
def count():
    return {"total": len(unique_ids)}

# IMPORTANT: बाहर रखना
unique_ids = set()

def generate_frames():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("❌ Camera not opened")
        return

    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, frame = cap.read()

        if not success:
            continue   # ❗ FIX

        results = model(frame)

        detections = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                conf = float(box.conf[0])
                cls = int(box.cls[0])

                # PERSON detection
                if conf > 0.2 and cls == 0:
                    detections.append([x1, y1, x2, y2, conf])

        # Tracking
        if len(detections) > 0:
            tracks = tracker.update(np.array(detections))
        else:
            tracks = []

        for t in tracks:
            x1, y1, x2, y2, track_id = map(int, t)

            unique_ids.add(track_id)

            # Draw box
            cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame, f"ID {track_id}",
                        (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0,255,0),
                        2)

        # Total count
        cv2.putText(frame, f"Total Persons: {len(unique_ids)}",
                    (20,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255,255,0),
                    2)

        # Encode frame
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame = buffer.tobytes()

        # Stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)