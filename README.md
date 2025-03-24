# 🏋️‍♂️ Real Time Gym - AI Exercise Form Tracker

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-red.svg)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🎯 Your personal AI-powered fitness coach that provides real-time form feedback!

<div align="center">
  <img src="./outputs/bicep_curl_form.png" width="400" />
</div>

## ✨ Features

- 🎥 Real-time exercise form detection
- 🔢 Smart repetition counting
- 🚦 Visual feedback with color-coded pose tracking
  - 🟢 Green: Perfect form
  - 🔴 Red: Form needs improvement
- 🏋️ Supported Exercises:
  - 💪 Bicep Curls
  - 🦵 Squats

## 📝 Exercise Form Guidelines

### 💪 Bicep Curls

| Position          | Angle      | Status       |
| ----------------- | ---------- | ------------ |
| Full curl         | ≤ 30°      | ✅ Correct   |
| Partial curl      | 90° - 160° | ❌ Incorrect |
| Starting position | > 160°     | ➡️ Ready     |

<div align="center">
  <img src="./outputs/bicep_curl_form.png" width="400" />
  <p><i>Bicep Curl Form Detection in Action</i></p>
</div>

### 🦵 Squats

| Position      | Angle       | Status       |
| ------------- | ----------- | ------------ |
| Deep squat    | < 110°      | ✅ Correct   |
| Partial squat | 110° - 150° | ❌ Incorrect |
| Standing      | > 150°      | ➡️ Ready     |

<div align="center">
  <img src="./outputs/squat_form.png" width="400" />
  <p><i>Squat Form Detection in Action</i></p>
</div>

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Webcam or video input

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/real-time-gym.git

# Install dependencies
pip install flask opencv-python mediapipe numpy
```

### Usage

```bash
# Run the application
python app.py
```

Then:

1. 🌐 Open your browser and go to `http://localhost:5000`
2. 📤 Upload your exercise video
3. 🎯 Select exercise type
4. 📊 Get real-time form feedback!

## 🛠️ Technologies

<table>
  <tr>
    <td align="center"><img src="https://flask.palletsprojects.com/en/2.0.x/_static/flask-icon.png" width="40"/><br />Flask</td>
    <td align="center"><img src="https://opencv.org/wp-content/uploads/2020/07/OpenCV_logo_no_text-1.png" width="40"/><br />OpenCV</td>
    <td align="center"><img src="https://developers.google.com/static/mediapipe/images/mediapipe.png" width="40"/><br />MediaPipe</td>
    <td align="center"><img src="https://numpy.org/images/logo.svg" width="40"/><br />NumPy</td>
  </tr>
</table>

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Made with ❤️ for fitness enthusiasts
</div>
