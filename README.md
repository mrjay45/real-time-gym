# Real-Time Gym Exercise Tracker

A Python-based application that uses computer vision to track and evaluate exercise form in real-time.

## Project Structure

```
real time gym/
├── webcam_app/           # Main application directory
│   ├── app.py           # Flask application for exercise tracking
│   ├── templates/       # HTML templates
│   └── README.md        # Webcam app documentation
└── README.md            # Main project documentation
```

## Features

- Real-time exercise form detection
- Support for multiple exercises:
  - Bicep Curls
  - Squats
- Visual feedback with color-coded pose detection
- Exercise repetition counting

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- Flask
- NumPy

## Getting Started

1. Clone this repository
2. Install dependencies:
   ```
   pip install flask opencv-python mediapipe numpy
   ```
3. Navigate to the webcam_app folder
4. Run the application:
   ```
   python app.py
   ```

## Installation and Running Procedure

1. Clone this repository or download the source code
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   # Or install individually:
   pip install flask opencv-python mediapipe numpy
   ```
4. Setup procedure:
   ```bash
   cd webcam_app
   mkdir templates  # If not exists
   ```
5. Running the application:
   ```bash
   python app.py
   ```
6. Access the application:

   - Open your browser
   - Navigate to http://localhost:5000
   - Allow camera access when prompted
   - Select exercise type (Bicep Curls or Squats)

7. Troubleshooting:
   - Ensure webcam is properly connected
   - Check if port 5000 is available
   - Verify all dependencies are installed correctly

## License

This project is open source and available under the MIT License.
