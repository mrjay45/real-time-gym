from flask import Flask, render_template, Response, request
import cv2
import mediapipe as mp
import numpy as np
import os

app = Flask(__name__)

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radian = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radian * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

def generate_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    correct = 0
    incorrect = 0
    state = None
    temp = 0
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while True:
            ret, frame = cap.read()
            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  
                continue

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            result = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = result.pose_landmarks.landmark
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                angle = calculate_angle(shoulder, elbow, wrist)

                # Bicep curl logic
                if angle > 160:
                    state = "down"
                    if temp <= 30 and temp > 20:
                        correct += 1
                        temp = 0
                    elif temp < 160 and temp >90:
                        incorrect += 1
                        temp = 0
                if angle < 160 and angle > 90 and state == 'down':
                    state = "mid_down"
                    temp = angle
                if angle <= 30:
                    state = "up"
                    temp = angle
            except:
                pass

            # Render detection
            mp_drawing.draw_landmarks(image, result.pose_landmarks, mp_pose.POSE_CONNECTIONS, mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2), mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2))

            # Display counts
            cv2.rectangle(image, (image.shape[1] - 350, 0), (image.shape[1], 73), (0, 255, 0), -1)  # Green background for correct count
            cv2.putText(image, 'CORRECT', (image.shape[1] - 335, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, str(correct), (image.shape[1] - 60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.rectangle(image, (image.shape[1] - 350, 75), (image.shape[1], 148), (0, 0, 255), -1)  # Red background for incorrect count
            cv2.putText(image, 'INCORRECT', (image.shape[1] - 335, 115), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, str(incorrect), (image.shape[1] - 60, 115), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2, cv2.LINE_AA)

            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return "No video file provided", 400
    file = request.files['video']
    if file.filename == '':
        return "No selected file", 400
    
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    video_path = os.path.join(upload_folder, file.filename)
    file.save(video_path)
    return render_template('video.html', video_path=video_path)

@app.route('/video_feed/<path:video_path>')
def video_feed(video_path):
    return Response(generate_frames(video_path), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
