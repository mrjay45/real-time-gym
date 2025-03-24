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

- ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat&logo=flask)
- ![OpenCV](https://img.shields.io/badge/-OpenCV-5C3EE8?style=flat&logo=opencv)
- ![MediaPipe](https://img.shields.io/badge/-MediaPipe-00FF00?style=flat)
- ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy)

## 🤝 Contributing

align="center">
Contributions are welcome! Feel free to:mg src="https://raw.githubusercontent.com/opencv/opencv/master/samples/data/opencv-logo.png" width="40"/>
<br />OpenCV

- 🐛 Report bugs
- 💡 Suggest features <td align="center">
  <img src="https://raw.githubusercontent.com/google/mediapipe/master/docs/images/mediapipe_small.png" width="40"/>
  <br />MediaPipe

## 📄 License

">
<img src="https://numpy.org/images/logo.svg" width="40"/>under the MIT License - see the [LICENSE](LICENSE) file for details.
<br />NumPy

---

  </tr>
<div align="center">
  Made with ❤️ for fitness enthusiasts
## 🤝 Contributingiv>
Contributions are welcome! Feel free to:- 🐛 Report bugs- 💡 Suggest features
- 🔧 Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  Made with ❤️ for fitness enthusiasts
</div>
