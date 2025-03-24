from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import numpy as np

app = Flask(__name__)

# Add global variables for counting
correct_count = 0
incorrect_count = 0

# Add global variables for squats counting
squats_correct = 0
squats_incorrect = 0

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

def generate_frames():
    global correct_count, incorrect_count
    cap = cv2.VideoCapture(0)
    state = None
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

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
                        correct_count += 1
                        temp = 0
                    elif temp < 160 and temp >90:
                        incorrect_count += 1
                        temp = 0
                if angle < 160 and angle > 90 and state == 'down':
                    state = "mid_down"
                    temp = angle
                if angle <= 30:
                    state = "up"
                    temp = angle

                # Set colors based on curl form
                landmark_color = (0, 255, 0)  # default green
                connection_color = (0, 255, 0)  # default green
                
                if state == "mid_down":
                    if temp > 90:  # incorrect form
                        landmark_color = (0, 0, 255)  # red
                        connection_color = (0, 0, 255)  # red
                
                # Render detection with dynamic colors
                mp_drawing.draw_landmarks(
                    image, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=landmark_color, thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=connection_color, thickness=2, circle_radius=2)
                )
            except:
                pass

            # Display counts
            cv2.rectangle(image, (image.shape[1] - 250, 0), (image.shape[1], 50), (0, 255, 0), -1)  # Green background for correct count
            cv2.putText(image, 'CORRECT', (image.shape[1] - 240, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, str(correct_count), (image.shape[1] - 80, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.rectangle(image, (image.shape[1] - 250, 60), (image.shape[1], 110), (0, 0, 255), -1)  # Red background for incorrect count
            cv2.putText(image, 'INCORRECT', (image.shape[1] - 240, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, str(incorrect_count), (image.shape[1] - 60, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

def generate_squats_frames():
    global squats_correct, squats_incorrect
    cap = cv2.VideoCapture(0)
    state = None
    temp = 160
    lowest_angle = 160 
    
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            result = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = result.pose_landmarks.landmark
                
                hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                
                angle = calculate_angle(hip, knee, ankle)

                if angle > 150:  
                    if state == "down":
                        if lowest_angle < 90:  
                            squats_correct += 1
                        else: 
                            squats_incorrect += 1
                    state = "up"
                    lowest_angle = 160  
                elif angle <= 150:  
                    if state == "up" or state == "mid":
                        state = "down"
                    lowest_angle = min(lowest_angle, angle)  


                landmark_color = (0, 255, 0)  # default green
                connection_color = (0, 255, 0)  # default green
                
                if state == "down" and lowest_angle > 90:  
                    landmark_color = (0, 0, 255) 
                    connection_color = (0, 0, 255)  
                
                # Render detection with dynamic colors
                mp_drawing.draw_landmarks(
                    image, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=landmark_color, thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=connection_color, thickness=2, circle_radius=2)
                )
            except:
                pass

            # Display counts
            cv2.rectangle(image, (image.shape[1] - 250, 0), (image.shape[1], 50), (0, 255, 0), -1)
            cv2.putText(image, 'CORRECT', (image.shape[1] - 240, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, str(squats_correct), (image.shape[1] - 80, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.rectangle(image, (image.shape[1] - 250, 60), (image.shape[1], 110), (0, 0, 255), -1)
            cv2.putText(image, 'INCORRECT', (image.shape[1] - 240, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(image, str(squats_incorrect), (image.shape[1] - 60, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/reset_counts')
def reset_counts():
    global correct_count, incorrect_count
    correct_count = 0
    incorrect_count = 0
    return "Counts reset", 200

@app.route('/reset_squats_counts')
def reset_squats_counts():
    global squats_correct, squats_incorrect
    squats_correct = 0
    squats_incorrect = 0
    return "Counts reset", 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/squats_feed')
def squats_feed():
    return Response(generate_squats_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
