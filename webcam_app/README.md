# Webcam Exercise Tracker App

A Flask-based web application that uses computer vision to track exercise form and count repetitions in real-time.

## Features

### Exercise Tracking

- **Bicep Curls**
  - Tracks arm angle during curls
  - Counts correct/incorrect repetitions
  - Green landmarks for correct form
  - Red landmarks for incorrect form
- **Squats**
  - Monitors squat depth and form
  - Tracks hip-knee-ankle angles
  - Visual feedback with color changes
  - Separate correct/incorrect counters

## Technical Details

### Dependencies

- Flask (web framework)
- OpenCV (computer vision)
- MediaPipe (pose detection)
- NumPy (calculations)

### Key Components

- `app.py`: Main application file
  - Flask routes for web interface
  - Real-time video processing
  - Exercise form detection
  - Repetition counting logic

### Usage

1. Start the server:

   ```
   python app.py
   ```

2. Open a web browser and navigate to:

   ```
   http://localhost:5000
   ```

3. Allow camera access when prompted

### Exercise Form Criteria

- **Bicep Curls**

  - Correct: Full range of motion (160° to 30°)
  - Incorrect: Partial range or improper form

- **Squats**
  - Correct: Depth below 90° knee angle
  - Incorrect: Insufficient depth or improper form

## API Endpoints

- `/`: Main interface
- `/video_feed`: Bicep curl tracking stream
- `/squats_feed`: Squat tracking stream
- `/reset_counts`: Reset bicep curl counters
- `/reset_squats_counts`: Reset squat counters

## Detailed Setup and Running Instructions

1. Environment Setup

   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # For Windows:
   venv\Scripts\activate
   # For Linux/Mac:
   source venv/bin/activate
   ```

2. Dependencies Installation

   ```bash
   # Install all required packages
   pip install flask
   pip install opencv-python
   pip install mediapipe
   pip install numpy
   ```

3. Application Structure Check

   ```bash
   webcam_app/
   ├── app.py
   ├── templates/
   │   └── index.html
   └── README.md
   ```

4. Running Instructions

   ```bash
   # Navigate to webcam_app directory
   cd webcam_app

   # Run Flask application
   python app.py
   ```

5. Access and Usage

   - Open browser: http://localhost:5000
   - Initial Setup:
     - Allow camera permissions
     - Face the camera properly
     - Ensure good lighting
   - Exercise Selection:
     - Choose exercise type from interface
     - Follow on-screen form guidance
     - Monitor rep counts and form feedback

6. Common Issues and Solutions
   - Camera not detected:
     - Check USB connection
     - Verify camera permissions
   - Performance issues:
     - Close other camera applications
     - Ensure sufficient lighting
   - Counter not working:
     - Check if full body is visible
     - Verify proper exercise form
